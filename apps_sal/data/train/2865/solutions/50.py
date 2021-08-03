def solution(string):
    # checks if it one char or less and returns the value if so
    if (len(string) <= 1):
        return string
    # reverse the string using a slide statement that starts at the last element to the first and iterates -1
    else:
        string = string[::-1]
        return string
