def reverseWords(s):
    words = s.split()
    reversed = ""
    index = len(words)      
    while index > 0:
        index -= 1
        reversed = reversed + " " + (words[index])
    return reversed[1:]
        

