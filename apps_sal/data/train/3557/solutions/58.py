def odd_count(n):
    even_list = range(0, n + 1)[0%2::2] 
    return len(even_list) - 1
