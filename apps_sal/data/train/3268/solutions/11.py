def words_to_object(s):
    s=s.split()
    return str([{'name': s[i], 'id': s[i+1]} for i in range(0,len(s),2)]).replace("'name'","name ").replace("'id'","id ")
