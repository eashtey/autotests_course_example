# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time


def plus(a, b):
    time.sleep(1)
    return a + b


# Класс с фикстурой start_end_time(описана в файле conftest.py)
@pytest.mark.usefixtures("start_end_time")
class Test:

    # Тест с фикстурой delta_time(описана в файле conftest.py)
    def test_1(self, delta_time):
        assert plus(1, 2) == 3

    # Тест без фикстуры
    def test_2(self):
        assert plus(-5, 7) == 2

    # Тест с фикстурой delta_time(описана в файле conftest.py)
    def test_3(self, delta_time):
        assert plus(0, 0) == 0
