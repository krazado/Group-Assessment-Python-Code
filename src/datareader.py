import pandas as pd

#read data file
def read_data():
    excel_file_path = 'data/companions_data.xlsx'
    df = pd.read_excel(excel_file_path)
    df_skipped = df.drop(columns=['PUB'])
    return df_skipped