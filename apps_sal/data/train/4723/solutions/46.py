def greet(name): 
    # your code here
    name=name.lower()
    ans='Hello '+name[0].upper()+name[1:len(name)]+'!'
    return ans
