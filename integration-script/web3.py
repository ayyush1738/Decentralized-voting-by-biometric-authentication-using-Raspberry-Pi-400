import json
from web3 import Web3

# connect to the Ganache testnet server
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# import the contract ABI and address
with open('contract_abi.json', 'r') as f:
    abi = json.loads(f)
contract_address = web3.toChecksumAddress("0x809800336c519F998dF9283aC245cD6395594c8F") # replace with actual contract address

# instantiate the contract
contract = web3.eth.contract(address=contract_address, abi=abi)

# define some example voter IDs
voter_ids = ["6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b",
             "d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35",
             "4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce",
             "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
             "ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d"]

# verify a voter's eligibility to vote
def verify_voter(id):
    print(contract.functions.verify(id).call())

# cast a vote for party 1
def cast_vote_party1(id):
    tx_hash = contract.functions.castvoteparty1(id).transact({'from': web3.eth.accounts[0]})
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt

# cast a vote for party 2
def cast_vote_party2(id):
    tx_hash = contract.functions.castvoteparty2(id).transact({'from': web3.eth.accounts[0]})
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt

# cast a vote for party 3
def cast_vote_party3(id):
    tx_hash = contract.functions.castvoteparty3(id).transact({'from': web3.eth.accounts[0]})
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return tx_receipt

# print the current state of the voter list and vote counts
def print_state():
    voter_list = contract.functions.arr().call()
    party1_votes = contract.functions.p1().call()
    party2_votes = contract.functions.p2().call()
    party3_votes = contract.functions.p3().call()
    print("Current state:")
    print("Voter list: {}".format(voter_list))
    print("Party 1 votes: {}".format(party1_votes))
    print("Party 2 votes: {}".format(party2_votes))
    print("Party 3 votes: {}".format(party3_votes))

# example usage
print("Verifying voters:")
for id in voter_ids:
    print("{}: {}".format(id, verify_voter(id)))

print("\nCasting votes:")
for id in voter_ids:
    print("Casting vote for {}...".format(id))
    cast_vote_party1(id)
print_state()
