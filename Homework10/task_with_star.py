# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


# Фикстура для вывода на экран значений переданных в маркер id_check
@pytest.fixture
def print_id_checks(request):
    marks = request.node.get_closest_marker("id_check")
    print(marks.args)


@pytest.mark.id_check(1, 2, 3)
def test(print_id_checks):
    assert 1 == 1
