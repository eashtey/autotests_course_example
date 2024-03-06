import pytest
import time
import datetime


# Фикстура для класса. Печать времени начала выполнения класса с тестами и окончания.
@pytest.fixture(scope="class")
def start_end_time():
    start_time = datetime.datetime.now()
    print(f"Начало выполнения класса {start_time}")
    yield start_time
    end_time = datetime.datetime.now()
    print(f"Окончание выполнения класса {end_time} сек")


# Фикстура для конкретных тестов. Время выполнения теста.
@pytest.fixture()
def delta_time():
    start_time = time.time()
    yield start_time
    end_time = time.time()
    delta_time = end_time - start_time
    print(f"Время выполнения теста {delta_time} сек")
