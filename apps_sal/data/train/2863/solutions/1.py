def alan_annoying_kid(sentence):
    action = sentence.split(None, 2)[-1].rstrip('.')
    if "didn't" in sentence:
        (verb, did, it) = (action.split(None, 2)[1], 'did', 'it')
    else:
        (verb, did, it) = (action.split(None, 1)[0][:-2], "didn't", 'at all')
    return "I don't think you {} today, I think you {} {} {}!".format(action, did, verb, it)
