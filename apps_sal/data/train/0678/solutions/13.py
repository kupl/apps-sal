'''

          Online Python Compiler.
       Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(1, n):
        arr[i] += arr[i - 1]
    days = 0
    ppl = 1

    while ppl < n:
        ppl += arr[ppl - 1]
        days += 1

    print(days)
