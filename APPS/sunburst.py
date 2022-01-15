
# import libraries
import pandas as pd
import plotly.express as px 

# import csv 

df = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/Legislativas2022/main/DATA/Legislativas2022_Portugal_Candidatos_Final.csv')

# plot sunburst 

fig = px.sunburst(df, path=['circulo', 'partido','tipo','nome'],color='partido',
		hover_name="circulo",
		branchvalues="remainder",
		# Colors were picked at each parties website 
		color_discrete_map={
                "PCTP/MRPP": "#E00E02",
				"PPD/PSD": "#FF6400",
				"CDS/PP":"#0B6AB1",
				"Ergue-te": "#BF311E",
				"MAS": "#2B2C2C",
				"PS": "#F1A0A2",
				"LIVRE": "#00CE8C",
				"ADN": "#204E84",
				"BE": "#C90635",
				"PCP - PEV - CDU": "#F8D704",
				"R.I.R.": "#00939D",
				"Volt Portugal": "#502376",
				"CHEGA": "#202056",
				"JPP": "#03AB83",
				"IL": "#00AEEF",
				"PAN": "#00798E",
				"MPT": "#66BB69",
				"PTP": "#00659B",
				"Nós, Cidadãos!": "#00659B",
				"ALIANÇA": "#0451CB",
				"PPD/PSD-CDS-PP - MADEIRA PRIMEIRO": "#F36D24",
				"PPM" : "#19476C",
 				"PPD/PSD - CDS-PP - PPM – AD/Aliança Democrática": "#0031A"
							},
		 hover_data={'partido':False,
                      'circulo':False,
                      'tipo':False,
                      'nome':False,

                    },
            )

fig.show()




