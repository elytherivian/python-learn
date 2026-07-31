import sys
from datetime import datetime
from zoneinfo import ZoneInfo


def main():

    # Effective Python: 90 Specific Ways to Write Better Python

    ##############################################################################
    # chapter 1: Pythonic Thinking
    ##############################################################################

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

    # 4、使用 f-string 定义字符串
    #### demo 日志记录
    level = "INFO"
    module = "database"
    message = "Connection established"
    shanghai = ZoneInfo("Asia/Shanghai")
    print(
        # 遵循 （# 5、使用辅助函数代替复杂表达式）
        f"[{datetime.now(shanghai):%Y-%m-%d %H:%M:%S}] [{level:<5}] [{module:<10}] {message}"
    )

    def log(level: str, module: str, message: str) -> None:
        print(
            f"[{datetime.now(shanghai):%Y-%m-%d %H:%M:%S}] [{level:<5}] [{module:<10}] {message}"
        )

    log(level, module, message)

    # 5、使用辅助函数代替复杂表达式
    #### if-else 表达式比 or and 的布尔表达式要好懂
    #### DRY(Don't Repeat Yourself) 原则 避免重复代码
    #### 重复使用的复杂表达式写到辅助函数里
    #### 使用业务语言代替逻辑语言

    # 6、使用 unpacking 机制读取数据到多个变量 而不是使用下标索引访问数据
    #### 索引应该服务于业务 而不是成为获取元素的默认工具
    snacks = [("bacon", 350), ("donut", 200), ("cookie", 150)]
    for i in range(len(snacks)):
        item = snacks[i]
        # 这里就是使用下标索引访问元组内数据
        snack = item[0]
        calories = item[1]
        print(f"#{i + 1}: {snack} has {calories} calories")

    for rank, (name, calories) in enumerate(snacks, start=1):
        # 这里就是使用 unpacking 机制读取数据到多个变量
        print(f"#{rank}: {name} has {calories} calories")
        #### enumerate 需要一个有顺序的可迭代对象

    # 7、使用 enumerate 代替 range
    #### 结合 unpacking 机制
    singers = ["adele", "beyonce", "carrie"]
    it = enumerate(singers, start=1)
    print(next(it))
    print(next(it))

    # 8、使用 zip 同时遍历多个迭代器
    #### 如果多个迭代器的长度不一致 zip 会在最短的迭代器耗尽时停止迭代
    names = ["alice", "bob", "charlie"]
    counts = [5, 3, 7]
    max_count = 0
    longest_name = None
    for name, count in zip(names, counts):
        if count > max_count:
            max_count = count
            longest_name = name
    print(f"The longest name is {longest_name} with a count of {max_count}")

    # 9、不要在 for while 循环后使用 else
    #### Python 特殊语法 会让人看不懂含义

    # 10、使用赋值表达式（walrus operator :=）以减少重复代码
    #### 被赋值变量成为表达式结果
    fruit = {
        "apple": 10,
        "banana": 8,
        "orange": 99,
    }

    def make_orange_juice(count: int):
        print(f"Making {count} orange juice(s)")

    def out_of_stock():
        print("Out of stock!")

    if count := fruit.get("orange", 0):
        make_orange_juice(count)
    else:
        out_of_stock()

    ##############################################################################
    # chapter 2: list and dict
    ##############################################################################


if __name__ == "__main__":
    main()
