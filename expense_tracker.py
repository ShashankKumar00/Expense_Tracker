money_amount = int(input("Money Used: "))
money_reason = input("Money Used For: ")
money_location = input("Money Used At: ")

list1 = f"{money_amount} | {money_reason} | {money_location}\n"

with open("expenses.txt", "a") as file:
    file.write(list1)