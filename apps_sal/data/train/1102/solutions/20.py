# cook your dish here

t = int(input())
#d = {"1":1, "2":3, "3":3, "4":3, "5":3, "6":3, "7":4, "8":3, "9":4, "0":1}
for rep in range(t):
 p = 1
 s = input()
 l = list(s)
 for i in l:
  if i == "7" or i == "9":
   p = (p * 4) % 1000000007
  elif i in ["2","3","4","5","6","8"]:
   p = (p * 3) % 1000000007
 print(p)
