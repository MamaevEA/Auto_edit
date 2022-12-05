import pandas as pd

def transform_MD(MD):
    MD = '-'+MD
    return MD

df = pd.read_csv('TRJ/22ПЛ.txt', encoding='ISO-8859-1')
name = df['#  X  Y  TVDSS  MD'][0]
name = name.split()
name = {'X': name[0], 'Y': name[1], 'TVDSS': '', 'MD': ''}
name = pd.DataFrame([name])
df.drop(labels = [0],axis = 0, inplace=True)
df = df['#  X  Y  TVDSS  MD'].str.split(expand=True)
df.columns=['X', 'Y', 'TVDSS', 'MD']
df['MD'] = df['MD'].apply(transform_MD)
df = pd.DataFrame(df)
res = pd.concat([name, df], ignore_index=True)


with open('TRJ/22ПЛ.txt', 'w') as file:
    file.write(res.to_string(index=False))


print(df.info())
print(df)
print(name)
print(res)
