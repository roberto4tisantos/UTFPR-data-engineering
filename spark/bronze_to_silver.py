
#SPARK
from pyspark.sql import SparkSession

def run():
    spark = SparkSession.builder.appName("bronze_to_silver").master("spark://spark-master:7077") \
        .config("spark.jars.packages", ",".join([
            "io.delta:delta-core_2.12:2.4.0",
            "org.apache.hadoop:hadoop-aws:3.3.4",
            "com.amazonaws:aws-java-sdk-bundle:1.12.262"
            ])) \
        .config('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
        .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
        .config("spark.hadoop.fs.s3a.access.key", "minio") \
        .config("spark.hadoop.fs.s3a.secret.key", "minio123") \
        .config("spark.hadoop.fs.s3a.path.style.access", "true") \
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
        .getOrCreate()

    bronze_path = "s3a://bronze/sample_data.csv"
    silver_path = "s3a://silver/warehouse/default/sample_data"

    df = spark.read.option("header", True).csv(bronze_path)
    df.write.format("delta").mode("overwrite").save(silver_path)

    spark.stop()

