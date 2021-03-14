import pandas as pd
import numpy as np

def load_process(path):
    data = (pd.read_csv(path)
           .replace(r'^\s*$', np.nan, regex=True)
           .dropna()
           .reset_index()
           .drop(['index'], axis=1)
           .rename(columns={"Specific Bean Origin\nor Bar Name": "Specific Bean Origin or Bar Name",
                      "Review\nDate": "Review Date",
                      "Cocoa\nPercent": "Cocoa Percent",
                      "Company\nLocation": "Company Location",
                      "Bean\nType": "Bean Type",
                      "Broad Bean\nOrigin": "Broad Bean Origin"}) 
           )
    data.rename(columns={ data.columns[0]: "Company (Maker-if known)" }, inplace = True)
    data['Cocoa Percent'] = data['Cocoa Percent'].str.rstrip('%').astype('float') / 100.0
    data.to_csv('../data/processed/data.csv')
    return data

def make_table(df,subject):
    table = (df
             .groupby(subject)['Rating']
             .mean()
             .sort_values(ascending=False)
             .reset_index())
    return table
