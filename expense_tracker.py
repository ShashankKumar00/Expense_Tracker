import keyboard

def display_summary():
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

    print(f"\n--- [ LIVE BALANCE: {total_spending} ] ---")
    for cat, amt in category_spending.items():
        print(f" * {cat}: {amt}")
    print("------------------------------------------\n")


keyboard.add_hotkey('F2', display_summary)

print("LEDGER RUNNING IN SECURE BACKGROUND MODE...")
print("-> Press [F2] globally to display summaries.\n")

while True:
    money_amount = (input("Money Used: "))
    if money_amount == "exit":
        break
    money_amount = int(money_amount)
    money_reason = (input("Money Used For: "))
    money_location = (input("Money Used At: "))

    list1 = f"{money_amount} | {money_reason} | {money_location}\n"

    with open("expenses.txt", "a") as file:
        file.write(list1)