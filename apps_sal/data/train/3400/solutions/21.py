def even_numbers(arr,n):  
    return [number for number in arr if number%2==0][::-1][:n][::-1]
