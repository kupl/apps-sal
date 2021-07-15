def convert(st):    
    for x,y in [['o','u'],['a','o']]:
        st = st.replace(x,y)
    
    return st
