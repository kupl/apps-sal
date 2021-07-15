def alan_annoying_kid(s):
    lst = s.split()
    isNegative  = lst[2] == "didn't"
    verb = lst[2 + isNegative]
    cplt = ' '.join(lst[3 + isNegative:])
    return ("I don't think you didn't {} {} today, I think you did {} it!".format(verb, cplt[:-1], verb)
                if isNegative else
            "I don't think you {} {} today, I think you didn't {} at all!".format(verb, cplt[:-1], verb[:-2]))
