def super_size(n):
    size_str = ''
    size_list = [int(i) for i in str(n)]
    for _ in range(len(size_list)):
        i = max(size_list)
        size_str+=str(i)
        size_list.remove(i)
    return int(size_str)
        

