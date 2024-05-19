def main(a: list[list[int]]) -> list[dict[str, int]]:
    b: list = list()
    for num_list in a:
        dict_num: dict = dict()
        for i, num in enumerate(num_list):
            dict_num[f"k{i}"]: int = num
        else:
            b.append(dict_num)
    return b


def main_one_line(a: list[list[int]]) -> list[dict[str, int]]:
    return [{f"k{i}": num for i, num in enumerate(num_list)} for num_list in a]


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print(main(a))
    print(main_one_line(a))
