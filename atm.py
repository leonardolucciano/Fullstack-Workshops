from time import ctime

class ATM:
    
    def __init__(self, balance, bank_name):
        self.__balance = balance
        self.__bank_name = bank_name
        self.__withdrawal_amount = 0
        self.__transactions_history = {}
        self.__log_in()
    
    
    def __log_in(self):
        """ In brief, this method displays the welcome message, and guides the user through the whole withdraw process """
        print("============================================================")
        print("Welcome to %s" %(self.__bank_name))
        print("============================================================")
        print()
                
        while True:
            command = 0
            while command != 1 and command != 2:
                print("""
                Enter (1) to withdraw cash
                Enter (2) to Quit the Program """)
                print("")
                command = int(input("Your choice:"))
                
            if command == 2:
                self.__show_transactions()
                input()
                exit(0)
            else:
                print("------------------------------------------------------------")
                self.__withdrawal_amount = int(input("Please enter the amount of money you want to withdraw:"))
                print("------------------------------------------------------------")
                print("Your Transaction Details:")
                print("")
                if self.__withdraw():
                    print("============================================================")
                    print("Your current balance is %i DNT" %(self.__balance))
                    print("============================================================")
                else:
                    print("You don't have the sufficient amount to withdraw!!!")
          
    
    
    def __withdraw(self):
        if self.__withdrawal_amount <= self.__balance:
            allowed_papers = [100, 50, 20, 10, 5, 2, 1] # Allowed papers and piece of money in Tunisia
            self.__transactions_history[ctime()] = str(self.__withdrawal_amount)
            for i in range(len(allowed_papers)):
                while self.__withdrawal_amount >= allowed_papers[i]:
                    print("Give -> %3i DNT" %(allowed_papers[i]))
                    self.__withdrawal_amount -= allowed_papers[i]
                    self.__balance -= allowed_papers[i]
            return True
        else:
            return False


    def __show_transactions(self):
        print("============================================================")
        print("Transactions History:")
        for transaction in self.__transactions_history:
            print("------------------------------------------------------------")
            print("%s DNT withdrawed at %s." %(self.__transactions_history[transaction], transaction))
            print("------------------------------------------------------------")
        print("============================================================")


atm1  = ATM(1000, "Python Bank")
atm1.show_transactions()
