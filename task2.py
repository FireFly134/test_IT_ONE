def main(m: list[set[int]]) -> tuple[int, int, float, tuple[int]]:
    list_num: list = [num for set_num in m for num in set_num]
    count_num: int = len(list_num)
    sum_val: int = sum(list_num)
    medium_val: float = sum_val / count_num if count_num != 0 else 0
    tuple_num: tuple = tuple(list_num)
    return count_num, sum_val, medium_val, tuple_num


def main_one_line(m: list[set[int]]) -> tuple[int, int, float, tuple[int]]:
    return sum(map(len, m)), sum(map(sum, m)), sum(num for set_num in m for num in set_num) / sum(map(len, m)) if m else 0, tuple(num for set_num in m for num in set_num)


if __name__ == "__main__":
    m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

    count_num, sum_val, medium_val, tuple_num = main(m)

    print(f"{count_num=}\n{sum_val=}\n{medium_val=}\n{tuple_num=}")
    print()
    count_num2, sum_val2, medium_val2, tuple_num2 = main_one_line(m)
    print(f"{count_num2=}\n{sum_val2=}\n{medium_val2=}\n{tuple_num2=}")
