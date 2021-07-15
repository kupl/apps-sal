def main():
 for _ in range(int(input())):
  rows,column = map(int,input().split())
  arr = []
  for i in range(rows):
   arr.append(list(input()))
  string = input()
  last = string[-1]
  operation = Find(string,last)
  for i in string:
   if i == "L":
    arr = Left(arr)
   if i == "R":
    arr = Right(arr)
   if i == "U":
    arr = Transpose(arr)
    arr = Left(arr)
    arr = Transpose(arr)
   if i == "D":
    arr = Transpose(arr)
    arr = Right(arr)
    arr = Transpose(arr)
  for i in arr:
   print(i)
def Left(arr):
 for i in range(len(arr)):
  ans = arr[i].count("1")
  arr[i] = "1"*ans + (len(arr[i]) - ans)*"0"
 return arr
def Right(arr):
 for i in range(len(arr)):
  ans = arr[i].count("1")
  arr[i] = (len(arr[i]) - ans)*"0"+"1"*ans
 return arr
def Transpose(arr):
 ansss = []
 ans = list(map(list, zip(*arr)))
 for i in ans:
  ass = i
  hello = ""
  for j in ass:
   hello += j
  ansss.append(hello)
 return ansss 
def Find(string,last):
 for i in string[-2::-1]: 
  if last == "L":
   if i in ["D","U"]:
    last = i + last
    break
  if last == "R":
   if i in ["D","U"]:
    last = i + last
    break
  if last == "D":
   if i in ["L","R"]:
    last = i + last
    break
  if last == "U":
   if i in ["L","R"]:
    last = i + last
    break
 return last
 
def __starting_point():
 main()
__starting_point()
