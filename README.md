# Legislativas2022
A repository with scripts and data for the Portuguese General Elections of January 2022

## Repository Structure

### APPS 
Here you can find some Python apps that explore the datasets

1. sunburst.py creates a Sunburst visualization bu electoral circle, party, type of candidate, and candidate name
2. color_discrete_map.py is a color sequence that can be adapted to other projects. With contains a dictionary of all parties running for the 2022 elections, and the respective logo color. The color was picked from the official website or wikipedia page. 
3. crowd.py takes data from crowdtangle and plots a graph showing the accumlated likes between 08 december 2021 and 07 january 2022 on Facebook in posts that used the hashtag #Legislativas2022 

### CONTENT 
This folder contains video and images for reference 

### PDFS_CNE
This folder contains the PDFs published at [**CNE**](https://cne.pt/content/eleicoes-para-assembleia-da-republica-2022) with the final lists per electoral circle 

**FInal Lists present at 08 Jan 2022**

Aveiro

Beja

Bragança

Évora

Faro

Guarda

Leiria

Portalegre

Porto

Santarém

Setúbal

Vila Real

Viseu

Madeira

Açores

Viana do Castelo 

Braga

Coimbra

Europa 

Fora da Europa


**Missing Lists on 12 JAN 2022 **


Lisboa

Castelo Branco 

### PRODUCTS

In this folder you can find several products derived from the **PDFS_CNE** folder 
1. A .csv file with circle, party, candidate, and type columns.
**Type** stands for efective or substitute candidate
2. A combined PDF file of all available PDF files 
3. A .csv file containing an already filtered and treated dataset from Crowdtangle with the search query "#Legislativas2022" between 08/12/2021 and 07/01/2022
4. A folder with datasets from Crowdtangle with the search results for every candidate between 01 JAN 2022 to 07 JAN 2022

