from collections.abc import Callable


def is_multiple_of(multiple: int) -> Callable[[int], bool]:
    return lambda number: number % multiple == 0


def contains(contained_number: int) -> Callable[[int], bool]:
    return lambda number: str(contained_number) in str(number)


def and_p(*predicates: list[Callable[[bool], bool]]) -> bool:
    return lambda number: all(predicate(number) is True for predicate in predicates)


def or_p(*predicates: list[Callable[[bool], bool]]) -> bool:
    return lambda number: any(predicate(number) is True for predicate in predicates)
