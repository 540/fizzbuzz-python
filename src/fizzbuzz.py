def fizzbuzz(number: int) -> int:
    if _is_multiple_of_5(number) and _is_multiple_of_3(number):
        return "FizzBuzz"
    if _is_multiple_of_3(number):
        return "Fizz"
    if _is_multiple_of_5(number):
        return "Buzz"

    return str(number)


def _is_multiple_of(multiple: int) -> int:
    return lambda number: number % multiple == 0


def _is_multiple_of_3(number: int) -> int:
    return _is_multiple_of(3)(number)


def _is_multiple_of_5(number: int) -> int:
    return _is_multiple_of(5)(number)
