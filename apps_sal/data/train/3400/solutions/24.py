def even_numbers(arr,n):
    arr=arr[::-1]
    ans=[]
    for x in arr:
        if x%2==0:
            ans.append(x)
            if len(ans)==n:
                return ans[::-1]
