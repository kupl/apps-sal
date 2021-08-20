def reverse(st):
    w = st.split()
    w.reverse()
    return ' '.join(w)


stri = 'Hello World'
print(reverse(stri))
