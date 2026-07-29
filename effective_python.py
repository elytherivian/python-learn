import sys
from datetime import UTC, datetime


def main():

    # Effective Python: 90 Specific Ways to Write Better Python

    # 1、查询自己使用的 python 版本
    print(sys.version)
    print(sys.version_info)

    # 2、遵循 PEP 8 风格
    print("Using Ruff 'charliermarsh.ruff' to check code style and formatting issues.")

    # 3、bytes and str
    #### 二进制数据 <--> Unicode 字符串
    #### str.encode("utf-8") & bytes.decode("utf-8")
    #### 顶层程序应当处理 Unicode 字符串，而不是字节数据
    data_str = "Hello, String!"
    data_bytes = data_str.encode("utf-8")
    print(f"Encoded bytes: {data_bytes}")
    data_str_back = data_bytes.decode("utf-8")
    print(f"Decoded string: {data_str_back}")

    # 4、实用 f-string 定义字符串
    #### demo 日志记录
    level = "INFO"
    module = "database"
    message = "Connection established"
    print(
        f"[{datetime.now(UTC):%Y-%m-%d %H:%M:%S}] [{level:<5}] [{module:<10}] {message}"
    )


if __name__ == "__main__":
    main()
