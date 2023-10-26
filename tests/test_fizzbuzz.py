from hamcrest import assert_that, is_
from src.fizzbuzz import fizzbuzz


def test_fizzbuzz_example():
    assert_that(fizzbuzz(), is_(None))
