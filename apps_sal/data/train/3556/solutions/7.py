def diamonds_and_toads(sentence, fairy):
    jewels = ["ruby", "crystal"] if fairy == "good" else ["python", "squirrel"]   
    return {j: sentence.count(j[0]) + 2 * sentence.count(j[0].upper()) for j in jewels}
