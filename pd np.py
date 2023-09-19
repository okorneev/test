# import pandas as pd
# df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
# df = df.sort_index()
# print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex:

import pandas as pd

class Data:
    uk, uk_scrbd, ru = range(3)

def load_data(identity):
    '''имплементация мультиметода на Python; загружает данные в зависимости от значения идентификатора'''
    return {
        Data.uk: lambda: do('ch01/UK2010.xls',
                            pd.read_excel,
                            lambda o: o[o['Electron Year'].notnull()]
                            )
    }[identity]()

load_data(Data.uk)
