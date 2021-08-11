from libs.helpy import *
from libs.twitter_connection import *

# init date
last = pd.to_datetime('2021.07.23 15:08:20')

URL = 'http://www.koeri.boun.edu.tr/scripts/lst9.asp'

while True:
    df = checkWebsite(last)
    if df.shape[0] > 0:
        for i in range(df.shape[0]):
            if (int(df.loc[i, 'ML']) > 4.5):
                print('tweet atildi!!')
                print(df.loc[i,'Tarih'])
                api.update_status("Tarih: {} \n Yer: {} \n Niteligi: {} \n Siddeti: {}"
                    .format(df.loc[i, 'Tarih'], df.loc[i, 'Yer'], df.loc[i, 'Çözüm Niteliği\r'], df.loc[i, 'ML']))
            time.sleep(3)
        last = df['Tarih'].max()
    
    print(f'There is no eartquake now: {datetime.datetime.now()}')
    time.sleep(60)