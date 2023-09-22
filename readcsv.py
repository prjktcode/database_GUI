import pandas as pd
import sqlite3
import os

def get_csv_filenames(directory):
    csv_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            csv_files.append(filename)
    return csv_files

def process_csv_filename(csv_file):
    processed_file = ""
    name = csv_file.split('.csv')[0]  
    name = name.replace("-", "_") 
    name = name.lower()           
    processed_file = name
    return processed_file

def create_table_and_insert_data(columns, rows, table_name):

    original_col = columns

    conn = sqlite3.connect('database-3nf.db')
    cursor = conn.cursor()

    original_col.insert(0, f'{table_name}_id INTEGER PRIMARY KEY AUTOINCREMENT')

    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}({",".join(original_col)})')

    columns.remove(f'{table_name}_id INTEGER PRIMARY KEY AUTOINCREMENT')
    for row in rows:

      cursor.execute(f'INSERT INTO {table_name}  {tuple(columns)} VALUES {tuple(row)}')

    conn.commit()
    conn.close()

def read_csv(filename):

  df = pd.read_csv(filename)
  df = df.dropna()
  columns = df.columns.tolist()  
  data = df.values.tolist()  
  return columns, data

csv_files = get_csv_filenames("./")

for file in csv_files:
  columns, data = read_csv(file)
  create_table_and_insert_data(columns,data,process_csv_filename(file))