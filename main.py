MAX_LINES = 3
MAX_BET = 1000


def deposit():
    while True:
        
        print("desposit amount : $")
        # amount = input("What you desposit amount : $")
        amount = input()
        
        
        # if not amount.isdigit(): or 
        if  amount.isdigit()==False:
            print("invalid amount")
        else :
            _amount = int(amount)
            if _amount  <=0:
                print("invalid amount")
            else:    
                # print(f"deposited amount :${amount}") 
                return amount
    

def get_maxno_of_lines():
    while True:
        # print("no of lines you want to bet in ?")
        
        lines=input("no of lines you want to bet in  (1 - " + str(MAX_LINES) + ")?  : ")
        lines_temp=lines
        # print(lines_temp)
        
       
        if lines.isdigit() ==False:
            print("enter a valid number") 
                
        else:
            n=int(lines_temp)
            # print(n)
            if n <= 0 or n > MAX_LINES :
                print("inavlid no of lines please enter from the specified range")
            else:
                # print(f"no of lines you want to bet in : {lines}")
                return lines
def get_bet():
    while True:
        bet = input("what would you like to bet : ")
        bet_temp = bet
        
        if bet.isdigit() == False:
            print("invalid bet")
        
        else:
            n=int(bet_temp)
            if not  n > 0  or not n <= MAX_BET:
                print("invalid bet amount") 
            else:
                # print(bet)
                return bet
                # break
    # else:
    #     print("no balance")
    #     return bet
def get_bet_check(balance,lines):
    while True:
        # bet = get_bet()
        # total = bet*lines
        # print(bet)
        bet = int(get_bet())
        total = lines * bet
        print(total)
        
        if balance < total:
            print("not enough balance")#no line after this so it goes back to the start of the loop which is the While True : statement

            
        else:
            # final_balance = balance - total
            break
            # print(f"your total after youve placed youre bet will be ${final_balance}")
    print(f"you are betting ${bet} on lines : {lines} for a total of ${total}")
          

        
# get_maxno_of_lines() 
def main():
    balance = deposit()
    lines = int(get_maxno_of_lines())
    # bet = int(get_bet())
    # total = lines * bet
    # print(total)
    # int(get_bet_check(balance,total))
    get_bet_check(int(balance),lines)
    

main()


# if __name__=="__main__":
#     print("amount stored succesfully")
        