from collections import defaultdict


def main():

    # Effective Python: 90 Specific Ways to Write Better Python

    ##############################################################################
    # chapter 2: list and dict
    ##############################################################################

    # 11、学会对 list 做 slice 切片
    #### attention 列表的切片操作得到的是列表的浅拷贝
    data = ["a", "b", "c", "d", "e", "f", "g", "h"]
    #### 从头开始取列表应该取消左下标
    assert data[:5] == data[0:5]
    print("data[:5] == data[0:5]")
    #### 取到列表末尾应该取消右下标
    assert data[5:] == data[5 : len(data)]
    print("data[5:] == data[5:len(data)]")
    data_copy = data[:]
    assert data_copy == data and data_copy is not data
    print("data_copy == data and data_copy is not data")

    # 12、不要在切片操作中同时指定起止下标与步进
    #### 这样会让切片操作理解困难

    # 13、通过带有 * 操作的 unpacking 机制来捕捉多个元素 不要用切片
    #### 在切片操作过程中使用下标会让代码看起来很乱 同时很容易出错
    car_age = [3, 5, 7, 9, 11]
    first = car_age[0]
    second = car_age[1]
    rest = car_age[2:]
    print(f"first: {first}, second: {second}, rest: {rest}")

    #### 使用带 * 表达式 也是一种 unpacking 操作
    first, second, *rest = car_age
    print(f"first: {first}, second: {second}, rest: {rest}")

    #### 同时可以出现在任何地方
    first, *others, last = car_age
    print(f"first: {first}, others: {others}, last: {last}")
    *others, second_last, last = car_age
    print(f"others: {others}, second_last: {second_last}, last: {last}")

    #### repeat 使用下标访问数据很容易出错 上下文牵连

    # 14、使用 sort 方法的 key 参数来表示复杂排序逻辑
    #### 具备自然顺序的内置类型都可以使用 sort 排序
    numbers = [5, 2, 9, 1, 7]
    numbers.sort()
    print(f"Sorted numbers: {numbers}")

    #### 一般对象如何排序？
    class Tool:
        def __init__(self, name: str, weight: int):
            self.name = name
            self.weight = weight

        def __repr__(self):
            # 该方法用于返回对象的字符串表示，通常用于调试和日志记录
            return f"Tool(name={self.name!r}, weight={self.weight})"

    tools = [
        Tool("hammer", 5),
        Tool("screwdriver", 2),
        Tool("wrench", 3),
        Tool("pliers", 4),
    ]

    #### 很多对象需要在不同情况下使用不同的排序逻辑 此时定义自然排序没有意义
    print(f"Unsorted Tools: {tools}")
    tools.sort(key=lambda x: x.name)
    print(f"Tools sorted by name: {tools}")
    tools.sort(key=lambda x: x.weight)
    print(f"Tools sorted by weight: {tools}")
    #### lambda 表达式是一个匿名函数 表达式就是这个匿名函数的返回值

    #### lambda 表达式返回元组数据实现多条件排序 但是无法实现更复杂的排序逻辑
    #### 对于不支持一元操作符的指标 使用多次调用 sort 方法来实现多条件排序
    tools.sort(key=lambda x: (x.weight, x.name))
    print(f"Tools sorted by weight and name: {tools}")

    # 15、不要过分依赖给字典添加条目时所用的顺序

    # 16、使用 get 处理 key 不在 dict 中的情况 不要使用 in 和 KeyError
    #### 对于非自己创建的字典 处理 key 不在 dict 中的情况
    counters = {"apple": 23, "banana": 10}
    key_orange = "orange"
    count = counters.get(key_orange, 0)
    counters[key_orange] = count + 1
    print(f"Fruit Counters : {counters}")
    #### 使用赋值表达式处理复杂情况
    key_mango = "mango"
    if (count := counters.get(key_mango)) == None:
        counters[key_mango] = 1
    else:
        counters[key_mango] += 1
    print(f"Fruit Counters : {counters}")

    # 17、用 defaultdict 处理内部状态中缺失元素 而不是使用 setdefault
    class Visits:
        def __init__(self):
            #### set 是一种数据类型 这里指默认数据是一个 set 集合
            #### defaultdict 会为不存在的 key 自动创建一个默认值 具体为 set() 集合
            self.data = defaultdict(set)

        def add(self, country: str, city: str):
            self.data[country].add(city)

    visits = Visits()
    visits.add("England", "Bath")
    visits.add("England", "London")
    print(f"Visits : {visits.data}")

    # 18、使用 __missing__ 构建依赖 key 的默认 value 值
    #### 在 dict 中 如果构建的数据 value 需要 key 来确定
    #### 那么可以定义自己的 dict 子类 并实现 __missing__ 方法
    #### 需要根据文件路径来拿到文件句柄 dict[file_path][file_handle]
    def open_picture(file_path: str):
        try:
            return open(file_path, "rb")
        except OSError as e:
            print(f"Error opening picture: {e}")
            raise

    class PictureDict(dict):
        def __missing__(self, file_path: str):
            picture = open_picture(file_path)
            self[file_path] = picture
            return picture

    pictures = PictureDict()
    path = "static/image/buzhihuo.jpg"
    #### 如果 path 不在字典中 会调用 __missing__ 方法打开图片并返回句柄
    handle = pictures[path]
    handle.seek(0)
    image_data = handle.read()
    print(f"Read {len(image_data)} bytes from {path}")


if __name__ == "__main__":
    main()
