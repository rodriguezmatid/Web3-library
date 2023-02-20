from web3 import Web3
import dotenv as _dotenv
import os as os
import utils
from datetime import datetime

rpc = os.environ["ETHEREUM"]
web3 = Web3(Web3.HTTPProvider(rpc))

# Documentation
# https://web3py.readthedocs.io/en/v5/

# Connection to the blockchain
# Allows you to read information about the blockchain, like the blocks and the transactions, create transactions, and interact with smart contracts
if web3.isConnected() == True:
    print('Logged in')
else:
    print('Not logged')

# Number of the last block in the blockchain
lastBlockNumber = web3.eth.blockNumber
print("Last block number")
print(lastBlockNumber)
print()

# information of last block
print('Information of last block')
baseFeePerGas = web3.eth.getBlock(lastBlockNumber)['baseFeePerGas']/(10**9)
timeStamp = web3.eth.getBlock(lastBlockNumber)['timestamp']
print("Base Gas Fee in Gwei: ", "{:,.2f}".format(baseFeePerGas))
print("Date time: ", datetime.fromtimestamp(timeStamp))
print()

# Eth balance from a wallet
wallet = '0x16B34Ce9A6a6F7FC2DD25Ba59bf7308E7B38E186'
balance = web3.eth.get_balance(wallet)
print("Wallet balance in ETH")
print(web3.fromWei(balance, 'ether'))
print()

# Analysis of a contract
tokenAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F'
tokenContract = web3.eth.contract(address = tokenAddress, abi = utils.ethereum(tokenAddress))

# Protocol name
tokenName = tokenContract.functions.name().call()
print("Name: ", tokenName)

# Token Symbol
tokenSymbol = tokenContract.functions.symbol().call()
print("Symbol: ", tokenSymbol)

# Token Decimals
tokenDecimals = tokenContract.functions.decimals().call()
print("Decimals: ", tokenDecimals)

# Total Supply
tokenSupply = tokenContract.functions.totalSupply().call()/(10**tokenDecimals)
print("Supply: ", "{:,.0f}".format(tokenSupply))

# Wallet balance of the token
walletBalance = tokenContract.functions.balanceOf(wallet).call()
print("Token balance in Wallet: ", "{:,.0f}".format(web3.fromWei(walletBalance, 'ether')))
print()

# ###### NEW ENTRIES ######
# def handle_event(event):
#     try:
#         print("From: ", event['address'])
#         # print("To: ", event['to'])
#         print("From: ", event['topics'][1])
#         print("To: ", event['topics'][2])
#         print("Transaction Hash: ", event['transactionHash'].hex())
#         print("Block Number: ", event['blockNumber'])
#         print("\n")
#     except KeyError:
#         print("Could not find expected keys in event:", event)

# def log_loop(event_filter, poll_interval):
#     while True:
#         for event in event_filter.get_new_entries():
#             handle_event(event)
#             time.sleep(poll_interval)

# block_filter = web3.eth.filter({'fromBlock':'latest', 'address':usdt})
# log_loop(block_filter, 2)