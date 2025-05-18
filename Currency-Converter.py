with open('currencyData.txt') as f:
    data = f.readlines()

currencyDict={}
for line in data:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]
amount=float(input("Enter the amount you want to convert:"))
print("Available Options:\n")
[print(item) for item in currencyDict.keys()]
print("-----------------------------------------------------")
currency=input("Please select one of the options below:\n")
if currency not in currencyDict:
    print("Enter the valid currency.")
else:
    print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency} ")