import sys
from datetime import date

def main():
 s = sys.stdin.readline
 dateis = list(map(int, s().strip().split()))
 day = dateis[0]
 month = dateis[1]
 year = dateis[2]
 ans = date(year, month, day).weekday()
 if ans == 0:
  print("Monday")
 elif ans == 1:
  print("Tuesday")
 elif ans == 2:
  print("Wednesday")
 elif ans == 3:
  print("Thursday")
 elif ans == 4:
  print("Friday")
 elif ans == 5:
  print("Saturday")
 else:
  print("Sunday")

def __starting_point():
 main()
 

__starting_point()
