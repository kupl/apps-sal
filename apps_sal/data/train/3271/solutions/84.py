def arr(*n): 
    try:
        return [i for i in range(n[0]) if n !=0]
    except IndexError: 
        return []
