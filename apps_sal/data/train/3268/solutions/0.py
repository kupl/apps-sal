import re

def words_to_object(s):
    return "[" + re.sub("([^ ]+) ([^ ]+)", r"{name : '\1', id : '\2'},", s).strip(',') + "]"
