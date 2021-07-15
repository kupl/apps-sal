def mango(quantity, price):
    print(quantity, price)
    if not quantity%3==2:
      return price*(quantity*2//3)+price*(quantity%3) 
    else:
      return price*(quantity*2//3)+price*(quantity%3)/2
