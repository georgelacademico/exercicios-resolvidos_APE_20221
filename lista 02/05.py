#A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário-mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu salário.
vendas = float(input('Valor total das vendas: '))
salario = vendas / 20
if salario < 1212:
    print('Salário abaixo do mínimo. Verifique.')
else:
    print(f'Salário: R$ {salario}.')