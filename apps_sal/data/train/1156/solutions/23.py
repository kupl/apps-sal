List = []
n=int(input())
for i in range(0,n):
    a = int(input())
    List.append(a)
for element in List:
    if element <= 9:
        print("Thanks for helping Chef!")
    else:
        print("-1")
