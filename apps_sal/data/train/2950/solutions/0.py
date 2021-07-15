def solve(arr):
    return sum( y-x == z-y for i,x in enumerate(arr[:-2])
                           for j,y in enumerate(arr[i+1:-1])
                           for _,z in enumerate(arr[j+1:]))
