def mango(quantity, price):
  batch = quantity//3 
  total = (batch * 2 + quantity%3 ) * price 
  return total
