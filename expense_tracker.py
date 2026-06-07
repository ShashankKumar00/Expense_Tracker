import keyboard

from datetime import date

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

def display_month_summary():
    monthly_ledger = {}
    with open("expenses.txt", "r") as file:
        for items in file:
            var_0 = items.split(" | ")
            date_category = var_0[1]
            date_value = float(var_0[0])
            date_string = var_0[3]
            month_key = date_string[:7]

            if month_key not in monthly_ledger:
                monthly_ledger[month_key] = {}

            if date_category in monthly_ledger[month_key]:
                monthly_ledger[month_key][date_category] += date_value
            else:
                monthly_ledger[month_key][date_category] = date_value
    
    print("\n========= [ MONTHLY DATE SHEET ] =========")
    for month, categories in monthly_ledger.items():
        print(f"\n[ {month} ]")
        
        for cat, amt in categories.items():
            print(f"  * {cat}: {amt}")
            
    print("\n==========================================")
        
keyboard.add_hotkey('F3', display_month_summary)

print("==================================================")
print("       PERSONAL EXPENSE & LEDGER DASHBOARD        ")
print("==================================================")
print("-> Press [F2] globally to display category summaries.")
print("-> Press [F3] globally to display date wise summary.")
print("-> Type 'exit' in the 'Money Used' prompt to close the app safely.\n")

while True:
    money_amount = (input("Money (+ for Earned / - for Spent):"))
    if money_amount == "exit":
        break
    money_amount = int(money_amount)
    money_reason = (input("Transaction Category: "))
    money_location = (input("Transaction Source: "))
    current_date = date.today()

    list1 = f"{money_amount} | {money_reason} | {money_location} | {current_date}\n"

    with open("expenses.txt", "a") as file:
        file.write(list1)
