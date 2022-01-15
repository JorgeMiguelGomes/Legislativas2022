import pandas as pd
import numpy as np

def merge_informations(df_new, df_old):
    """
    Return dataframe with sufix "new/old" with merged info
    
    df_new: table with information of new elections
    df_old: table with information of old elections
    """

    #put 'nome' in first positions
    first_column = df_new.pop('nome')
    df_new.insert(0, 'nome', first_column)
    
    #add sufixe
    new_columns = ["nome"]
    for col in df_new.columns:
        if col != "nome":
            new_columns.append(col+"_new")
    
    df_new.columns = new_columns


    #put 'nome' in first positions
    first_column = df_old.pop('nome')
    df_old.insert(0, 'nome', first_column)

    #add sufixe
    new_columns = ["nome"]
    for col in df_old.columns:
        if col != "nome":
            new_columns.append(col+"_old")
    
    df_old.columns = new_columns

    #join information: last elections with new
    df_all = pd.merge(df_new, df_old, on='nome', how='left')
    
    return df_all
    
def new_columns(df):
    """
    Adding some columns

    """

    #If they participate in the last elections
    mask = df.partido_old.isnull()
    column_name = 'old_elections'
    df.loc[mask, column_name] = False 
    df['old_elections'] = df['old_elections'].fillna(True)
    

    return df

def diff_circle(df):
    """
    Return a df of candidates that change cicle, those who didnt participate will be drop
    """

    df = df.loc[df['old_elections'] == True]
    df = df[df['circulo_new'] != df['circulo_old']]
    
    return df

def diff_partido(df):
    """
    Return a df of candidates that change partido, those who didnt participate will be drop
    """

    df = df.loc[df['old_elections'] == True]
    df = df[df['partido_new'] != df['partido_old']]

    return df

