brackets = __import__("re").compile(r"\[(.*?)\]").findall

def bracket_buster(string):
    return brackets(string) if type(string) == str else "Take a seat on the bench."
