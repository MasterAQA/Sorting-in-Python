import os
import time

from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)

class data:

    count_number = os.getenv("COUNT_NUMBER")


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        elapsed_time = time.perf_counter() - start_time  # Получаем время работы в секундах
        print(f"Время выполнения функции {function.__name__}: {elapsed_time:.2f} секунд")
        return res
    return wrapped