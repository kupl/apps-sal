def scf(arr):
    return next((i for i in range(2,min(arr)+1) if all(v%i==0 for v in arr)),1) if arr else 1
