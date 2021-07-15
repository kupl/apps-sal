def conjugate(verb):
    conjugation = verb[-2:]
    
    if conjugation == "ar":
        return { verb : [verb[:-2] + "o", verb[:-2] + "as", verb[:-2] + "a", verb[:-2] + "amos", verb[:-2] + "ais", verb[:-2] + "an"] }
    elif conjugation == "er":
        return { verb : [verb[:-2] + "o", verb[:-2] + "es", verb[:-2] + "e", verb[:-2] + "emos", verb[:-2] + "eis", verb[:-2] + "en"] }
    elif conjugation == "ir":
        return { verb : [verb[:-2] + "o", verb[:-2] + "es", verb[:-2] + "e", verb[:-2] + "imos", verb[:-2] + "is", verb[:-2] + "en"] }
