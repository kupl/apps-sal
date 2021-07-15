int_diff=lambda arr, n: 0 if len(arr)<2 else len([1 for i in arr[1:] if abs(i-arr[0])==n])+int_diff(arr[1:], n)
