import traceback;
import math;

MAX_INF = 9223372036854775807
INF = 2147483647
SEM_INF = INF // 2
MOD = int(1e9 + 7)


class HELPER:
 tmplst = []
 pntr = 0
 outPutStream = ""

 def __init__(self):
  pass

 def __next__(self):
  if self.pntr == -1 or self.pntr == len(self.tmplst):
   self.tmplst = input().split(" ")
   self.pntr = 0
  ret = self.tmplst[self.pntr]
  self.pntr += 1

  return ret

 def nextInt(self):
  return int(next(self))

 def nextFloat(self):
  return float(next(self))

 def nextLine(self):
  return input()

 def readArray(self, n):
  l = []
  for x in range(0, n):
   l.append(self.nextInt())
  return l

 def getIntArray(self, s):
  l = []
  s = s.split(" ")
  for x in range(0, len(s)):
   l.append(int(s[x]))

  return l

 # Printing Arena

 def printArray(self, a, nextLine):
  for x in a:
   sc.write("{} ".format(x))
  if nextLine:
   self.writeln()

 def writeln(self, s):
  self.outPutStream += (str(s) + "\n")

 def write(self, s):
  self.outPutStream += str(s)

 def flush(self):
  print(self.outPutStream)
  outPutStream = ""


sc = HELPER()


def writeln(s=""):
 sc.writeln(s)


def write(s):
 sc.write(s)


"""Code Starts Here"""


def getFactorList(n):
 l = [];
 p = 0
 while n % 2 == 0:
  p += 1
  n = n // 2
 l.append(int(math.pow(2,p)))

 x = 3
 while x <= math.sqrt(n):
  p = 0
  while n % x == 0:
   n = n // x
   p += 1
  if p != 0:
   l.append(int(math.pow(x,p)))
  x += 2

 if n > 2:
  l.append(n)

 return l


def getMinRecur(l, a, pos):
 if(pos == len(l)):
  return sum(a)
 ans = float('inf')
 for x in range(0,len(a)):
  a[x] *= l[pos]
  ans = min(ans,getMinRecur(l,a,pos + 1))
  a[x] //= l[pos]

 return ans


def getMinAns(l,k):
 ans = 0
 if k == len(l):
  ans = sum(l)
 elif k > len(l):
  more = k - len(l)
  ans = more + sum(l)
 else:
  arr = [1] * k
  ans = getMinRecur(l,arr,0)
 return ans


def testCase():
 k = sc.nextInt(); day = sc.nextInt()
 l = getFactorList(day)

 ans = getMinAns(l,k)
 ans = min(ans,day + k - 1)
 writeln(ans)
 pass


"""Code Ends Here"""


def main():
 t = int(input())
 # t = 1
 while t > 0:
  testCase()
  t -= 1
 sc.flush()


try:
 def __starting_point():
  main()
except:
 print("Error Occured")
 traceback.print_exc()

__starting_point()
