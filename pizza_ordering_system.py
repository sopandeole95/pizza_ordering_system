print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")

add_pepperoni = input("Do you want pepperoni? Y or N ")

pep = 0

extra_cheese = input("Do you want extra cheese? Y or N ")

che=0

bill=0



if size=="L":

  bill += 25

  if add_pepperoni=="Y":

    pep += 3

    if extra_cheese=="Y":

      che += 1

      print(f"Your bill is ${bill+pep+che}")

    else:

      print(f"Your bill is ${bill+pep}")  

  else:

    print(f"Your bill is ${bill}")



if size=="M":

  bill += 20

  if add_pepperoni=="Y":

    pep += 3

    if extra_cheese=="Y":

      che += 1

      print(f"Your bill is ${bill+pep+che}")

    else:

      print(f"Your bill is ${bill+pep}")  

  else:

    print(f"Your bill is ${bill}")



if size=="S":

  bill += 15

  if add_pepperoni=="Y":

    pep += 3

    if extra_cheese=="Y":

      che += 1

      print(f"Your bill is ${bill+pep+che}")

    else:

      print(f"Your bill is ${bill+pep}")  

  else:

    print(f"Your bill is ${bill}")