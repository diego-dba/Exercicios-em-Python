#Valor do etanol inf pelo user
etaInf = float(input("Qual o valor do etanol? "))
#Valor da gasolina inf pelo user
gasInf = float(input("Qual o valor da gasolina? "))

#conversão do valor da gasolina para porcentagem
gasolina = (gasInf * 0.7)
#condiçao do valor do etanol informado vs porc da gasolina
if etaInf > gasolina: print('Prefira abastecer com gasolina.')
else: print('Prefira abastecer com etanol.')


##  Carro flex 
## se o valor etanol for maior que 70% do valor gasolina -> gasolina
## se o valor do etanol for menor ou igual a 70% do valor gasolina -> etanol
