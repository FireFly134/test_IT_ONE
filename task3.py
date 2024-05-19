def main(a: list[list[int]]) -> list[dict[str, int]]:
    b = list()
    for num_list in a:
        dict_num = dict()
        for i, num in enumerate(num_list):
            dict_num[f"k{i}"] = num
        else:
            b.append(dict_num)
    return b


if __name__ == "__main__":
    print(main(a=[[1, 2, 3], [4, 5, 6]]))
