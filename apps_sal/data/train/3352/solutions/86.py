def find_longest(arr):
    arr=[str(i) for i in arr]
    m_len=lambda x:len(x)
    return int(max(arr,key=m_len))
