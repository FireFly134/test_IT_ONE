import os
import logging
from datetime import datetime, timedelta


def delete_old_files(folder_path: str, days: int) -> None:

    now = datetime.now()
    cutoff = now - timedelta(days=days)

    # Перебираем все файлы в папке
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Проверяем, является ли это файлом
        if os.path.isfile(file_path):
            # Получаем время последнего изменения файла
            file_modified_time = os.path.getmtime(file_path)
            # Если файл старше N дней, удаляем его
            if file_modified_time < cutoff.timestamp():
                logging.info(f"Удаляю файл: {file_path}")
                os.remove(file_path)


if __name__ == "__main__":
    folder_path: str = str(input("Укажите путь к директории "))
    if os.path.isdir(folder_path):
        if input("Укажите количество дней ").isnumeric():
            days: int = int()
            delete_old_files(folder_path, days)
        else:
            logging.error("Введено не верное количество дней.")
    else:
        logging.error("Введен не верный путь в директории.")
