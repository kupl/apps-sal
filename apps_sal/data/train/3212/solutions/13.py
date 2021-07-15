def generate_hashtag(s):
    s='#'+s.title().replace(' ','')
    return s if s!='#' and len(s)<=140 else False
