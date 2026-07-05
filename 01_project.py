# inputs we need from the user::
# total rent
# total food ordered for snaking
# electricity units spend
# charge per unit


# output
# total amount you have to pay per person is 

total_rent = int(input("Enter the total rent: "))
total_food = int(input("Enter the total food ordered for snacking: "))
electricity_units = int(input("Enter the electricity units spent: "))
electric_fees=electricity_units * 9
print(f"your total charge is {total_rent + total_food + electric_fees}")

total_people = int(input("Enter the total number of people: "))
print(f"""your total charge per person is {(total_rent + total_food + electric_fees) / total_people}\n 
        THANK YOU FOR USING OUR SERVICE""")
