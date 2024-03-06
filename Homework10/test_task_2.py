# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke
def test_1():
    assert all_division(1.2, 2) == 0.6


def test_2():
    assert all_division(40.56, -2) == -20.28


@pytest.mark.smoke
def test_3():
    assert all_division(-10, -2.7, 20.8) == 0.17806267806267803


def test_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)


def test_zero_dividend():
    assert all_division(0, 2) == 0

# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного

# 1) pytest -v
# 2) pytest -m smoke -v
# 3) pytest -k "test_zero" -v
