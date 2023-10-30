from hamcrest import assert_that, has_length, is_
from pytest import fixture
from src.predicate import and_p, is_multiple_of, contains, or_p
from src.fizzbuzz import FizzBuzz


@fixture(name="fizz_buzz")
def fixgure_fizz_buzz() -> FizzBuzz:
    rule_set = [
        [
            and_p(is_multiple_of(3), is_multiple_of(5)),
            lambda number: "FizzBuzz",
        ],
        [
            or_p(is_multiple_of(3), contains(3)),
            lambda number: "Fizz",
        ],
        [
            or_p(is_multiple_of(5), contains(5)),
            lambda number: "Buzz",
        ],
    ]

    return FizzBuzz(rule_set, range(1, 101))


def test_returns_1_string_for_1_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 1), is_("1"))


def test_returns_2_string_for_2_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 2), is_("2"))


def test_returns_Fizz_for_3_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 3), is_("Fizz"))


def test_returns_Fizz_for_6_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 6), is_("Fizz"))


def test_returns_Buzz_for_5_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 5), is_("Buzz"))


def test_returns_Buzz_for_10_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 10), is_("Buzz"))


def test_returns_FizzBuzz_for_15_number(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 15), is_("FizzBuzz"))


def test_returns_Fizz_for_number_containing_3(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 13), is_("Fizz"))


def test_returns_Buzz_for_number_containing_5(fizz_buzz: FizzBuzz):
    assert_that(fizzbuzz_number(fizz_buzz, 52), is_("Buzz"))


def test_returns_multiple_numbers(fizz_buzz: FizzBuzz):
    assert_that(fizz_buzz.run()[:5], is_(["1", "2", "Fizz", "4", "Buzz"]))


def test_returns_100_numbers(fizz_buzz: FizzBuzz):
    assert_that(fizz_buzz.run(), has_length(100))


def fizzbuzz_number(fizz_buzz, number: int):
    return fizz_buzz.run()[number - 1]
