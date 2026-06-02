money_amount = int(input("Money Used: "))
money_reason = (input("Money Used For: "))
money_location = (input("Money Used At: "))

list1 = f"{money_amount} | {money_reason} | {money_location}\n"

with open("expenses.txt", "a") as file:
    file.write(list1)

category_spending = {}
total_spending =  0
with open("expenses.txt", "r") as file:
    for items in file:
        var = items.split(" | ")
        value = float(var[0])
        total_spending += value

        category = var[1]
        if category in category_spending:
            category_spending[category] += value
        else:
            category_spending[category] = value

    print(f"Your Total expenditure is {total_spending}")