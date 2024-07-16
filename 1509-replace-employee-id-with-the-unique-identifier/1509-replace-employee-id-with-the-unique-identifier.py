import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(employee_uni, on='id', how='left')
    return merged[["unique_id","name"]]
    