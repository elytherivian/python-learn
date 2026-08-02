import json
import sys
import time

import fastapi

MAX_COUNT = 1000


def main():
    print("Python Basic Grammar")
    print(sys.executable)
    print(sys.version)
    print("Hello from python-learning!")
    message = "hello world"
    print(message[0])
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(message.title())
    file = "example.txt"
    print(file.removesuffix(".txt"))
    print(4 / 2)
    names = ["Alice", "Bob", "Charlie"]
    call_name = f"Hello, {names[0]}!"
    print(call_name)

    print(MAX_COUNT)

    names.insert(0, "David")
    print(names)
    poped_name = names.pop()
    print(names)
    print(poped_name)
    print("the length of names is", len(names))
    for name in names:
        print(name)

    print("=============================")
    even_numbers = [2, 4, 6, 8, 10]
    print(sum(even_numbers))

    food_1_list = ["apple", "banana", "cherry"]

    # 此处并不是列表数据的拷贝 而是两个变量指向了同一数据
    food_2_list = food_1_list
    # 这样才是对列表数据进行拷贝
    food_3_list = food_1_list[:]

    # 测试
    food_1_list.append("milk")
    print(food_1_list)
    print(food_2_list)
    print(food_3_list)

    alice_info = {
        "first_name": "alice",
        "last_name": "smith",
        "age": 30,
        "city": "beijing",
    }
    print(alice_info)
    print(alice_info["first_name"])

    def make_pizza(size, *toppings):
        print(f"making a {size}-inch pizza with the following toppings:")
        for topping in toppings:
            print(f"- {topping}")

    make_pizza(12, "pepperoni", "mushrooms", "green peppers")

    def args_kwargs(*args, **kwargs):
        print("args:", args)
        print("kwargs:", kwargs)

    args_kwargs(1, 2, 3, name="Bob", age=30)

    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def sit(self):
            print(f"{self.name} is now sitting.")

        def roll_over(self):
            print(f"{self.name} rolled over!")

    my_dog = Dog("Buddy", 3)
    print(f"My dog's name is {my_dog.name}.")
    my_dog.sit()
    my_dog.roll_over()

    # try-except-else-finally
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        print("Division successful:", result)
    finally:
        print("Execution completed.")

    with open("static/data/data.json", "r") as f:
        content = f.read()
        data = json.loads(content)
        print(data["name"])

    # GitHub API request
    # url = "https://api.github.com/search/repositories"
    # url += "?q=language:python+sort:stars+stars:>100000"
    # headers = {"Accept": "application/vnd.github.v3+json"}
    # r = requests.get(url, headers=headers)
    # print(f"Status code: {r.status_code}")
    # response_dict = r.json()
    # print(f"Total repositories: {response_dict['total_count']}")
    # print(response_dict.keys())
    # Print information about each repository
    # for i in range(len(response_dict["items"])):
    #     repo_dict = response_dict["items"][i]
    #     print(f"\nName: {repo_dict['name']}")
    #     print(f"Stars: {repo_dict['stargazers_count']}")

    print("=============================")
    print("FastAPI version:", fastapi.__version__)


if __name__ == "__main__":
    main()
