# takes a function or lambda and a list of arguments to be passed to that function or lambda
# returns the result of calling the function or lambda on those arguments
def spread(func, args):
    return func(*args)
