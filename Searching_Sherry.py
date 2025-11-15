def big_line():
    red = "\033[91m"
    bold = "\033[1m"
    reset = "\033[0m"
    print(f"{red}{bold}-={reset}" * 25)

def characters():
    print("""\n👩‍🦰 - Claire Redfield
👧 - Sherry Birkin
🧟 - Zombie""")

def mission():
    print("""\n1. You Are Claire Redfield.
2. Your Mission Is To Rescue Sherry Birkin.
3. RPD's Max Coordinates Are 8x8.
4. If Your Attempts Surpass 5, She Will Die.""")

BOLD = "\033[1m"
RESET = "\033[0m"

big_line()
title = "Resident Evil 2 - Searching for Sherry".center(50)
print(f"{BOLD}{title}{RESET}")
big_line()

title2 = "Main Characters Of The Game".center(50)
print(f"{BOLD}{title2}{RESET}")
characters()

title3 = "\n\t\t\tExplaining The Game".center(50)
print(f"{BOLD}{title3}{RESET}")
mission()
big_line()

title4 = "Asking User To Enter Data".center(50)
print(f"{BOLD}{title4}{RESET}")

rows = 8
columns = 8
attempts = 0

asking_rows = int(input("\nEnter a Number For Rows: "))
asking_columns = int(input("Enter a Number For Columns: "))

while asking_rows != 6 or asking_columns != 3:
    attempts += 1

    if attempts >= 5:
        print(f"\nIt Took You {attempts} attempts, Claire...")
        print("That Means Sherry Birkin is.... DEAD 👧🧟🩸⚰️")
        print(f"Game Over".upper())
        break

    print("\nSherry Can't Wait No More, Claire! Hurry Up!")
    asking_rows = int(input("\nEnter a Number For Rows: "))
    asking_columns = int(input("Enter a Number for Columns: "))


else:
    print(f"\nIt Only Took You {attempts} Attempts, Redfield...")
    print("Well Done, Claire! Sherry Is Now Safe Thanks To You!")

    print()

    for r in range(rows):
        for c in range(columns):
            if r == 0 and c == 0:
                print('👩‍🦰', end=' ')
            elif r == 6 and c == 3:
                print('👧', end=' ')
            else:
                print('🧟', end=' ')
        print()
    title5 = "Raccoon City Department 👮🏩"
    print(f"\n{BOLD}{title5}{RESET}")


