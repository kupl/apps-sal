def is_palindrome(s):
    s = s.lower()  # making all characters lowercase
    _list = list(s)  # saving the text from the string s in a list
    _list.reverse()  # reversing the list
    str = ""  # declaring some string variable
    for i in _list:
        str += i  # adding every item in our list in the string variable
    return str == s  # comaparing the origianl string ot the reverset string
    # this will automaticly return true or false
