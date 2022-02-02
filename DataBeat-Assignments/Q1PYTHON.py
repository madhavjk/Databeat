import pandas as pd

movies_url='https://drive.google.com/file/d/113VxddyUdXBIfngF22AR_8PCYYG2hGUk/view'
movies_path='https://drive.google.com/uc?id=' + movies_url.split('/')[-2]

activity_url='https://drive.google.com/file/d/1kQYohgOOA9wvrXsp2gAlgtv-7HvxsZV9/view'
activity_path='https://drive.google.com/uc?id=' + activity_url.split('/')[-2]



movies = pd.read_csv(movies_path)
activity = pd.read_csv(activity_path)

df = movies['_source']

df.to_csv('result.csv')
