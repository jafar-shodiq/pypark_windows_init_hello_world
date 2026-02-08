import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

def create_spark_session():
    """Initializes the Spark Session with Windows-specific fixes."""
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    return SparkSession.builder \
        .appName("BRI_Data_Exploration") \
        .master("local[*]") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.shuffle.partitions", "4") \
        .getOrCreate()

def main():
    spark = create_spark_session()
    
    spark.sparkContext.setLogLevel("ERROR")

    try:
        print("\n--- Starting BRI Data Exploration ---")

        data = [
            ("C001", "Tabungan Utama", 15000000.0, "Jakarta"),
            ("C002", "Simpedes", 500000.0, "Surabaya"),
            ("C003", "BritAma", 2500000.0, "Jakarta"),
            ("C004", "Simpedes", 7500000.0, "Bandung"),
        ]
        columns = ["customer_id", "product_type", "balance", "branch_city"]
        
        df = spark.createDataFrame(data, columns)

        print("\nSummary by Product Type:")
        summary_df = df.groupBy("product_type").agg(
            F.count("customer_id").alias("total_customers"),
            F.sum("balance").alias("total_balance"),
            F.avg("balance").alias("avg_balance")
        )

        summary_df.show()

        print("DataFrame Schema:")
        df.printSchema()

    except Exception as e:
        print(f"Error during execution: {e}")
    finally:
        print("Shutting down Spark Session...")
        spark.stop()

if __name__ == "__main__":
    main()