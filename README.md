# 以太坊钱包生成器

## 项目简介
该脚本用于生成以太坊钱包，直到找到符合指定地址模式的钱包。

## 使用说明
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 修改 `config.py` 文件中的配置信息。
3. 运行 `main.py`：
   ```bash
   python3 main.py

   ```

## 配置说明
- `address_start`：指定钱包地址的开头字符匹配。
- `address_end`：指定钱包地址的结尾字符匹配。
- `num_processes`：并行进程数量，建议设置为 `CPU核心数 - 1`。
- `show_log`：是否显示生成日志信息。
- `log_count`：每隔多少次生成记录一次日志。
