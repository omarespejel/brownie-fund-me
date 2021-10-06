from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(f"The active network is {network.show_active()}")
        print("No need to deploy mocks")

        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

        print(f"Price feed address: {price_feed_address}")

    # pass the price feed address to our fundme contract
    # Todo lo que se ponga en el constructor debe ser dado en el .deploy del contrato
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    print(f"We are returning an object of type {type(fund_me)}")
    return fund_me


def main():
    deploy_fund_me()
