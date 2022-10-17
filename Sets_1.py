items={"shirt","pasta","biryani","iron","cold drink"}
d1={}
price_list=[]
for i in range(len(items)):
    x=items.pop()
    print("Enter price for",x)
    d1[x]=int(input())

amount=0
for j in d1.values():
    price_list.append(j)
    amount+=j
    
print("*********BILL**********")
print("{:<15}{:<15}".format("ITEMS","PRICE"))
for a,b in d1.items():
    print("{:<15}{:<15}".format(a,b))
print("Total Amount= Rs.",amount)
print("Maximun Price=",max(price_list))
print("Minimum Price=",min(price_list))
print("THANKS FOR VISITING")
