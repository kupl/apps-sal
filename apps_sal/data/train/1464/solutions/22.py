# cook your dish here
t = int(input())


def leapYear(Year):
 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  return True
 else:
  return False


for _ in range(t):
 s = input()
 a = s.split(":")
 year = int(a[0])
 m = int(a[1])
 d = int(a[2])

 if m == 2:
  if leapYear(year):
   print((29 - d) // 2 + 1)
  else:
   print((28 + 31 - d) // 2 + 1)

 if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
  print((31 - d) // 2 + 1)
 elif m == 4 or m == 6 or m == 9 or m == 11:
  print((30 + 31 - d) // 2 + 1)

