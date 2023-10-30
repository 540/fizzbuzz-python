from typing import Tuple
from src.predicate import is_multiple_of, and_p, or_p, contains
from collections.abc import Callable


def fizzbuzz(numbers: list[int] = []) -> int:
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

    return [singleFizzbuzz(rule_set, n) for n in numbers]


def singleFizzbuzz(
    rule_set: list[Tuple[Callable[[int], bool], Callable[[int], str]]], number: int
) -> str:
    apply_rule = next(
        (predicate[1] for predicate in rule_set if predicate[0](number)),
        str,
    )

    return apply_rule(number)
