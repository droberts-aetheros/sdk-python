#! /usr/bin/env python

# Copyright (c) Aetheros, Inc.  See COPYRIGHT

import argparse

from .client.onem2m.http.OneM2MRequest import OneM2MRequest
from .client.onem2m.OneM2MPrimitive import OneM2MPrimitive
from .client.cse.CSE import CSE
from .client.ae.AE import AE

from requests import HTTPError
import subprocess
import traceback

import os, sys, json, time

class CseEndpoint(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

class AeRegistrationRequest(object):
    def __init__(self, app_id, app_name, credential, poa=['http://localhost:7000']):
        self.app_id = app_id
        self.app_name = app_name
        self.credential = credential
        self.poa = poa

def register_ae(cse, app_id, credential, app_name=None):
    to = f'{cse.transport_protocol}://{cse.host}:{cse.port}/PN_CSE'

    # op is not required as it is implied by the function that the params will be passed to.
    params = {
        OneM2MPrimitive.M2M_PARAM_TO: to,
        OneM2MPrimitive.M2M_PARAM_FROM: credential,
        OneM2MRequest.M2M_PARAM_RESOURCE_TYPE: OneM2MPrimitive.M2M_RESOURCE_TYPES.AE.value
    }

    ae = {
        AE.M2M_ATTR_APP_ID: app_id,
        AE.M2M_ATTR_POINT_OF_ACCESS: ['http://localhost:7000'],
    }

    if app_name is not None:
        ae[AE.M2M_ATTR_APP_NAME] = app_name

    # Create a request object
    oneM2MRequest = OneM2MRequest()

    # Returns a OneM2MResponse object.  Handle any response code logic here.
    oneM2MResponse = oneM2MRequest.create(to, params, {'ae': ae})

    return oneM2MResponse

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--register', default=False, action='store_true')
parser.add_argument('-i', '--ae-id')
parser.add_argument('-a', '--app-id')
parser.add_argument('-n', '--app-name', default=None)
parser.add_argument('--credential')
parser.add_argument('-c', '--cse-address', required=True)
parser.add_argument('--http', default=False, action='store_true')

args = parser.parse_args()

cse_host, cse_port = args.cse_address.split(':')

transport = 'https'
if args.http:
    transport = 'http'

cse = CSE(cse_host, cse_port , transport_protocol = transport)

if args.register:
    try:
        resp = register_ae(cse, args.app_id, args.credential, args.app_name)

        # None indicates failed registration.
        if resp.rsc != OneM2MPrimitive.M2M_RSC_CREATED:
            print(f"E: Failed to register AE", file=sys.stderr)
            sys.exit(1)

        resp.dump('AE resp')
    except HTTPError as e:
        traceback.print_exc()
        print(f"Resp:\n{e.response.text}")
else:
    parser.print_help()
