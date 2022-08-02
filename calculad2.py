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

def calculadora():
    num1 = float(input("Digite um número?: \n"))
    parar = False

    while not parar:

        for simbolos in operacao:
            print(simbolos)

        opera= input("Qual operação você quer fazer?: \n")

        num2 = float(input("Qual o novo número?: \n"))

        calcaladora = operacao[opera]      #VARIAVEL CALCULADORA VVAI RECEBER UMA DAS FUNÇÕES DO DICIONARIO OPERACAO DEPENDENDO DA OPERAÇÃO ESCOLHIDA PELÇO USUARIO (OPERA).

        resultado = calcaladora(n1=num1, n2=num2)

        print(f"{num1} {opera} {num2} = {resultado}")

        continuar1 = input(f"Voce quer continnuar calculando com {resultado}? Digite 'S' ou 'N': \n").lower()
        if continuar1 == "n":
            parar = True
            os.system("cls")
            calculadora()
        else: 
            num1 = resultado
calculadora()
    