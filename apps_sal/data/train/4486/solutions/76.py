def repeat_it(string,n):
    #your code here
    return "Not a string" if type(string) is not str else string * n 
    
print(repeat_it("abc", 3))
