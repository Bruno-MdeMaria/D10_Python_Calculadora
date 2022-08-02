from importlib import import_module
from art import logo
import os

print(logo)

def add (n1, n2):
    ''''Função soma valores'''
    return n1 + n2

def mult(n1, n2):
    '''Função multiplica valores'''
    return n1 * n2

def subt (n1 , n2):
    '''Função subtrai valores'''
    return n1 - n2

def div (n1, n2):
    ''''Função divide valores'''
    return n1 / n2

operacao = {                   #UM DICIONARIO COM A CHAVE(KEY) COMO SENDO OS SIMBOLOS E OS PARAMETROS SÃO  AS FUNÇÕES DEFINIDAS.
"+": add,                  #NÃO ESQUECER DAS VIRGULAS NO FINAL
"*": mult,
"-": subt,
"/": div,
}   

num1 = int(input("Qual o primeiro número?: \n"))

for simbolos in operacao:
    print(simbolos)

opera= input("Qual operação você quer fazer?: \n")

num2 = int(input("Qual o segundo número?: \n"))

calcaladora = operacao[opera]      #VARIAVEL CALCULADORA VVAI RECEBER UMA DAS FUNÇÕES DO DICIONARIO OPERACAO DEPENDENDO DA OPERAÇÃO ESCOLHIDA PELÇO USUARIO (OPERA).

resultado = calcaladora(n1=num1, n2=num2)

print(f"{num1} {opera} {num2} = {resultado}")

new_opera = input("Qual a nova operação?: \n")

num3 = int(input("Qual o novo numero?: \n"))

calcaladora = operacao[new_opera]  

new_resultado = calcaladora(resultado,num3)

print(f"{resultado} {new_opera} {num3} = {new_resultado}")

continuar = input(f"Voce quer continnuar calculando com {new_resultado}? Digite 'S' ou 'N': \n").lower()
if continuar == "n":
    repetir = False


