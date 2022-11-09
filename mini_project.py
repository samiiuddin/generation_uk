#Mini Project

drinks = ['red bull', 'pepsi', 'Fanta']

def drinks_index():
  for x in drinks:
    print(f'{((drinks.index(x)) + 1)}. {x}')

print('Welcome\nEnter 0 to Exit App\nEnter 1 for Main Menu')
enter = int(input(10))

if enter == 0:
  print('\nExit, Thank You')
else:
  print('\nChoose Option:\n0. Return to Main Menu\n1. Product List\n2. Create New Product\n3. Update Product\n4. Delete a Product')

user_input = int(input())

while user_input > 5 or user_input < 0:
  print('Enter Number between 0 and 4')
  user_input = int(input())
if user_input == 0:
  pass 
elif user_input == 1:
  print('\nDrinks:\n')
  drinks_index()
  cstmr_drink = input('\nChoose your drink:\n')
  while str(cstmr_drink) not in  drinks:
    print('\nChoose a drink in the menu:\n')
    cstmr_drink = str(input())
  print('\nWould you like Ice \nEnter yes/no:')
  option_input = str(input())
  if option_input == 'yes':
    print(f'\nServing {cstmr_drink} with Ice')
  elif option_input == 'no':
    print(f'\nServing {cstmr_drink} without Ice')
  else:
    option_input = str(input('Please Enter yes/no:'))
elif user_input == 2:
  add_item = input('\nAdd Item:\n')
  drinks.append(str(add_item))
  print('\nNew Drink List:')
  drinks_index()
elif user_input == 3:
  print('\nChoose a list item to be changed')
  drinks_index()
  drinks_change = str(input('\nItem to Change:'))
  drinks_add = str(input('\nItem to Add:'))
  drinks[(drinks.index(drinks_change))] = drinks_add
  drinks_index()
elif user_input == 4:
  for x in drinks:
    print(f'{((drinks.index(x)) + 1)}. {x}')
  print('\nDelete an Item')
  del_input = input('\nDelete: ')
  if del_input in drinks:
    drinks.remove(del_input)
  print(f'\n{del_input} has been deleted\n')  
  drinks_index()

  #this is a comment
  print("This is my Mini Project")
  
