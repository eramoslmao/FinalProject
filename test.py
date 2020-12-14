#User interface screen
print('Hello and thank you for using Estimator by Ramos Inc. A cost estimator for construction in NYC')
print('How long will your project be in weeks?')
length = input()
print('How big will your project be in terms of area?(Square feet)')
area = input()
print('What would you like to start with? Type in Labor or Material. (Case sensitive)')
user = input()
if user == 'Material':
  print("Which material are you looking for? Steel, Wood or Concrete?")
  reply = input()
  if reply == 'Steel':
    laborsub = 0
    select_from_db("""

    SELECT * FROM steel_data;

    """, 'steel')
    print('Choose your item')
    steelchoice = input()
    print(steelchoice)
    materialsub = '400 per beam'
    print('Cost recorded!')
  elif reply == 'Concrete':
    laborsub = 0
    materialsub = concrete_calc(area)
    print('Cost recorded!')
  elif reply == 'Wood':
    laborsub = 0
    print('How many planks?')
    planks = input()
    materialsub = wood_calc(planks)
    print('Cost recorded!')
  else:
    print('Oh no, an error occurred, please rerun the program!')
elif user == 'Labor':
  materialsub = 0
  select_from_db("""

    SELECT * FROM labor_data

    """, 'labor')
  print('Choose your item')
  laboritem = input()
  print(laboritem)
  rate = 20
  laborsub = labor_calc(laborCost)
  print('Cost recorded!')
else:
  print("Error occurred! Please rerun the program")

#Summary Table - - - - - - - - - - -
def display_menu():
   print ("Category\t\t\tcost\t\tsubtotal")
print ("---------------------------------------------------------------")
print ('Labor cost is ' + str(laborsub))
print ('Materials cost is ' + str(materialsub))
print ("---------------------------------------------------------------")
print ('Run again to calculate other costs!')
