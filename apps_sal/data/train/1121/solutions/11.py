

def CHEFJUMP(hour, minute):

 h_m = (minute * 12) / 60 * 30
 diff = (30 * minute) / 60

 hour = (((hour % 12) * 30) + diff) % 360
 A = min(abs(hour - h_m), (360 - max(hour, h_m)) + min(hour, h_m))
 
 if A != int(A):
  return A
 else:
  return int(A)



TESTCASES = int(input().strip())

for i in range(0, TESTCASES):
 
 H, M = [int(x) for x in input().strip().split(":")]
  
 print(str(CHEFJUMP(H, M)) + " degree")
  

