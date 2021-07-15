def palindrome(num):
    return "Not valid" if type(num) != int or num < 0 else bool(__import__("re").search(r'(\d).?\1', str(num)))
