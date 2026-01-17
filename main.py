import os
from utils.file_handler import read_sales_file, save_report
from utils.data_processor import clean_sales_data, analyze_sales

BASE_DIR = r"C:\Users\nares\OneDrive\Desktop\BITSOM\Python_Class_BitSOM\New folder"

DATA_PATH = os.path.join(BASE_DIR, "data", "sales_data.txt")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "report.txt")

def main():
    df = read_sales_file(DATA_PATH)
    df = clean_sales_data(df)
    insights = analyze_sales(df)

    report = f"""
SALES ANALYTICS REPORT
=====================

Total Revenue: ₹{insights['total_revenue']:,}
Top Product: {insights['top_product']}
Top Customer ID: {insights['top_customer']}
Top Performing Region: {insights['top_region']}
Average Order Value: ₹{insights['average_order_value']:,}
"""

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    save_report(report, OUTPUT_PATH)

    print("✅ Sales report generated successfully.")
    print(f"📄 Report saved at: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
