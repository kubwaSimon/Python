import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROW = 3
COL = 3

symbol_cnt ={
    "A": 2,
    "B": 3,
    "C": 5,
    "D": 7
}

def get_project_count(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_cnt in symbols.items():
        for _ in range(symbol_cnt):
            all_symbols.append(symbol)


    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns



def get_project_count(columns):
    for row in range (len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end ="")

    print()



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


def main():
  
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
    
    slots = get_project_count(ROW, COL, symbol_cnt)
    get_project_count(slots)
   

main()


