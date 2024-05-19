def main(in_word: str) -> list[str]:
    list_new_word: list = list()
    for word in list_word:
        if word != in_word:
            for i in range(1, len(word) + 1):
                if in_word.endswith(word[:i]):
                    list_new_word.append(in_word + word[i:])
    return list_new_word


if __name__ == "__main__":
    list_word: list = ["ласты", "стык", "стыковка", "баласт", "кабала", "карась"]
    word: str = ""
    print('чтобы завершить работу программы, напишите слово "СТОП"')
    while word.lower() != "стоп":
        if word:
            result = ", ".join(main(in_word=word.lower()))
            if result:
                print(result)
            else:
                print("Не получилось создать новое слово.")
        word = input("Введите слово: ")
