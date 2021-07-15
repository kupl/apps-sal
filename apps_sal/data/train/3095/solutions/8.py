def my_add(a, b):
    try:
        a + b
    except: 
        try:
            float(a, b)
        except:
            return None
    return a + b
    # Your code here.

