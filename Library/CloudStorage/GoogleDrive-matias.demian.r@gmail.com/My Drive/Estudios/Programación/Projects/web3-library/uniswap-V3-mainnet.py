from web3 import Web3
import json
import dotenv as _dotenv
import os as os
import time

_dotenv.load_dotenv()

infura_url = os.environ["INFURA_URL"]
web3 = Web3(Web3.HTTPProvider(infura_url))

# Log
if web3.isConnected() == True:
    print('Logged in')
else:
    print('Not logged')
print()

# ABI's
with open('./utils/contract_factory.json', 'r') as f:
  abi_contract_factory = json.load(f)

with open('./utils/pools.json', 'r') as f:
  abi_pools = json.load(f)

with open('./utils/router.json', 'r') as f:
    abi_router = json.load(f)

# Address V3
factoryAddress = web3.toChecksumAddress('0x1F98431c8aD98523631AE4a59f267346ea31F984')
routerAddress = web3.toChecksumAddress('0xE592427A0AEce92De3Edee1F18E0157C05861564')
account = web3.toChecksumAddress('0x596FbF10a5129fa7ae38FD6135C0954d415ea7Bc')
poolAddress = web3.toChecksumAddress('0x8ad599c3A0ff1De082011EFDDc58f1908eb6e6D8')

daiAddress = web3.toChecksumAddress('0x6B175474E89094C44Da98b954EedeAC495271d0F')
usdcAddress = web3.toChecksumAddress('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')
wethAddress = web3.toChecksumAddress('0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2')

contractFactory = web3.eth.contract(address = factoryAddress, abi = abi_contract_factory)
routerContract = web3.eth.contract(address = routerAddress, abi = abi_router)
poolContract = web3.eth.contract(address = poolAddress, abi = abi_pools)

# direcpool = web3.toChecksumAddress(contractFactory.functions.getPair(wethAddress,usdcAddress).call())
# print(direcpool)

token1Address = web3.toChecksumAddress(poolContract.functions.token0().call())
token2Address = web3.toChecksumAddress(poolContract.functions.token1().call())

contract1 = web3.eth.contract(address = token1Address, abi = abi_pools)
contract2 = web3.eth.contract(address = token2Address, abi = abi_pools)

tokenBalance = poolContract.functions.getReserves().call()

# token1Symbol = contract1.functions.symbol().call()
# token2Symbol = contract2.functions.symbol().call()

# print(poolAddress)
# print()

### Token 1 ####
#print(token1Symbol)
print("Address token 1: " + f"{token1Address}")
print("# Tokens: " + f"{web3.fromWei(tokenBalance[0], 'ether')}")
print()

### Token 2 ####
#print(token2Symbol)
print("Address token 2: " + f"{token2Address}")
#print("# Tokens: " + f"{web3.fromWei(tokenBalance[1], 'ether')}")
print()