#to find the second largest number from given 3 number

n = int(input())
for _ in range(n):
    input_list = input().split(" ")
    input_list = [int(x) for x in input_list]
    input_list.sort()
    print(input_list[1])

