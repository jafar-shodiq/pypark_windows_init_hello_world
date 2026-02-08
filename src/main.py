import os
import sys
from pyspark.sql import SparkSession

def main():
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    spark = SparkSession.builder \
        .appName("TestApp") \
        .master("local[*]") \
        .config("spark.driver.host", "127.0.0.1") \
        .getOrCreate()

    data = [("Testing", 1), ("Spark", 2)]
    df = spark.createDataFrame(data, ["Name", "Value"])
    df.show()

    spark.stop()

if __name__ == "__main__":
    main()