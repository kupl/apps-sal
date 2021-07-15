import math
def graceful_tipping(bill):
  bill = bill * 1.15
  if bill < 10:
    return math.ceil(bill)
  elif 10 <= bill < 100:
    bill = math.ceil(bill)
    mul5 = [i for i in range(1,bill+5) if i % 5 ==0]
    return mul5[-1]
  elif 100 <= bill < 1000:
    bill = math.ceil(bill)
    mul50 = [i for i in range(1,bill+50) if i % 50 ==0]
    return mul50[-1] 
  elif 1000 <= bill < 10000:
    bill = math.ceil(bill)
    mul500 = [i for i in range(1,bill+500) if i % 500 ==0]
    return mul500[-1] 
  elif 10000 <= bill < 100000:
    bill = math.ceil(bill)
    mul5000 = [i for i in range(1,bill+5000) if i % 5000 ==0]
    return mul5000[-1]  
  elif 100000 <= bill < 1000000:
    bill = math.ceil(bill)
    mul50000 = [i for i in range(1,bill+50000) if i % 50000 ==0]
    return mul50000[-1] 
  elif 1000000 <= bill < 10000000:
    bill = math.ceil(bill)
    mul500000 = [i for i in range(1,bill+500000) if i % 500000 ==0]
    return mul500000[-1]  
    
    
   

