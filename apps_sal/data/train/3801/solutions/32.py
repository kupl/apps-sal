def words_to_marks(s):
    from string import ascii_lowercase
    answer = 0    
    for element in s:
        answer += ascii_lowercase.index(element) + 1
    return answer    
