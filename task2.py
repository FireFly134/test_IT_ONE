def main(m: list[set[int]]) -> tuple[int, int, float, tuple[int]]:
	list_num: list = list()
	count_num: int = 0
	sum_val: int = 0
	for set_num in m:
		count_num += len(set_num)
		sum_val += sum(set_num)
		for num in set_num:
			list_num.append(num)
		# или
		# list(map(lambda set_num: list(map(lambda num: list_num.append(num), set_num)), m))
	medium_val: float = sum_val/count_num if count_num != 0 else 0
	tuple_num: tuple = tuple(list_num)
	return count_num, sum_val, medium_val, tuple_num


if __name__ == "__main__":
	count_num, sum_val, medium_val, tuple_num = main(
		m=[{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
	)
	print(f"{count_num=}\n{sum_val=}\n{medium_val=}\n{tuple_num=}")

