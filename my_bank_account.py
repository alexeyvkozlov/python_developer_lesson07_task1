
#~ USAGE
# cd c:\python_developer
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd c:\python_developer\lesson_07_task1
# cd d:\python_developer\lesson_07_task1
#~~~~~~~~~~~~~~~~~~~~~~~~
# python my_bank_account.py
#~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bill_sum = 0
history = []

def buy(bill_sum):
  cost = int(input('Введите сумму покупки: '))
  if cost > bill_sum:
    print('Недостаточно средств')
  else:
    bill_sum -= cost
    name = input('Введит название покупки: ')
    history.append((name, cost))
  return bill_sum

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    break
  else:
    print('Неверный пункт меню')
