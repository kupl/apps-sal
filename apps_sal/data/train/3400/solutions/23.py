def even_numbers(arr,n):
    even = [a for a in arr if not a%2]
    return even[len(even)-n::]
