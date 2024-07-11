purchase = float(input(("How much does the product cost?")))

# initialization

change = 100 - purchase*100
print(change)
quarters = 0
dimes = 0
pennies = 0

if change >= 25:
    quarters = int(change // 25)
    change -=  quarters*25

if change >= 10:
    dimes = int(change // 10)
    change -= dimes*10

if change < 10:
    pennies = int(change)



print (f'Your change is:\n{quarters} quarters \n{dimes} dimes \n{pennies} pennies')