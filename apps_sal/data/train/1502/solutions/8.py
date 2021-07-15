# cook your dish here
t=int(input())
for _ in range(t):
    st=input().strip()
    n=int(input())
    f=1 
    arr=input().split()
    for i in arr:
        st=st.replace(i,'')
    if(len(st)==0):
        print('1')
    else:
        print('0')
