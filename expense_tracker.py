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

print("==================================================")
print("       PERSONAL EXPENSE & LEDGER DASHBOARD        ")
print("==================================================")
print("-> Press [F2] globally to display category summaries.")
print("-> Type 'exit' in the 'Money Used' prompt to close the app safely.\n")

while True:
    money_amount = (input("Money (+ for Earned / - for Spent):"))
    if money_amount == "exit":
        break
    money_amount = int(money_amount)
    money_reason = (input("Transaction Category: "))
    money_location = (input("Transaction Source: "))

    list1 = f"{money_amount} | {money_reason} | {money_location}\n"

    with open("expenses.txt", "a") as file:
        file.write(list1)
