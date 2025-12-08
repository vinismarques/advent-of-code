from functools import reduce
from operator import add, mul, sub
from typing import Any, Callable

from dotenv import load_dotenv
from utils import get_day_data


def get_operation(op: str) -> Callable[[Any, Any], Any]:
    match op:
        case "*":
            return mul
        case "+":
            return add
        case "-":
            return sub
        case _:
            raise ValueError(f"Operator '{op}' is not supported.")


def main(data: str) -> None:
    lines = data.splitlines()
    transposed = ["".join(char) for char in zip(*lines)]

    grand_total = 0
    current_numbers = []
    current_op = None

    for col in reversed(transposed):
        problem_value = col[:-1].strip()
        operator_char = col[-1].strip()

        if not problem_value:
            continue

        if operator_char == "":
            current_numbers.append(int(problem_value))
        else:
            current_numbers.append(int(problem_value))
            current_op = get_operation(operator_char)
            grand_total += reduce(current_op, current_numbers)
            current_numbers = []

    answer = grand_total
    print("Answer: ", answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""123 328  51 64
    #  45 64  387 23
    #   6 98  215 314
    # *   +   *   +  """  # Sample

    main(data)
