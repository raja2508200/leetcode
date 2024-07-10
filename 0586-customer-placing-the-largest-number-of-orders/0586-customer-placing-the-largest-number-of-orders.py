import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df=orders.groupby("customer_number")["order_number"].count().reset_index()
    filter1=df[df['order_number'] == df['order_number'].max()]
    return filter1[["customer_number"]]
    