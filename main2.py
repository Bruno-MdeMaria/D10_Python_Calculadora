def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    '''Determina quantos dias tem no mês'''
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if month > 12 or month < 1:
        return "Valor de mês invalido."
    if is_leap(year) == True and month ==2:
        return 29
    else: return month_days[month - 1] #SE NÃO FOR VERDADE RETORNA DIA DA LISTA REFERENTE A POSICAO MONTH ESCOLHIDA MENOS(-) 1 POR CAUSA QUE A LISTA COMEÇA COM 0. eX. JANEIRO MES 2 VAI SER A POSIÇÃO DA LISTA 1.


# 🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)