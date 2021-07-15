for _ in range(int(input())):
    string = input().rstrip()
    start=(ord(string[0])-96)*100
    sum=0
    #print(start)
    for i in range(len(string)):
        sum+=start+(ord(string[i])-97)
    print(sum%1000000007)
