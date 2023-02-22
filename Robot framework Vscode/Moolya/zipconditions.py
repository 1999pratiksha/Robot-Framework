costprice=[100,150,200,300]
sellingprice=[50,60,80,70]
sell=zip(costprice,sellingprice)

for x,y in sell:
    if x<y:
        print("profit of:",y-x)
    elif x>y:
        print("loss of:",x-y)
    else:
        print("no profit no loss")