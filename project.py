MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

#collecting user input
def deposit():
    while True:
        amount=input("DEPOSIT AMOUNT||Ksh ")
        if amount.isdigit():#isdigit can be used on strings to determine validity of a number.
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("SET AMOUNT TO GREATER THAN 0.")
        else:
            print("ENTER AMOUNT.")

            return amount
        
#Number of lines
def get_number_of_lines():
    while True:
        lines =input("INPUT NUMBER OF LINES|| (1- " + str(MAX_LINES )+ ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("ENTER VALID NUMBER of LINES||.")
        else:
            print("INVALID NUMBER.")

    return lines
#----------------------------------------------#
def get_bet():
    """while True:
        amount=input("SET BET AMOUNT||Ksh ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"BET AMOUNT RANGE||. Ksh{MIN_BET} - Ksh{MAX_BET}")
        else:
            print("ENTER BET AMOUNT.")

            return amount"""
       
    while True:
        amount = input("SET BET AMOUNT||Ksh ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount  # Return the valid amount
            else:
                print(f"BET AMOUNT RANGE||. Ksh{MIN_BET} - Ksh{MAX_BET}")
        else:
            print("ENTER BET AMOUNT.")


"""def main():
    yourbalance = deposit()
    lines= get_number_of_lines()
    while True:
      
      bet = get_bet()
      total_bet = bet * lines

      if total_bet > yourbalance:
          print(f"NOT ENOUGH BALANCE, BALANCE IS:|| Ksh{yourbalance}")
      else:
          break
    print(f"ENTERED BET IS|Ksh {bet} on {lines} lines. Total bet is equal to: Ksh{total_bet}")
    
    
   

main()"""
def main():
    yourbalance = deposit()
    if yourbalance is None or not isinstance(yourbalance, int):
        print("Error: Unable to retrieve balance. Please check your deposit function.")
        return
    
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        if bet is None or not isinstance(bet, int):
            print("Error: Invalid bet amount. Please enter a valid integer.")
            continue
        
        total_bet = bet * lines
        if total_bet > yourbalance:
            print(f"NOT ENOUGH BALANCE, BALANCE IS:|| Ksh{yourbalance}")
        else:
            break
    
    print(f"ENTERED BET IS|Ksh {bet} on {lines} lines. Total bet is equal to: Ksh{total_bet}")

main()

