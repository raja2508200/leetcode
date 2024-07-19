import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    step1=employee["salary"].drop_duplicates()
    step2=step1.sort_values(ascending=False)
    if len(step2)<=1:
        data=pd.DataFrame([{"SecondHighestSalary":None}])
        return data
    data=pd.DataFrame({"SecondHighestSalary":[step2.iloc[1]]})
    return data