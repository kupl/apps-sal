def is_inertial(arr):
    if not arr or len(arr)<2: return False
    m1=max(arr)
    m2,m_odd=max(arr[1:],key=lambda x:(1-(x%2) and x!=m1,x)),min(arr,key=lambda x:(1-x%2,x))
    return bool(m_odd%2) and not bool(m1%2) and bool(m2%2 or m_odd>m2)
