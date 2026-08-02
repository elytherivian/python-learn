from datetime import datetime
from zoneinfo import ZoneInfo


def main():

    # Effective Python: 90 Specific Ways to Write Better Python

    ##############################################################################
    # chapter 3: functions
    ##############################################################################

    # 19、函数返回值最多三个 返回值过多容易出错

    # 20、遇到意外情况应该抛出异常 不要返回 None
    #### 出现异常应该抛出 让上级去处理异常
    #### 当然也不是到处 try except 判定 由 api 层处理

    # 21、在闭包里面使用外围作用域的变量
    #### 除特别简单的函数外 不要使用 nonlocal

    # 22、用数量可变的位置参数给函数设计清晰的参数列表
    #### 可变位置参数 star args *args
    #### *args 接受的数据是一个元组 tuple
    def log_args(*args):
        print("Logging arguments:")
        for arg in args:
            print(arg)
        print(f"All arguments: {args}")

    log_args("apple", "banana", "cherry")

    # 23、用关键字参数来表示可选行为
    #### 函数参数中使用关键字可以给关键字赋默认值 方便调用者使用
    #### 同时给函数增加新的关键字默认值时 不影响现有代码逻辑
    def log_message(message: str, level: str = "INFO"):
        print(f"[{level}] {message}")

    log_message("This is an info message")
    log_message("This is a warning message", level="WARNING")
    log_message("This is an error message", level="ERROR")

    #### 万能形参 **kwargs 接受参数整合成字典数据
    def log_kwargs(**kwargs):
        print("Logging keyword arguments:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        print(f"All keyword arguments: {kwargs}")

    log_kwargs(alpha=1, beta=2, gamma=3)

    # 24、用 None 和 docstring 来描述默认值会变的关键字参数
    #### 参数默认值只会计算一次 即 系统把定义函数加载进来的时候
    #### 如果默认值是可变对象 会导致函数多次调用时使用同一个对象
    def log_message_with_time(message, when=None):
        #### 这里的 when 如果默认值直接计算 那么这个默认值会固定 之后都是一个数据
        if when is None:
            when = datetime.now().astimezone(ZoneInfo("Asia/Shanghai"))
        print(f"[{when}] : {message}")

    log_message_with_time("This is a log message with time")
    log_message_with_time("another log message with time")

    #### 如果默认值是可变对象 如 dict 在加载函数时创建默认 dict
    #### 那么之后每次调用函数时 都会使用同一个 dict 对象

    #### 若关键字默认值会发生变化 则应当设置为 None
    #### 同时在函数中处理为 None 的默认行为 并在 docstring 中说明默认行为


if __name__ == "__main__":
    main()
