t = int(input())
while t > 0:
    n = input()
    ls = input()
    ls = ls.split()
    st = ''
    for i in ls:
        if i == '0':
            st += ' '
        else:
            st += 'x'
    if len(st.strip()) == 0:
        print(1)
    else:
        print(len(st.strip()))
    t -= 1
