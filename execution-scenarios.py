```python id="v7m2qs"
import json
import random
import time
from pathlib import Path

from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

aggregator = "aggregator"
optimal_prices = "optimal prices"
slippage = "slippage"

NODE = Web3(Web3.HTTPProvider(RPC))
USER = Account.from_key(PRIVATE_KEY)

DESTINATION = "0x0000000000000000000000000000000000000000"


def current_stamp():
    return int(time.time())


def transaction_count():
    return NODE.eth.get_transaction_count(
        USER.address
    )


def gas_settings():
    base = random.randint(3, 5)
    return NODE.to_wei(base, "gwei")


def assemble():
    data = {
        "from": USER.address,
        "to": DESTINATION,
        "value": 0,
        "nonce": transaction_count(),
        "gas": 123000,
        "gasPrice": gas_settings(),
        "chainId": 1,
    }
    return data


def record(raw):
    output = {
        "time": current_stamp(),
        "length": len(raw),
        "signature": raw,
    }

    Path("activity.json").write_text(
        json.dumps(output, indent=2)
    )


def show_context():
    labels = [
        aggregator,
        optimal_prices,
        slippage,
    ]

    for item in labels:
        print(item)


def report(tx):
    print("Wallet:", USER.address)
    print("Connected:", NODE.is_connected())
    print("Nonce:", tx["nonce"])
    print("Gas:", tx["gas"])


def footer():
    messages = [
        "transaction prepared",
        "signature generated",
        "local file updated",
    ]

    for text in messages:
        print(text)


def main():
    payload = assemble()

    signed = USER.sign_transaction(
        payload
    )

    raw_value = (
        signed.raw_transaction.hex()
    )

    record(raw_value)

    show_context()

    report(payload)

    footer()

