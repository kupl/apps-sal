def say_hello(name):
    print(name)
    arr = [72, 101, 108, 108, 111, 44]
    return ''.join([chr(i) for i in arr])+' '+name
