def correct_polish_letters(st): 
    st2=''
    arr=[]
    for i in st:
        arr.append(i)
    letters=[['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż'], ['a', 'c', 'e', 'l', 'n', 'o', 's', 'z', 'z']]
    for i in range(len(arr)):
        for j in range(len(letters[0])):
            if arr[i]==letters[0][j]:
                arr[i]=letters[1][j]
    for i in arr:
        st2+=i
    return st2
