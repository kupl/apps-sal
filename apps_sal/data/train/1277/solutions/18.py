for t in range(int(input())):
 totallossforthiscase = 0
 for i in range(int(input())):
  price , quantity , discount = map(int,input().split())
  originalprice = price
  price = price*(1 + (discount/100))
  price = price*(1 - (discount /100))
  diff = originalprice - price
  loss = diff * quantity
  totallossforthiscase +=loss
 print(totallossforthiscase)
