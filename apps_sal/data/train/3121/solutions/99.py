def solve(arr):
    for i in range(0,len(arr)):
        num = arr[i]
        reversenumber = -num
        found = False
        for index in range(0, len(arr)):
            if i == index :
                continue
            if reversenumber == arr[index]:
                found = True
                break
        if found == False:
            return num 
