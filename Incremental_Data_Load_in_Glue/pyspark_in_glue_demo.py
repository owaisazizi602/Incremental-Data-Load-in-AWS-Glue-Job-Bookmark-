import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

subsDf = glueContext.create_dynamic_frame.from_catalog(
    database="telecom_catalog",
    table_name="telecom_data_project"
    )

subsDf.printSchema()
sparkSubsDf = subsDf.toDF()
sparkSubsDf.show()
print(sparkSubsDf.count())