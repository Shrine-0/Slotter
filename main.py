# #! alertbar 
# # highlight
# ? should this be publicised 
# TODO make a loading bar or load tab before you start the game
# Todo make it modular by adding classes
# @param check_for_wins()

import random as rd
from time import sleep
from tqdm import tqdm,trange

MAX_LINES = 3
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def get_slot_machine_spin(rows, cols, symbols, lines):
    all_symbols = []

    # list comprehension  --- 1
    count = [symbols for symbols, counts in symbol_count.items() for _ in range(counts)]
    # print(count)

    # simple method       --- 2 s
    for symbols, counts in symbol_count.items():
        # print(counts)
        for _ in range(counts):
            all_symbols.append(symbols)

    # print(all_symbols)
    columns = []

    for _ in range(lines):
        column = []
        current_symbols = all_symbols[:]  # : colon essential for copying not reference copy but creating a new reference

        for _ in range(cols):
            value = rd.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    i = 0
    print("\n")
    while True:
        for _ in tqdm(range(100),desc="Loading your slots",leave=False):
                # r=rd.random()
                sleep(0.1)
        for ind, value in enumerate(column for column in columns):
            if i == ind:
                j = 0
                current_value = [C_values for C_values in value]
                for ind, value in enumerate(current_value):
                    if j * 2 <= ind + 1:
                        print(value, end=" | ")

                    else:
                        print(value, end="")
                    j += 1
                print("\n")
                i += 1
            else:
                pass
        break


def check_for_wins(columns,lines,balance,symbol_value,bet):
    # columns=[["C","D","C"],["B","B","B"]]
    winnings = []
    
    for i in range(lines):
    # for i in tqdm(range(lines),desc="Loading..",leave=False):
        # print(f"i : {i}")
        value = 0
        for _ in tqdm(range(100),desc="Loading your wins",leave=False):
                # r=rd.random()
                sleep(0.01)
        for j in range(len(columns[i])):
            
            # if j>=len(columns[i]):
            #     print(f"j : {j} out of index")
            #     continue
            
            
                    
            if columns[i][0] != columns[i][j] :
                # print("break",columns[i][j]5
                # r=rd.random()
                # sleep(r)
                value = 0
                totalvalue = value
                break
            else:
                # print(columns[i][j])
                value += symbol_value[columns[i][j]]* bet 
                # print(f"value : {value}")  
                totalvalue = value    
            
        winnings.append(totalvalue)
        print(f"total winnings for line {i} : {winnings[i]}") 
        
    # for i in tqdm(range(len(winnings)),desc="Loading..",leave=False):
    #     sleep(2)   
    #     print(f"total winnings for line {i} : {winnings[i]}") 
    print("\n")
        
    

def deposit():
    while True:
        # print("desposit amount : $")
        # amount = input("What you desposit amount : $")
        amount = input("desposit amount : $")
        print("\n")

        # if not amount.isdigit(): or
        if amount.isdigit() == False:
            print("invalid amount")
        else:
            _amount = int(amount)
            if _amount <= 0:
                print("invalid amount")
            else:
                # print(f"deposited amount :${amount}")
                return amount


def get_maxno_of_lines():
    while True:
        # print("no of lines you want to bet in ?")

        lines = input(
            "no of lines you want to bet in  (1 - " + str(MAX_LINES) + ")?  : "
        )
        print("\n")
        lines_temp = lines
        # print(lines_temp)

        if lines.isdigit() == False:
            print("enter a valid number")

        else:
            n = int(lines_temp)
            # print(n)
            if n <= 0 or n > MAX_LINES:
                print("inavlid no of lines please enter from the specified range")
            else:
                # print(f"no of lines you want to bet in : {lines}")
                return lines


def get_bet():
    while True:
        bet = input("what would you like to bet : $")
        print("\n")
        bet_temp = bet

        if bet.isdigit() == False:
            print("invalid bet")

        else:
            n = int(bet_temp)
            if not n > 0 or not n <= MAX_BET:
                print("invalid bet amount")
            else:
                # print(bet)
                return bet
                # break
    # else:
    #     print("no balance")
    #     return bet


def get_bet_check(balance, lines):
    while True:
        # bet = get_bet()
        # total = bet*lines
        # print(bet)
        bet = int(get_bet())
        total = lines * bet
        # print(total)

        if balance < total:
            print(
                "not enough balance"
            )  # no line after this so it goes back to the start of the loop which is the While True : statement

        else:
            # final_balance = balance - total
            break
            # print(f"your total after youve placed youre bet will be ${final_balance}")
    print(f"you are betting ${bet} on number of lines : {lines} for a total of ${total}")
    return True,bet

def loading_game():
    # t= trange(10,desc = "loading",leave=False)
    # for i in t:
    #     t.set_description("loading please wait",refresh=True)
    #     sleep(2)
    for i in tqdm(range(5),desc="Loading",leave=False):
        sleep(0.5)


# get_maxno_of_lines()
def main():
    loading_game()
    balance = deposit()
    lines = int(get_maxno_of_lines())
    value,bet = get_bet_check(int(balance), lines)
    # print(bet)
    if value == True:
        columns = get_slot_machine_spin(ROWS, COLS, symbol_count, lines)
        # print(columns,"\n")
        print_slot_machine(columns)
        check_for_wins(columns,lines,balance,symbol_value,bet)


main()


if __name__ == "__main__":
    
    print("Thanks for playing the Slot machine by NT")
