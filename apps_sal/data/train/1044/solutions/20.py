# cook your dish here
def add():
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    print(sum)


for _ in range(int(input())):
    add()
