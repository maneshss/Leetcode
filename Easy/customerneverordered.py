import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # keep customers whose id is NOT in orders.customerId
    df = customers[~customers["id"].isin(orders["customerId"])]
    # LeetCode wants only the name column
    df = df.rename(columns={"name": "Customers"})
    return df[["Customers"]]
