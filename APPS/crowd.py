# import libraries
import pandas as pd 
import plotly.express as px 


# Create color dictionary for each entry 

colors={
 		"Partido Social Democrata": "#FF6400",
 		"Ana Mendes Godinho 2022": "#E31F26",
 		"Ana Catarina Mendes": "#E31F26",
 		"PSD - Distrital de Évora":"#FF6400",
 		"Federação do PS Santarém": "#E31F26",
 		"Bloco de Esquerda - Distrito do Porto": "#C90635",
 		"Grupo Parlamentar do Partido Socialista": "#E31F26",
 		"PS do Baixo Alentejo": "#E31F26",
 		"José Pinto Coelho": "#BF311E",
 		"Federação Distrital de Leiria do PS": "#E31F26",
 		"Hugo Carvalho": "#FF6400",
 		"LIVRE": "#00CE8C",
 		"PAN - Pessoas Animais Natureza": "#00798E",
 		"Chega Açores": "#202056",
 		"Bruno Nunes - Chega": "#202056",
 		"Catarina Martins": "#C90635",
 		"Bloco de Esquerda": "#C90635",
 		"Partido Socialista": "#E31F26",
 		"António Costa": "#E31F26",
 		"CHEGA": "#202056"

		}

# Read CSV to Dataframe 

df = pd.read_csv('../PRODUCTS/Legislativas2022_CT_Analysis - PERIOD_08DEZ2021_09DEZ2022.csv')

# Rename columns

df = df.rename(columns={'Post Created': 'PostCreated',"Page Name": 'PageName'})

# Sum Values for each page name

df_sum=df.groupby(by=["PageName"]).sum().reset_index() 

# Create dataframe that sorts current dataframe by likes 

df_likes = df_sum.sort_values('Likes')

# Plot graph by likes 

fig_likes = px.bar(df_likes.tail(20),x="PageName",y="Likes",color='PageName',
			 template='plotly_white',title="#Legislativas2022<br><br><sup>Total de likes em posts que usaram a hashtag #Legislativas2022 no Facebook</sup><br><sup>Período 08 DEZ 2021 a 07 JAN 2022</sup>",
			 color_discrete_map = colors, 
			 labels=dict(PageName="Nome da Página", Likes="Likes Acumulados")
			)

# Define title layou 

fig_likes.update_layout(
    
    title=dict(
        x=0.5,
        y=0.95,
        font=dict(
            family="Arial",
            size=36,
            color='#000000'
        ),
    ),
    )

# Show graph on screen

fig_likes.show()

