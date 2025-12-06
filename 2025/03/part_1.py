from dotenv import load_dotenv
from utils import get_day_data


def main() -> None:
    data = get_day_data()
    #     data = """
    # 987654321111111
    # 811111111111119
    # 234234234234278
    # 818181911112111
    # """.strip()

    banks = data.splitlines()
    joltages = []
    for bank in banks:
        first_battery = max(bank[:-1])
        first_position = bank.find(first_battery)
        second_battery = max(bank[first_position + 1 :])
        battery_joltage = int(f"{first_battery}{second_battery}")
        joltages.append(battery_joltage)

    print(sum(joltages))


if __name__ == "__main__":
    load_dotenv()
    main()
