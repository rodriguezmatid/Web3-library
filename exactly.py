from web3 import Web3
import json
import dotenv as _dotenv
import os as os

_dotenv.load_dotenv()

# ##########################
# ###### Mainnet ######
# ##########################
infura_url = os.environ["INFURA_URL"]
web3 = Web3(Web3.HTTPProvider(infura_url))

with open('./utils/marketExactly.json', 'r') as f:
    abi_market = json.load(f)

market = web3.toChecksumAddress('0x1F29D4E11881e1A44409FE455A864295f06573d9')

wethAddress = web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')
usdcAddress = web3.toChecksumAddress('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
daiAddress = web3.toChecksumAddress('0x6B175474E89094C44Da98b954EedeAC495271d0F')
uniAddress = web3.toChecksumAddress('0x1f9840a85d5af5bf1d1762f925bdaddc4201f984')

contractMarket = web3.eth.contract(address = market, abi = abi_market)

wethreserve = contractMarket.functions.totalAssets().call()
print(wethreserve)