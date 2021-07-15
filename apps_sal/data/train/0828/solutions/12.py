# cook your dish here
try:
    for _ in range(int(input())):
        N = int(input())
        Log = input().split()
        if '0' in Log:
            print((100*(N-Log.index('0')))+Log.count('0')*1000)
        else:
            print(Log.count('0')*1000)
except:
    pass
