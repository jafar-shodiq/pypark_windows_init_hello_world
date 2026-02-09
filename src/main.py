import sys
import time
from pyspark.sql import functions as F

from src.utils import create_spark_session

def main():
    """Main function to demonstrate Spark session and aggregation."""
    spark = create_spark_session(app_name="SparkTestSession", shuffle_partitions=4)
    
    spark.sparkContext.setLogLevel("ERROR")
    spark.sparkContext.setLogLevel("OFF")

    try:
        data = [
            (1, "Alice", 10000),
            (2, "Bob", 3100), 
            (3, "David", 2500),
            (4, "David", 3500),
            (5, "Eve", 2800),
            (6, "Alice", 3300),
            (7, "Grace", 2700),
            (8, "Bob", 2900),
            (9, "Eve", 4100),
            (10, "Frank", 2300),
            (11, "Grace", 3600),
            (12, "Heidi", 3900),
            (13, "Alice", 5800)
        ]
        columns = ["id", "name", "trx_amount"]

        df = spark.createDataFrame(data, columns)
        
        print("Started creating dataframe")
        df.show()
        print("Finished creating dataframe")

        print("Started performing aggregation")
        agg_df_1 = df.groupBy("name").agg(
            F.count("trx_amount").alias("transaction_count"),
            F.sum("trx_amount").alias("total_amount"),
            F.avg("trx_amount").alias("average_amount")
        )
        agg_df_1.show()
        print("Finished performing aggregation")

        print("Started exporting results to CSV")
        agg_df_1.coalesce(1).write.mode("overwrite").option("header", "true").csv("data/agg_results")
        print("Finished exporting results to CSV")
    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        spark.stop()
        time.sleep(1)

if __name__ == "__main__":
    main()
    sys.exit(0)