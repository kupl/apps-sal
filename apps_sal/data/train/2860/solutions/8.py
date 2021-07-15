def isomorph(a, b):
    if len(a)!=len(b):
        return False
    st={}
    for i in range(len(a)):
        if a[i] not in list(st.keys()) and b[i]  in list(st.values()):
            return False
        if a[i] not in list(st.keys()) and b[i] not in list(st.values()):
            st[a[i]]=b[i]
        elif st[a[i]]!=b[i] :#or a[i] not in st.keys() and b[i]  in st.values():
             return False
    return True
  # Happy coding!

