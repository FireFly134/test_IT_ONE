# a = [[1,2,3], [4,5,6]]
# сделать список словарей
# b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
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
