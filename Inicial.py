import pandas  as pd
import plotly.express as px


tabela = pd.read_excel("AMAZONPREV CAMPO N PREENCHIDO.xlsx")
print(tabela)


print(tabela.info())
#Tratanto dados, excluindo coluna ou linha da base 
# tabela = tabela.drop_duplicates() # apaga os registros duplicados

#informação vazia  ou está no formato errado
print(tabela.info())

# em percentual = normalizado

print(tabela ["ETAPA_CADASTRO"].value_counts(normalize=True))

# criando grafico para cada coluna

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="ETAPA_CADASTRO",text_auto=True)
    grafico.show()


# analisar 3 problemas de cancelamento

# 1- duração de contrato não pode ser mensal

# tabela = tabela [tabela ["duracao_contrato"]!= "Monthly"]

# #2- ligações call center  só pode ser de até 4 ligações

# tabela = tabela [tabela ["ligacoes_callcenter"] <=4]

# #3- atrasos só podem ser de até 20 dias 

# tabela = tabela [tabela ["dias_atraso"] <=20]

# print(tabela ["cancelou"].value_counts(normalize=True))