# Faça um programa em python que lê palavras digitadas pelo usuário até que ele digite "sair". 
# Depois informe quantas palavras ela digitou

print('Olá, qual seu nome?')
nome = input()
print(f'Vamos lá {nome}, nesse exercício você precisa digitar um palavra ou número e, depois,\nvocê envia pressionando Enter.')
print('Você pode digitar a quantidade que quiser que eu vou te dizer o total.\n')
print('Só te peço para enviar a palavra "sair" quando você quiser finalizar a contagem.')
print('Então vamos começar, pode digitar:')
 
#gerando a lista vazia
listaPalavras = []
infPalavras = input('')
listaPalavras.append(infPalavras)
print(listaPalavras)
#loop para inserir novas palavras na lista até a condição ser satisfeita
while infPalavras != 'sair':
    infPalavras = input('')
    listaPalavras.append(infPalavras)
#mostrar a lista na tela
#    print(listaPalavras)

if infPalavras == 'sair':
#mostrar a qnt de palavras digitadas, exceto o comando sair
    del listaPalavras[-1]
    print(f'Você digitou um total de {len(listaPalavras)} palavras.')
    print('Obrigado!!')
    exit
   