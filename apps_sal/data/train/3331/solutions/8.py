def solve(arr,n):
    eaten = []
    dog = []
    for i in range(len(arr)):
        if arr[i] == "D":
            for j in range(max(0, i-n), min(1+i+n, len(arr))):
                if arr[j] == "C" and j not in eaten and i not in dog:
                    dog.append(i)
                    eaten.append(j)
    return len(eaten)
