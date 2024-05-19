import pandas as pd


def main() -> None:
    df_db: pd.DataFrame = pd.read_csv("./files/db.csv", sep="|")
    df_file: pd.DataFrame = pd.read_csv("./files/f.csv", sep="|")
    new_rows: list = list()
    index: int = max(df_db["id"].to_list())+1
    for idx, row in df_file.iterrows():
        df = df_db[
            (df_db["lastname"] == row["lastname"]) &
            (df_db["name"] == row["name"]) &
            (df_db["patronymic"] == row["patronymic"]) &
            (df_db["date_of_birth"] == str(
                row["date_of_birth"]).strip())
        ]
        if df.empty:
            new_row = row.copy()
            new_row["id"] = index
            index += 1
            new_rows.append(new_row)
    df_new = pd.DataFrame(new_rows,
                          columns=["id", "lastname", "name", "patronymic",
                                   "date_of_birth"])
    new_db = pd.concat([df_db, df_new], ignore_index=True)
    df_new.to_csv("./files/df_new.csv", index=None, sep="|")
    new_db.to_csv("./files/new_db.csv", index=None, sep="|")


if __name__ == "__main__":
    main()
