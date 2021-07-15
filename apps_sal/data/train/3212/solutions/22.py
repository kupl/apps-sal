import string
def generate_hashtag(s): return  '#'+''.join(string.capwords(s).split(' ')) if len(s)<=140 and len(s)!=0 else False
