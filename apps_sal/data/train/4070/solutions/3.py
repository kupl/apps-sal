def magic_sum(arr):
    return sum(i for i in arr if (i%2==1 and '3' in str(i))) if arr else 0
