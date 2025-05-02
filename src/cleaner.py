def remove_columns(df, columns):
    return df.drop(columns=columns)

def drop_na_rows(df):
    return df.dropna()

def fill_na_values(df, value):
    return df.fillna(value)

def convert_columns(df, columns, to_type):
    for col in columns:
        try:
            df[col] = df[col].astype(to_type)
        except Exception:
            pass
    return df
