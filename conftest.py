import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        elapsed_time = time.perf_counter() - start_time  # Получаем время работы в секундах
        print(f"Время выполнения функции {function.__name__}: {elapsed_time:.2f} секунд")
        return res
    return wrapped