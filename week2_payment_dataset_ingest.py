#!/usr/bin/env python
# coding: utf-8

import argparse
import os
from time import time
import pandas as pd
from sqlalchemy import create_engine


def main(params):
    tablename, csv_name = params.table_name, params.url
    
    engine = create_engine('postgresql://root:root@localhost:5432/olist_data')
    engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    df = next(df_iter)

    df.head(n=0).to_sql(name=tablename, con=engine, if_exists='replace')

    df.to_sql(name=tablename, con=engine, if_exists='append')

    while True:
        try:
            t_start = time()
            df = next(df_iter)
            df.to_sql(name=tablename, con=engine, if_exists='append')
            t_end = time()
            print('inserted chunk, took %.3f second' %(t_end-t_start))
        
        except:
            print('Finished data ingestion into postgres')
            break



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV to Postgres')
    parser.add_argument('--table_name', help='table for postgres')
    parser.add_argument('--url', help='url of csv file')

    args = parser.parse_args()

    main(args)

