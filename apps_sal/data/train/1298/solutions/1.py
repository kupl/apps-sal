t = eval(input())
while t > 0:
    n = eval(input())
    input_arr = input().split(' ')
    counter = 0
    for i in range(1, n + 1):
        if(int(input_arr[0]) < int(input_arr[i])):
            counter += 1
    print(counter)
    t -= 1
