class ATM:
    
    def __init__(self, balance, bank_name):
        self.__balance = balance
        self.__bank_name = bank_name
        self.__withdrawal_amount = 0
        self.log_in()


    def __getBalance(self):
        """ Return the current 'balance' """
        return self.__balance


    def __getBankName(self):
        """ Return the bank's name """
        return self.__bank_name


    def __setWithdrawalAmount(self, withdrawal_amount):
        """ This method sets the 'withrawal_amount' """
        self.__withdrawal_amount = withdrawal_amount
    
    
    def log_in(self):
        """ In brief, this method displays the welcome message, and guides the user through the whole withdraw process """
        print("==============================")
        print("Welcome to %s" %(self.__getBankName()))
        print("==============================")
        print()
        print("Please enter the amount of money you want to withdraw:")
        self.__setWithdrawalAmount(int(input()))
        if self.withdraw():
            print("==============================")
            print("Your current balance is ", self.__getBalance())
            print("==============================")
        else:
            print("You don't have the sufficient amount to withdraw")
            
    
    
    def withdraw(self):
        if self.__withdrawal_amount <= self.__getBalance():
            allowed_papers = [100, 50, 20, 10, 5, 2, 1] # Allowed papers and piece of money in Tunisia
            for i in range(len(allowed_papers)):
                while self.__withdrawal_amount >= allowed_papers[i]:
                    print("Give -> %3i DNT" %(allowed_papers[i]))
                    self.__withdrawal_amount -= allowed_papers[i]
                    self.__balance -= allowed_papers[i]
            return True
        else:
            return False


atm1  = ATM(1000, "Python Bank")
