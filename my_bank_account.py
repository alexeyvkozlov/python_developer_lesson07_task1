
#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\python_developer_lesson07_task1
# cd d:\python_developer\python_developer_lesson07_task1
#~~~~~~~~~~~~~~~~~~~~~~~~
# python my_bank_account.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bill_sum = 0
history = []

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_balance(bill_sum):
  prog_path = os.getcwd()
  fname = os.path.join(prog_path, 'balance.txt')
  with open(fname, 'w') as file:
    file.write(str(bill_sum))

def load_balance():
  prog_path = os.getcwd()
  fname = os.path.join(prog_path, 'balance.txt')
  print(f'load_history: fname: {fname}')
  try:
    with open(fname, 'r') as file:
      return int(file.read())
  except FileNotFoundError:
    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def save_history():
  prog_path = os.getcwd()
  fname = os.path.join(prog_path, 'history.txt')
  with open(fname, 'a') as file:
    for item in history:
      file.write(f"{item[0]} - {item[1]}\n")

def load_history():
  prog_path = os.getcwd()
  fname = os.path.join(prog_path, 'history.txt')
  print(f'load_history: fname: {fname}')
  try:
    with open(fname, 'r') as file:
      lines = file.readlines()
      for line in lines:
        name, cost = line.strip().split(' - ')
        history.append((name, int(cost)))
  except FileNotFoundError:
    print('Файл истории не обнаружен')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def buy(bill_sum):
  cost = int(input('Введите сумму покупки: '))
  if cost > bill_sum:
    print('Недостаточно средств')
  else:
    bill_sum -= cost
    name = input('Введите название покупки: ')
    history.append((name, cost))
    save_history()
  return bill_sum

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~
bill_sum = load_balance()
load_history()
#~~~~~~~~~~~~~~~~~~~~~~~~
while True:
  print()
  print('~'*70)
  print('1. пополнение счета')
  print('2. покупка')
  print('3. история покупок')
  print('4. выход')
  print(f'Ваш счет {bill_sum}')
  choice = input('Выберите пункт меню: ')
  if choice == '1':
    cost = int(input('Введите сумму: '))
    bill_sum += cost
  elif choice == '2':
    bill_sum = buy(bill_sum)
  elif choice == '3':
    print(history)
  elif choice == '4':
    save_balance(bill_sum)
    break
  else:
    print('Неверный пункт меню')