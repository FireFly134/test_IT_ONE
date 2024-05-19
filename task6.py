import json
from datetime import datetime
from typing import Any, Optional

import pandas as pd

from pydantic import BaseModel, ValidationError, field_validator

import requests


class BankDocument(BaseModel):
    key1: int
    key2: datetime
    key3: str

    @field_validator("key2")
    def parse_datetime(cls, v):
        if isinstance(v, str):
            return datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")
        elif isinstance(v, datetime):
            return v
        else:
            raise ValueError("Некорректный тип данных для key2")


def validate_documents(documents_json: Optional[dict[str, Any]]):
    rows = documents_json.get("Rows", [])
    columns = documents_json.get("Columns", [])
    if not rows or not columns:
        print("Ошибка: Отсутствуют Rows или Columns в JSON")
        return False

    try:
        for row in rows:
            # Создаем словарь для каждой строки
            row_dict = dict(zip(columns, row))
            # Пытаемся создать экземпляр модели с каждой строкой
            BankDocument(**row_dict)
        return True
    except ValidationError as e:
        print("Ошибка при валидации JSON:")
        print(e)
        return False


def get_documents() -> Optional[dict[str, Any]] | None:
    start_of_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_day_timestamp = int(start_of_day.timestamp())
    url = f"https://api.gazprombank.ru/very/important/docs?documents_date={start_of_day_timestamp}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка при запросе к API: {response.status_code}")
            return None
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        return None


def add_load_datetime_column(df: pd.DataFrame) -> pd.DataFrame:
    df["load_dt"] = pd.to_datetime("now")
    return df


def rename_columns(df: pd.DataFrame) -> pd.DataFrame:
    column_mapping = {
        "key1": "document_id",
        "key2": "document_dt",
        "key3": "document_name",
    }

    df = df.rename(columns=column_mapping)
    return add_load_datetime_column(df)


def json_to_dataframe(documents_json: Optional[dict[str, Any]]) -> pd.DataFrame:
    columns = documents_json.get("Columns", [])
    rows = documents_json.get("Rows", [])
    df = pd.DataFrame(rows, columns=columns)
    return rename_columns(df)


if __name__ == "__main__":
    documents_json = get_documents()
    # Для тестов т.к. ссылка фейковая
    # with open("./files/api.json", "r", encoding="utf-8") as json_file:
    #     documents_json = json.load(json_file)
    if documents_json:
        print("JSON успешно получен:")
        print(documents_json)
        # Валидация JSON
        is_valid = validate_documents(documents_json)
        if is_valid:
            print("JSON валиден!")
            # Преобразование JSON в DataFrame
            df = json_to_dataframe(documents_json)
            print("DataFrame:")
            print(df)
        else:
            print("JSON невалиден!")
