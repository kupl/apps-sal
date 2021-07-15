def reverse(st):
    ans = [i for i in st.split(' ')  if i != '']
    print(ans)
    return ' '.join(ans[::-1])

