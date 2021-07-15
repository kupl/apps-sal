# cook your dish here
def merge_sort(arr):
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid]   
        R = arr[mid:] 
        merge_sort(L) 
        merge_sort(R) 
        i = j = k = 0
 
        while i < len(L) and j < len(R): 
            if L[i][0] < R[j][0]: 
                arr[k] = L[i] 
                i+=1
            elif L[i][0] == R[j][0]:
                if L[i][1] > R[j][1]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
for _ in range(int(input())):
    arr = []
    input()
    for i in range(int(input())):
        arr.append(list(map(int,input().split())))
    merge_sort(arr)
    d = 0
    for i in range(1,len(arr)):
        d += ((arr[i][0]-arr[i-1][0])**2 + (arr[i][1]-arr[i-1][1])**2)**0.5
    print('%.2f'%d)
