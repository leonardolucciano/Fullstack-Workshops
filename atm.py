
balance = 500
request = 360

def withdraw(balance, request):
    try:
        if request > balance:
            raise ValueError("Invalid Amount")

        allowed_papers = [100, 50, 20, 10, 5, 2, 1] # Allowed papers and piece of money in Tunisia
        for i in range(len(allowed_papers)):
            while request >= allowed_papers[i]:
                print("Give -> %3i DNT" %(allowed_papers[i]))
                request -= allowed_papers[i]
                balance -= allowed_papers[i]
        return balance
    except ValueError as exp:
        return exp

balance = withdraw(balance, request)

if balance is 'Invalid Amount':
    print("You don't have this amount of money in your account!")    
else:
    print("***********Balance***********")
    print("Your balance is now %3i DNT" %(balance))
    print("*****************************")
    
    
        
       
           
    
