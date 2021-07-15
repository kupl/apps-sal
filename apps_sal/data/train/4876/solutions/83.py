def hello(name='World'):
    if len(name)==0:
        return "Hello, World!"
    retval = ''
    for i in range(len(name)):
        if i==0:
            retval += name[i].upper()

        else:
            retval += name[i].lower()
    return f"Hello, {retval}!"
