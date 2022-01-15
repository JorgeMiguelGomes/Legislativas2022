import data_utils as d_utils
import pandas as pd

if __name__ == "__main__":

    df_old = pd.read_csv("../Data/Legislativas2019_Portugal_Candidatos_Final.csv") 
    df_new = pd.read_csv("../Data/Legislativas2022_Portugal_Candidatos_Final.csv")
    
    df = d_utils.merge_informations(df_new, df_old)

    df = d_utils.new_columns(df)

    df_diff_circle = d_utils.diff_circle(df)
    df_diff_partido = d_utils.diff_partido(df)
