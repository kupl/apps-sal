def multi_table(number):
    st = str()
    for x in range(1,11):
        z = x * number
        st += '{} * {} = {}\n'.format(x,number,z)
    sti = st.strip('\n')
    return sti
