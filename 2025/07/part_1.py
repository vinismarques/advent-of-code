from dotenv import load_dotenv
from utils import get_day_data


def main(data: str) -> None:
    grid = [list(line) for line in data.splitlines()]

    total_splits = 0
    for row, row_value in enumerate(grid):
        for col, col_value in enumerate(row_value):
            if col_value in ("S", "|"):
                if row + 1 >= len(grid):
                    break

                next_value = grid[row + 1][col]

                if next_value == "^":
                    grid[row + 1][col - 1] = "|"
                    grid[row + 1][col + 1] = "|"
                    total_splits += 1

                elif next_value == ".":
                    grid[row + 1][col] = "|"

        print("".join(row_value))

    answer = total_splits
    print(answer)


if __name__ == "__main__":
    load_dotenv()

    data = get_day_data()
    #     data = r"""
    # .......S.......
    # ...............
    # .......^.......
    # ...............
    # ......^.^......
    # ...............
    # .....^.^.^.....
    # ...............
    # ....^.^...^....
    # ...............
    # ...^.^...^.^...
    # ...............
    # ..^...^.....^..
    # ...............
    # .^.^.^.^.^...^.
    # ...............
    # """.strip()  # Sample

    main(data)
