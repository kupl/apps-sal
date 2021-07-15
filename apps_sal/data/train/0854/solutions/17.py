t = int(input())
for x in range(t):
    n = int(input())
    arr = input().split()
    mySet = set(arr)
    if sorted(arr)==sorted(list(mySet)):
      print("prekrasnyy")
    else:
      print("ne krasivo")

