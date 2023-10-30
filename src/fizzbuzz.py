from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class FizzBuzz:
    rule_set: list[tuple[Callable[[int], bool], Callable[[int], str]]]
    numbers: list[int]

    def run(self):
        return [self._run_single(number) for number in self.numbers]

    def _run_single(self, number: int):
        apply_rule = next(
            (predicate[1] for predicate in self.rule_set if predicate[0](number)),
            str,
        )

        return apply_rule(number)
