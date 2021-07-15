def max_sum(arr,ranges): 
    st=[]
    for i in ranges:
        p=0
        for j in range(i[0],i[1]+1):
            p+=arr[j]
        st.append(p)
    return max(st)
