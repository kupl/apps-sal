def arithmetic(a, b, operator):
    #your code here
    words_operator = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    
    return(eval("{} {} {}".format(a,words_operator[operator],b)))
