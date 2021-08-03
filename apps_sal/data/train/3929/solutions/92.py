def reverse(st):
    print(st)
#     for x in range(len(st)-1):
#         if st[x]==' ' and st[x+1]==' ':
#             st[x]='!@#'
#     st=st.replace('!@#','')
    st = st.split('  ')
    st = ' '.join(st)
    st = st.split('  ')
    st = ' '.join(st)
    st = st.strip()
    st = (st.split(' '))

    st.reverse()
    # Your Code Here
    return ' '.join(map(str, st))
