def reverse(st):
    # Your Code Here
    string=st.split()
    string.reverse()
    ans=''
    for i in string:
        ans=ans+i+' '
    return ans[:len(ans)-1]
