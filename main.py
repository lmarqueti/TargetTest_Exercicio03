'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

import json

with open('dados.json') as file:
    dados = json.load(file)

faturamento_diario = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamento_diario)

maior_faturamento = max(faturamento_diario)

media_mensal = sum(faturamento_diario) / len(faturamento_diario)

dias_acima_da_media = 0
for faturamento in faturamento_diario:
    if faturamento > media_mensal:
        dias_acima_da_media += 1

print("Menor valor de faturamento diário:", menor_faturamento)
print("Maior valor de faturamento diário:", maior_faturamento)
print("Número de dias com faturamento diário acima da média mensal:", dias_acima_da_media)
