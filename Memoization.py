import datetime

cache = {}


def fib(num):
    if num == 1 or num == 2:
        return 1
    if num > 2:
        return fib(num - 1) + fib(num - 2)


def fib_opt(num):
    if num in cache:
        value = cache[num]
    else:

        if num == 1 or num == 2:
            value = 1
        if num > 2:
            value = fib_opt(num - 1) + fib_opt(num - 2)
        cache[num] = value
    return value


for i in range (1, 1000):
    star_time = datetime.datetime.now()
    print(f"{i} : {fib_opt(i)} : {datetime.datetime.now() - star_time}")
    # end_time = datetime.datetime.now()
    # print(f"time taken:{end_time - star_time}")
    