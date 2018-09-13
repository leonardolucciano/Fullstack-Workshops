
balance = 500
request = 650

# Allowed papers and piece of money in Tunisia
allowed_papers = [100, 50, 20, 10, 5, 2, 1]

for i in range(len(allowed_papers)):
    while request >= allowed_papers[i]:
        print("Give -> %3i DNT" %(allowed_papers[i]))
        request -= allowed_papers[i]
        balance -= allowed_papers[i]

print("***********Balance***********")
print("Your balance is now %3i DNT" %(balance))
print("*****************************")
        
       
           
    
