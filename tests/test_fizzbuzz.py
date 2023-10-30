from hamcrest import assert_that, is_
from src.fizzbuzz import fizzbuzz


def test_returns_1_string_for_1_number():
    assert_that(run_fizzbuzz(1), is_("1"))


def test_returns_2_string_for_2_number():
    assert_that(run_fizzbuzz(2), is_("2"))


def test_returns_Fizz_for_3_number():
    assert_that(run_fizzbuzz(3), is_("Fizz"))


def test_returns_Fizz_for_6_number():
    assert_that(run_fizzbuzz(6), is_("Fizz"))


def test_returns_Buzz_for_5_number():
    assert_that(run_fizzbuzz(5), is_("Buzz"))


def test_returns_Buzz_for_10_number():
    assert_that(run_fizzbuzz(10), is_("Buzz"))


def test_returns_FizzBuzz_for_15_number():
    assert_that(run_fizzbuzz(15), is_("FizzBuzz"))


def test_returns_Fizz_for_number_containing_3():
    assert_that(run_fizzbuzz(13), is_("Fizz"))


def test_returns_Buzz_for_number_containing_5():
    assert_that(run_fizzbuzz(52), is_("Buzz"))


def test_returns_multiple_numbers():
    assert_that(fizzbuzz(53, [1, 2, 3, 4, 5]), is_(["1", "2", "Fizz", "4", "Buzz"]))


def run_fizzbuzz(number: int):
    return fizzbuzz(number, [number])[0]
