import pytest
from src.main import create_spark_session
from pyspark.sql import Row

@pytest.fixture(scope="session")
def spark():
    """Fixture to create a Spark session for the test session."""
    session = create_spark_session()
    session.sparkContext.setLogLevel("ERROR")
    yield session
    session.stop()

def test_data_aggregation(spark):
    """Test if the balance aggregation logic is correct."""
    # Arrange
    data = [
        Row(customer_id="C001", product_type="Simpedes", balance=1000.0),
        Row(customer_id="C002", product_type="Simpedes", balance=2000.0),
    ]
    df = spark.createDataFrame(data)

    # Act
    result = df.groupBy("product_type").sum("balance").collect()

    # Assert
    assert result[0]["sum(balance)"] == 3000.0