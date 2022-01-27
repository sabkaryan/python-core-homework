from datetime import datetime
from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """
    def wrapper(func):
        def inner(url):
            total = None
            for i in range(num):
                start = datetime.now()
                func(url)
                score = datetime.now() - start
                if total is None:
                    total = score
                else:
                    total += score
                print(f'{i + 1}: {score}')
            print(f'avg: {(total / num)}')
        return inner
    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
