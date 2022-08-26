"""Considerar as variáveis para cada aliquota
            Base de cálculo         (R$)	            Alíquota (%)
            Abaixo de               1.903,99	            0%
sete        De                  1.903,99 até 2.826,65	    7,5%
quinze      De                  2.826,66 até 3.751,05	    15%
vinteDois   De                  3.751,06 até 4.664,68	    22,5%
vinteSete   Acima de            4.664,68	                27,5%"""
#variaveis atribuidas para o calculo da aliquota
sete= 1 * 0.075
quinze = 1 * 0.15
vinteDois = 1 * 0.225
vinteSete = 1 * 0.275

#habilitar laço while caso o user deseje seguir com as pesquisas
#se desabilitado, user faz uma pesquisa e encerra o programa
while True:
#como fazer para evitar que o user envie um input vazio (enter) ou que não seja do tipo solicitado (caracter ao invés de números)?
    salario = float(input('Qual o salário do funcionário? Digite apenas números e se precisar separar as \ncasas decimais use .(ponto)'))
##    if salario != float(input("")): print('Digite apenas números e se precisar separar as \ncasas decimais use .(ponto)')
    if salario < float(1903.99): print('Não há desconto de Imposto de Renda.') 
    if salario >= float(1903.99) and salario <= float(2826.65): print(f'O valor a ser descontado é de: R$ {salario * sete:.2f}')
    if salario >= float(2826.66) and salario <= float(3751.05): print(f'O valor a ser descontado é de: R$ {salario * quinze:.2f}')
    if salario >= float(3751.06) and salario <= float(4664.68): print(f'O valor a ser descontado é de: R$ {salario * vinteDois:.2f}')
    if salario > float(4664.68):print(f'O valor a ser descontado é de: R$ {salario * vinteSete:.2f}')
 ##   if salario == (): 
 ##       exit('Opção inválida. Reinicie a aplicação.')
    comando = input("Digite:\n 'c' para continuar,\ncaso contrario\n 's' para sair ")
    if comando == 'c': (salario)
    if comando == "s":
            exit('Programa Finalizado')
    if comando != 'c' and 's': 
        exit(print('Opção inválida. Reinicie a aplicação.'))