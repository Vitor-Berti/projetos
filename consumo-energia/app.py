#Entrada de dados
aparelho = input("Diga o nome do aparelho")
potencia = float(input("Qual a potência do aparelho em Watts (W)"))
horasdia = float(input("Quantas horas de uso por dia?"))
#Processamento
consumomensal  = (potencia * horasdia * 30)/ 1000
#Saída
print ("Aparelho:",aparelho)
print ("Consumo Estimado:",consumomensal, "kWh/mês") 