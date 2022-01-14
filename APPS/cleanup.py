# Credits: Luis Silva @ Política Para Todos 

# .csv on repository already cleaned and prepared 

# import libraries

import pandas as pd 

# Import CCSV files 

df_2022 = pd.read_csv("../DATA/Legislativas2022_Portugal_Candidatos_Final.csv")

df_2019 = pd.read_csv("../DATA/Legislativas2019_Portugal_Candidatos_Final.csv")

# df_2019_2022 data cleanup 

df_2022["partido"] = df_2022["partido"].str.strip()
df_2022["circulo"] = df_2022["circulo"].str.strip()
df_2022["tipo"] = df_2022["tipo"].str.replace("efectivo", "efetivo")
df_2022["partido"] = df_2022["partido"].str.replace("Aliança", "ALIANÇA")
df_2022["partido"] = df_2022["partido"].str.replace("PCPT/MRPP", "PCTP/MRPP")
df_2022["partido"] = df_2022["partido"].str.replace("R.I.R.", "R.I.R")
df_2022["partido"] = df_2022["partido"].str.replace("R.I.R", "R.I.R.")

# df_2019_2019 data cleanup 

df_2019["partido"] = df_2019["partido"].str.strip()
df_2019["circulo"] = df_2019["circulo"].str.strip()
df_2019["tipo"] = df_2019["tipo"].str.replace("efectivo", "efetivo")
df_2019["partido"] = df_2019["partido"].str.replace("Aliança", "ALIANÇA")
df_2019["partido"] = df_2019["partido"].str.replace("PCPT/MRPP", "PCTP/MRPP")
df_2019["partido"] = df_2019["partido"].str.replace("R.I.R.", "R.I.R")
df_2019["partido"] = df_2019["partido"].str.replace("R.I.R", "R.I.R.")


# save csv files 

df_2022.to_csv("../DATA/Legislativas2022_Portugal_Candidatos_Final.csv", index = False)
df_2019.to_csv("../DATA/Legislativas2019_Portugal_Candidatos_Final.csv", index = False)