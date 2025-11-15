def big_line():
    purple = "\033[95m"
    bold = "\033[1m"
    reset = "\033[0m"
    print(f"{purple}{bold}-={reset}" * 27)

BOLD = "\033[1m"
RESET = "\033[0m"

big_line()
title = "Ada Wong's Suitcase - Resident Evil 4 Remake 🌹🔫".center(54).upper()
print(f"{BOLD}{title}{RESET}")
big_line()

title2 = "Asking User To Enter Some Data".center(54)
print(f"{BOLD}{title2}{RESET}")

items = []

while True:
    item = input(f"\n{BOLD}Please, Enter An Item (Q/q To Quit): {RESET}")
    if item.lower() == "q":
        break
    else:
        item_type = input(f"{BOLD}Now, Enter The Type, Please: {RESET}")
        qtt = int(input(f"{BOLD}Finally, The Quantity: {RESET}"))
        items.append((item, item_type, qtt))

big_line()
print(f"| {BOLD}{"Num":^5} | {"Item":^17} | {"Type":^11} | {"Quantity"} |")
big_line()

for counter, (item, item_type, qtt) in enumerate(items):
    print(f"| {BOLD}{counter + 1:^5} | {item:^17} | {item_type:^11} | {qtt:^8} |")
big_line()