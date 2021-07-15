# cook your dish here
def binarySearch (arr, l, r, x):


    if r >= l:

        mid = l + (r - l)//2


        if arr[mid] == x:
            return mid


        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        if l<len(arr):
            return l
        else:
            return -1

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    posn = []
    for i in range(len(s)):
        if s[i] == 'b':
            posn.append(i)
    # print(posn)
    tot = 0
    for i in range(n):
        if posn == []:
            break
        else:
            if s[i] == 'a':
                z = binarySearch(posn,0,len(posn)-1,i)

                if z!=-1 and posn[z]<len(s):

                    # print(posn[z])
                    if s[posn[z]] == 'b':
                        z+=1
                        tot+=len(posn)-z+1
    tot*=k
    k1 = s.count('a')
    k2 = s.count('b')
    # k1*=(k-1)
    tot+=((k1*k2)*(k-1)*k)//2
    print(tot)




