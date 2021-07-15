def words_to_marks(s):
    sum=0
    for i in s:
        a=ord(i)
        a=a-96
        sum=sum+a
    return sum
