def no_space(x):
    a = ''
    for i in x:
        if i != ' ':
            a += i
    return a


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
