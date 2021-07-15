def alan_annoying_kid(sentence):
    if "didn't" in sentence:
        verb, subject = sentence[15:-1].split(" ", 1)
        return "I don't think you didn't %s %s today, I think you did %s it!" % (verb, subject, verb)

    verb, subject = sentence[8:-1].split(" ", 1)
    return "I don't think you %s %s today, I think you didn't %s at all!" % (verb, subject, verb[:-2])
