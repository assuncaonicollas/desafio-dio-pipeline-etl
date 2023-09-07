# Neste desafio foi criada uma Pipeline ETL onde foi utilizado um banco de dados em arquivo .csv, foram feitas calculos e criação de novas colunas nesse banco de dados, e por fim criado um novo arquivo .csv com as novas informações

#------------------Extract: extraindo um arquivo .csv para trabalhar
import pandas as pd
import csv
import numpy as np

tabela = pd.read_csv("/Users/nicollas_assuncao/Desktop/JOB/dio/dt_housing.csv", sep = ";")

print(tabela, "\n")

#------------------Transform: transformar as colunas que iremos utilizar em variáveis númericas, para podermos executar calculos e criar novas colunas com novas informações
tabela['Sqft'] = pd.to_numeric(tabela['Sqft'])
tabela['Price'] = pd.to_numeric(tabela['Price'])

tabela['Square Meter'] = tabela['Sqft'] * 0.09290304
tabela['Price per Mt'] = tabela['Price'] / tabela['Square Meter']

tabela['Square Meter'] = np.round(tabela['Square Meter'], decimals=2)
tabela['Price per Mt'] = np.round(tabela['Price per Mt'], decimals=2)

print(tabela, "\n")

#------------------Load: carregar as modificações feitas na tabela em um novo arquivo .csv
tabela.to_csv('desafio_etl.csv')
