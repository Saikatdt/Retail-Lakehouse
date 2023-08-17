import os
import pandas as pd

base_path='data'
dir_contents=os.scandir(base_path)
for item in dir_contents:
	if item.is_file() and item.name.endswith('.csv'):
		file_name=item.name
		df=pd.read_csv(base_path+'/'+file_name)
		df.to_parquet(base_path+'/'+file_name+'.parquet')
		


