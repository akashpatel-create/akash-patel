costprice=float(input("enter cost price:"))
sellprice=float(input("enter sell price:"))
profit=sellprice-costprice
newsellingprice=1.05*profit+costprice
print("profit from sell=",profit)
print(" to increase 5% profit the newsellingprice should be=",newsellingprice)