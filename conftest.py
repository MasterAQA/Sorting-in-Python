import datetime
import time
import timeit

import pytest

@pytest.fixture(scope='function', autouse=True)
def measure_time(request):
    start_time = 0

    def start_timer():
        nonlocal start_time
        start_time = timeit.default_timer()

    def stop_timer():
        elapsed_time = timeit.default_timer() - start_time
        print(f"Время выполнения метода {request.node.name}: {elapsed_time:.5f} секунд")

    request.addfinalizer(stop_timer)
    return start_timer


# def time_of_function(function):
#     def wrapped(*args):
#         start_time = time.perf_counter_ns()
#         res = function(*args)
#         # print(time.perf_counter_ns() - start_time)
#         print(f"Время выполнения: {(time.perf_counter_ns() - start_time)*0.000001:.5f} секунд")
#         return res
#
#     return wrapped

def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        elapsed_time = time.perf_counter() - start_time  # Получаем время работы в секундах
        print(f"Время выполнения функции {function.__name__}: {elapsed_time:.2f} секунд")
        return res
    return wrapped