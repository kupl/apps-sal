def remove_exclamation_marks(s):
    #your code here
    return "".join(filter(lambda x:x.isalpha() or x==" " or x==",",s))
