number_of_testcases = int(input())

def solve(string):
    n = len(string)
    for i in range(n-1,-1,-1):
        print(string[i],end="")
    print()
    
for i in range(0,number_of_testcases):
    input_string = input()
    solve(input_string)
