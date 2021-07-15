for _ in range(int(input())):
    s = input()
    st = []
    temp,count = 0,0
    for i in s:
        if i =='<':
            st.append('<')
        else:
            if len(st)==0:
                break
            else:
                st.pop()
                if len(st)==0:
                    count+=2 + temp
                    temp = 0
                else:
                    temp+=2
    print(count)
