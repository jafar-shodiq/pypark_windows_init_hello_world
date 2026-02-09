import pytest
from src.utils import create_spark_session

@pytest.fixture(scope="session")
def spark():
    """Fixture to create a Spark session for the test session."""
    session = create_spark_session(app_name="TestSparkSession", shuffle_partitions=4)
    session.sparkContext.setLogLevel("ERROR")
    yield session
    session.stop()

def test_data_aggregation(spark):
    """Test if the balance aggregation logic is correct."""
    # Arrange
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

    # Act
    result = df.groupBy("name").sum("trx_amount").collect()

    # Assert
    assert result[0]["sum(trx_amount)"] == 19100.0