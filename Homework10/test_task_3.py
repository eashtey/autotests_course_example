# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('nums, result', [
    pytest.param((1.2, 2), 0.6, marks=pytest.mark.smoke),
    pytest.param((40.56, -2), -20.28, marks=pytest.mark.skip),
    ((-10, -2.7, 20.8), 0.17806267806267803),
    ((0, 2), 0)
])
def test(nums, result):
    assert all_division(*nums) == result
