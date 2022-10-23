import time


def measure_velocity(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        y = func(*args, **kwargs)

        end = time.perf_counter()

        print(f'Time used: {end - start}')

        return y / (end - start)

    return wrapper


# @measure_velocity
# def foo():
#     time.sleep(3)
#     return 5


# x = foo()

# print(x)
