# cook your dish here

for _ in range(int(input())):
 friends = int(input())
 candies = list(map(int,input().split()))
 if (sum(candies) % friends == 0):
  print("Yes")
 else:
  print("No")
