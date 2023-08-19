import os
import pandas as pd
from dotenv import load_dotenv
import boto3
from io import BytesIO
import pyarrow
import pyarrow.parquet
load_dotenv()

def upload_to_aws(resource,data,bucket,s3_file):
	#client.upload_file(data,bucket,s3_file)
	resource.Object(bucket,s3_file).put(Body=data)
	


base_path='data'
s3=boto3.resource('s3',aws_access_key_id=os.getenv("ACCESS_KEY"), aws_secret_access_key=os.getenv("SECRET_KEY"))
bucket_name='masterbucket1234'

dir_contents=os.scandir(base_path)
for item in dir_contents:
	if item.is_file() and item.name.endswith('.csv'):
		file_name=item.name
		s3_file_name=file_name.replace(".csv","")+'.parquet'
		# reading the csv file using pandas
		df=pd.read_csv(base_path+'/'+file_name)
		#converting the csv file to parquet and put in bytesIO buffer. Instead of writing the file to disk we can create a file like buffer in memory using BytesIO
		data=pyarrow.Table.from_pandas(df)
		buffer=BytesIO()
		pyarrow.parquet.write_table(data,buffer)
		#uploading to aws
		upload_to_aws(s3,buffer.getvalue(),bucket_name,s3_file_name)
		print(file_name,"uploaded successfully")

print("all files are uploaded")
		


