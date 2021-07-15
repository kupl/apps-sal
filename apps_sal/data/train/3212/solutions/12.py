def generate_hashtag(s):
    #your code here
    
    
    return "#{}".format(s.title().replace(" ", "")) if len(s) in range(1,141) else False
