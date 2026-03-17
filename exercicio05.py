#Faça um programa que leia algo pelo teclado e mostre na tela o seu 
# tipo primitivo e todas as informações sobre ela n\

algumaCoisa = input('Digite alguma coisa: ')
print('o tipo primitivo é',type(algumaCoisa))
print('Esse valor é númerico?',algumaCoisa.isnumeric())
print('Esse valor tem espaços?',algumaCoisa.isspace())
print('Esse valor é alfabético?',algumaCoisa.isalpha())