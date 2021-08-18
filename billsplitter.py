import random

guests_dict = {}
try:
    no_of_guests = int(input("Enter the number of friends joining (including you):"))
    print()
    assert no_of_guests > 0
    print("Enter the name of every friend (including you), each on a new line:")
    for guest in range(no_of_guests):
        guests_dict[f"{input()}"] = 0
    print()
    bill = int(input("Enter the total bill value:"))
    for guest in guests_dict:
        guests_dict[f"{guest}"] = round(bill / no_of_guests, 2)
    try:
        print()
        lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        assert lucky == "Yes"
        fin_choice = random.choice(list(guests_dict.keys()))
        print()
        print(fin_choice, "is the lucky one!")
        for guest in guests_dict:
            guests_dict[f"{guest}"] = round(bill / (no_of_guests - 1), 2)
            if guest == fin_choice:
                guests_dict[f"{fin_choice}"] = 0
        print()
        print(guests_dict)
    except AssertionError:
        print()
        print("No one is going to be lucky")
        print()
        print(guests_dict)
except AssertionError:
    print("No one is joining for the party")
