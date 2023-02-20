import dotenv as _dotenv
import os as os
import requests

_dotenv.load_dotenv()
KEY_ETHEREUM = os.environ["KEY_ETHEREUM"]

def ethereum(address: str) -> str:
    _URL = 'https://api.etherscan.io/api'
    _KEY = KEY_ETHEREUM

    payload = {'module': 'contract',
               'action': 'getabi',
               'address': address.lower(),
               'apiKey': _KEY}

    req = requests.get(_URL, params=payload)
    res = req.json()

    return res['result']