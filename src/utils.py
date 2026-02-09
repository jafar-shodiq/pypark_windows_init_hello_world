import os
import sys
from pyspark.sql import SparkSession

def create_spark_session(app_name="SparkTestSession", shuffle_partitions=4):
    """Initialize and return a Spark session configured for local testing."""

    os.environ["HADOOP_OPTS"] = "-Djava.library.path="
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    builder = SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.shuffle.partitions", str(shuffle_partitions)) \
        .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem")

    return builder.getOrCreate()