from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork-dev"]

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["ganache-local", "development"]

DECIMALS = 18
STARTING_PRICE = 2000


def get_account():
    if (
        # show_ative displays the blockchain we are connected to
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        # In case we are not connected to local network, use our metamask keys
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print("The active network is " + str(network.show_active()))
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": accounts[0]}
        )

    print("Mocks deployed!")
