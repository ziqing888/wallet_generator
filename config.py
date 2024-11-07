# config.py

import multiprocessing

config = {
    "address_start": "0xaf",  # 地址的开头（不重要则留空）
    "address_end": "",  # 地址的结尾（不重要则留空）
    "num_processes": multiprocessing.cpu_count() - 1,  # 并行进程数量
    "show_log": True,  # 是否显示日志
    "log_count": 50    # 每隔多少次生成显示一次日志
}
