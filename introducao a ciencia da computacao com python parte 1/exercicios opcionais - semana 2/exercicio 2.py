se = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dia = se // 86400
se  = se % 86400
hora = se // 3600
se = se % 3600
minu = se // 60
se = se % 60

print(dia,'dias,',hora,'horas,',minu,'minutos e',se,'segundos.')
