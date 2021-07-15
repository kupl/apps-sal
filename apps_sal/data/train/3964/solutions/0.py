def rank_of_element(arr,i):
    return sum(x <= arr[i] if n < i else x < arr[i] for n,x in enumerate(arr))
