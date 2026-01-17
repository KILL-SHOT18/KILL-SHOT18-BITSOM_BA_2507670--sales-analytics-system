import pandas as pd

def read_sales_file(file_path: str) -> pd.DataFrame:
    """
    Reads pipe-delimited messy sales data.
    """
    df = pd.read_csv(
        file_path,
        delimiter="|",
        dtype=str
    )
    return df


def save_report(report: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
