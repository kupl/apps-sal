def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) == float or type(x) == int:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"


'''If the input is a string then "Zach" ate the cookie. If the input is a float
or an int then "Monica" ate the cookie. If the input is anything else "the dog" ate
the cookie. 
The way to return the statement is: "Who ate the last cookie? It was (name)!'''
