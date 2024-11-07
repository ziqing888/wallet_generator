
from eth_account import Account
from mnemonic import Mnemonic
from eth_utils import to_checksum_address

mnemo = Mnemonic("english")
Account.enable_unaudited_hdwallet_features()

def generate_wallet():
    """生成钱包并返回助记词、私钥和地址。"""
    seed_phrase = mnemo.generate(strength=128)
    account = Account.from_mnemonic(seed_phrase)
    private_key = account.key.hex()
    address = to_checksum_address(account.address)
    return {"seed_phrase": seed_phrase, "private_key": private_key, "address": address}

def matches_address(address, start, end):
    """检查地址是否符合指定的开头和/或结尾。"""
    address = address.lower()
    start = start.lower()
    end = end.lower()
    return (start == "" or address.startswith(start)) and (end == "" or address.endswith(end))
