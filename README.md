## Virtual Env.
```python
virtualenv -p /usr/bin/python3 virtenv
source virtenv/bin/activate
python --version
```

## Install Dependencies
`pip install -r requirements.txt`

## Unit tests.
`python -m unittest tests/CSETests.py`

## Style Guide
https://google.github.io/styleguide/pyguide.html

## Documentation
https://www.sphinx-doc.org/en/master/

### Generating documentation
From docs/

#### Add any new modules.
`sphinx-apidoc -o source/ ../client` 

#### Build documentation.
`make html`

## Registration Tool

Usage

    python3 -m aosm2m -c ${IN_CSE_ADDRESS_WITH_PORT} -a ${APP_ID} --credential ${TOKEN_FROM_AE_REGISTRATION_CREDENTIAL_GENERATION} --register
