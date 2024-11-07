
from datetime import datetime

def save_wallet_to_file(wallet, address_start):
    """将找到的钱包信息保存到文件。"""
    filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{address_start}.txt"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(f"助记词: {wallet['seed_phrase']}\n")
        f.write(f"私钥: {wallet['private_key']}\n")
        f.write(f"地址: {wallet['address']}\n")
    print(f"信息已保存到文件: {filename}")
