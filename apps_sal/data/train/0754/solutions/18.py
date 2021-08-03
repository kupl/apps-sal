'''
Sample Input:
2
19
385
Sample Output:
0
1
'''
for _ in range(int(input())):
    ans = 0
    for i in str(input()):
        if i in ["2", "4", "6", "8", "0"]:
            ans = 1
            break
    print(ans)
