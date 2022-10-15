v = q = t = 0
cont = ''
quit = ''
while True:

  while True:
    while True:
      try:
        v = float(input('Value: '))
      except ValueError:
        print("You must enter a number.")
      else:
        break
    q += 1
    t += v
    cont = str(input('Enter any key to continue or "n" to stop: ')).strip().lower()
    if cont == 'n':
      print('End')
      break
  print(f'Total = {t}\nItems quantity = {q}')
  print('-'*30)

  quit = str(input('Go to the next set of items [y/n]: ')).strip().lower()
  if quit == 'n':
    break


print('End of the program')