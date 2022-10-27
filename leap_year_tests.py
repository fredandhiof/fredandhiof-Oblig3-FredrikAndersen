from leap_year_calculator import is_leap_year


def test_year_divisible_by_4000_is_not_leap_year():
    assert not is_leap_year(4000)
    assert not is_leap_year(8000)


def test_year_divisible_by_400_is_leap_year():
    assert is_leap_year(400)
    assert is_leap_year(1600)


def test_year_divisible_by_100_is_not_leap_year():
    assert not is_leap_year(100)
    assert not is_leap_year(900)


def test_year_divisible_by_4_is_leap_year():
    assert is_leap_year(4)
    assert is_leap_year(2016)


def test_year_divisible_by_3_is_not_leap_year():
    assert not is_leap_year(2)
    assert not is_leap_year(18)
