import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        def _wrapper(*args, **kwargs):
            allLaunchTime = 0

            for _ in range(num):
                startTime = time.time()
                func(*args, **kwargs)
                oneLaunchTime = time.time() - startTime
                print(oneLaunchTime)
                allLaunchTime += oneLaunchTime

            print(allLaunchTime / num)
        return _wrapper
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
