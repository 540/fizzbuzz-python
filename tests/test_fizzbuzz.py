from hamcrest import assert_that, has_length, is_
from src.fizzbuzz import fizzbuzz


def test_returns_1_string_for_1_number():
    assert_that(fizzbuzz_number(1), is_("1"))


def test_returns_2_string_for_2_number():
    assert_that(fizzbuzz_number(2), is_("2"))


def test_returns_Fizz_for_3_number():
    assert_that(fizzbuzz_number(3), is_("Fizz"))


def test_returns_Fizz_for_6_number():
    assert_that(fizzbuzz_number(6), is_("Fizz"))


def test_returns_Buzz_for_5_number():
    assert_that(fizzbuzz_number(5), is_("Buzz"))


def test_returns_Buzz_for_10_number():
    assert_that(fizzbuzz_number(10), is_("Buzz"))


def test_returns_FizzBuzz_for_15_number():
    assert_that(fizzbuzz_number(15), is_("FizzBuzz"))


def test_returns_Fizz_for_number_containing_3():
    assert_that(fizzbuzz_number(13), is_("Fizz"))


def test_returns_Buzz_for_number_containing_5():
    assert_that(fizzbuzz_number(52), is_("Buzz"))


def test_returns_multiple_numbers():
    assert_that(fizzbuzz()[:5], is_(["1", "2", "Fizz", "4", "Buzz"]))


def test_returns_100_numbers():
    assert_that(fizzbuzz(), has_length(100))


def fizzbuzz_number(number: int):
    return fizzbuzz()[number - 1]
