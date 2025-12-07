import bisect

from dotenv import load_dotenv
from loguru import logger
from utils import get_day_data, merge_ranges


def main(data: str) -> None:
    fresh_input, ingredients_input = data.split("\n\n")
    fresh_ranges = []
    for fresh_range in fresh_input.splitlines():
        start, end = map(int, fresh_range.split("-"))
        fresh_ranges.append((start, end))
    merged_ranges = merge_ranges(fresh_ranges)
    ingredients = {int(i) for i in ingredients_input.splitlines()}

    # Precompute starts for binary search
    starts = [r[0] for r in merged_ranges]

    total_fresh = 0
    for i in ingredients:
        idx = bisect.bisect_right(starts, i) - 1
        if idx < 0:
            logger.debug(f"Value '{i}' not found")

        if merged_ranges[idx][0] <= i <= merged_ranges[idx][1]:
            total_fresh += 1

    answer = total_fresh
    print(answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""
    # 3-5
    # 10-14
    # 16-20
    # 12-18

    # 1
    # 5
    # 8
    # 11
    # 17
    # 32
    # """.strip()  # Sample

    main(data)
