MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    amount = input("What would you like to deposit? $")
    while not amount.isdigit() or int(amount) <= 0:
        if amount.isdigit():
            print("Amount must be greater than 0.")
        else:
            print("Please enter a valid positive number.")
        amount = input("What would you like to deposit? $")
    return int(amount)

def get_number_of_lines():
    lines = input(f"Enter the number of lines to between on (1-{MAX_LINES}) ")
    while not lines.isdigit() or (int(lines) < 1 or int(lines) > MAX_LINES):
        if lines.isdigit():
            print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
        lines = input(f"Enter the number of lines to between on (1-{MAX_LINES}) ")
    return int(lines)

def get_bet():
    amount = input("What would you like to bet? $")
    while not amount.isdigit() or (MIN_BET > int(amount) or MAX_BET < int(amount)):
        if amount.isdigit():
            print(f"Amount must be between {MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
        amount = input("What would you like to bet? $")
    return int(amount)

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance, lines, bet)

main()