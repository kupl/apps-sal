def words_to_object(s):
    if s:
        s=s.split(" ")
        return "["+', '.join("{"+"name : '{}', id : '{}'".format(s[i],s[i+1])+"}" for i in range(0,len(s),2))+"]"
    else:
        return '[]'
