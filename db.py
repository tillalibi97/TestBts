import pandas as pd
import sqlite3
import os

path = os.getcwd()
files = os.listdir(path + '/files')

df = pd.DataFrame()

db = sqlite3.connect('superstore.db')
c = db.cursor()
c.execute(
    """
    CREATE TABLE companies (
        Bin TEXT,
        Nazvanie TEXT,
        NomerReg TEXT,
        Adres TEXT,
        Sud TEXT,
        DataVyneseniya TEXT,
        DataNaznacheniya TEXT,
        FIOvrem TEXT,
        SrokS TEXT,
        SrokDo TEXT,
        AddressPriema TEXT     
        );
     """
)

for f in files:
    ind = files.index(f)
    if ind in [2, 3, 4]:
        a = 3
    else:
        a = 4
    companies = pd.read_excel(
        f'files/{f}',
        header=a,
        usecols='B:L')
    companies.rename(columns={2: 'Bin',
                              3: 'Nazvanie',
                              4: 'NomerReg',
                              5: 'Adres',
                              6: 'Sud',
                              7: 'DataVyneseniya',
                              8: 'DataNaznacheniya',
                              9: 'FIOvrem',
                              10: 'SrokS',
                              11: 'SrokDo',
                              12: 'AddressPriema'}, inplace=True)
    df = df.append(companies)

df.to_sql('companies', db, if_exists='append', index=False)

db.close()
