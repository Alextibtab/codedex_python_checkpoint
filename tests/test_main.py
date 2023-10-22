from terminal_rpg.__main__ import sum


def test_sum():
    assert sum(1, 2) == 3
    assert sum(2, 2) == 4
    assert sum(3, 2) == 5
