import pandas as pd

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "transaction_id", "date", "product_id", "product_name",
        "quantity", "unit_price", "customer_id", "region"
    ]

    df["unit_price"] = df["unit_price"].str.replace(",", "", regex=False)
    df["quantity"] = df["quantity"].str.replace(",", "", regex=False)

    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    df = df.dropna(subset=["unit_price", "quantity", "customer_id", "region"])
    df = df[(df["unit_price"] > 0) & (df["quantity"] > 0)]

    df["product_name"] = df["product_name"].str.split(",").str[0]
    df["date"] = pd.to_datetime(df["date"])

    df["total_sales"] = df["unit_price"] * df["quantity"]

    return df


def analyze_sales(df: pd.DataFrame) -> dict:
    return {
        "total_revenue": round(df["total_sales"].sum(), 2),
        "top_product": df.groupby("product_name")["total_sales"].sum().idxmax(),
        "top_customer": df.groupby("customer_id")["total_sales"].sum().idxmax(),
        "top_region": df.groupby("region")["total_sales"].sum().idxmax(),
        "average_order_value": round(df["total_sales"].mean(), 2)
    }
