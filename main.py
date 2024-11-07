
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from config import config
from utils.wallet_utils import generate_wallet, matches_address
from utils.file_utils import save_wallet_to_file

def wallet_search(process_id, stop_event):
    attempts = 0
    while not stop_event.is_set():
        wallet = generate_wallet()
        attempts += 1
        if config["show_log"] and attempts % config["log_count"] == 0:
            print(f"进程 {process_id}: 尝试生成 {attempts} 次")

        if matches_address(wallet["address"], config["address_start"], config["address_end"]):
            stop_event.set()
            save_wallet_to_file(wallet, config["address_start"])
            return wallet

def main():
    with multiprocessing.Manager() as manager:
        stop_event = manager.Event()
        with ProcessPoolExecutor(max_workers=config["num_processes"]) as executor:
            futures = [executor.submit(wallet_search, i + 1, stop_event) for i in range(config["num_processes"])]
            for future in futures:
                wallet = future.result()
                if wallet:
                    print(f"找到符合条件的钱包！地址: {wallet['address']}")
                    break

if __name__ == "__main__":
    main()
