def reverse(st):
    to_list = st.split(' ')
    to_list.reverse()
    return ' '.join(to_list).strip().replace('  ', ' ').replace('  ', ' ')
