from dotenv import load_dotenv
from utils import get_day_data


def find_max_joltage(bank: str, num_batteries: int) -> int:
    batteries = []
    start = 0

    for remaining in range(num_batteries, 0, -1):
        end = len(bank) - remaining + 1

        window = bank[start:end]
        best_digit = max(window)
        best_pos = start + window.index(best_digit)

        batteries.append(best_digit)
        start = best_pos + 1

    return int("".join(batteries))


def main(data: str) -> None:
    banks = data.splitlines()
    joltages = []

    total_batteries = 12
    for bank in banks:
        joltages.append(find_max_joltage(bank, total_batteries))

    print(sum(joltages))


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    # data = """
    # 987654321111111
    # 811111111111119
    # 234234234234278
    # 818181911112111
    #     """.strip()

    main(data)
