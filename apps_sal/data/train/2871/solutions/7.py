def starts_with(st, prefix): 
    if len(prefix) == 0:
        return True
    elif len(prefix) > len(st):
        return False
    else:
        return st.startswith(prefix)
