T = int(input())
for i in range(T):
  string = input().lower()
  pos = string.find('abc')
  while pos != -1:
    string = string.replace("abc","")
    pos = string.find('abc')
  print(string)# cook your dish here

