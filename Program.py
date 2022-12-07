import pandas as pd
from pathlib import *

def transform_MD(MD):
    MD = '-'+MD
    return MD

df = pd.read_table('TRJ/22ПЛ.txt', sep='/s*', engine='python', encoding='cp1251')
name = df['#  X  Y  TVDSS  MD'][0]
df.drop(labels = [0],axis = 0, inplace=True)
df = df['#  X  Y  TVDSS  MD'].str.split(expand=True)
df.columns=['X', 'Y', 'TVDSS', 'MD']
df['MD'] = df['MD'].apply(transform_MD)

with open('TRJ/22ПЛ.txt', 'w') as file:
    file.write(f'#  X  Y  TVDSS  MD \n {name} \n')

with open('TRJ/22ПЛ.txt', 'a') as file:
    file.write(df.to_string(index=False, header=None, col_space=12))



print(df.info())
print(df)
print(name)
