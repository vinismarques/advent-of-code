from dotenv import load_dotenv
from utils import get_day_data


def main(data: str) -> None:
    banks = data.splitlines()
    joltages = []
    for bank in banks:
        total_batteries = 12

        batteries = []
        available_bank = bank
        valid_last_pos = -total_batteries + 1
        while len(batteries) < total_batteries:
            seg = available_bank[:valid_last_pos] if valid_last_pos != 0 else available_bank
            battery = max(seg)
            position = available_bank.find(battery)
            available_bank = available_bank[position + 1 :]
            valid_last_pos += 1
            batteries.append(battery)

        battery_joltage = int("".join(batteries))
        joltages.append(battery_joltage)

    print(sum(joltages))


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = """
    # 987654321111111
    # 811111111111119
    # 234234234234278
    # 818181911112111
    #     """.strip()

    main(data)
