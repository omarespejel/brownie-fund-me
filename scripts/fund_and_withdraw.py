from brownie import FundMe
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def fund():
    account = get_account()
    if len(FundMe) <= 0:
        print("We did not have FundMe contract deployed; deploying now.")
        fund_me = deploy_fund_me()
    else:
        print("We had FundMe contract deployed, not need to redeploy.")
        fund_me = FundMe[-1]

    print(f"fund_me is: {fund_me} and of type {type(fund_me)}")

    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee is: {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee + 1})

    print(
        f"The current amount in the account is: {fund_me.addressToAmountFunded(account.address)}"
    )


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
