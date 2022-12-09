import pandas as pd
import pathlib as pl
import easygui as eg

def transform_MD(MD):
    MD = '-'+MD
    return MD
def transform_file():
    df = pd.read_table(f'{fieldValues[i]}', sep='/s*', engine='python', encoding='cp1251')
    name = df['#  X  Y  TVDSS  MD'][0]
    df.drop(labels = [0],axis = 0, inplace=True)
    df = df['#  X  Y  TVDSS  MD'].str.split(expand=True)
    df.columns=['X', 'Y', 'TVDSS', 'MD']
    df['MD'] = df['MD'].apply(transform_MD)
    with open(f'{fieldValues[i]}', 'w') as file:
        file.write(f'#  X  Y  TVDSS  MD \n {name} \n')
        file.write(df.to_string(index=False, header=None, col_space=12))

msg = "Уважаемый пользователь! \n \n \
    Данная программа редактирует .txt файлы, \n \
    добавляя впереди чисел столбца 'MD' знак '-'. \n \n \
    Выберите файлы для редактирования."
title = "Выбор файлов для редактирования"
txt_files = list(pl.Path.cwd().glob('*.txt'))
fieldValues = eg.multchoicebox(msg,title, txt_files)

for i in range(len(txt_files)):
    transform_file()
