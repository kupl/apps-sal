def string_merge(string1, string2, letter):
    """given two words and a letter, merge one word that combines both at the first occurence of 
    the letter
    >>> "hello","world","l"
    held
    >>> "jason","samson","s"
    jasamson 
    """
    return string1[0:string1.find(letter)] + string2[string2.find(letter):]
