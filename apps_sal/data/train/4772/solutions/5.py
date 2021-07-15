def name_score(name):
    answer=0
    for character in name:
        character=character.upper()
        for key,value in alpha.items():
            if character in key:
                answer+=value
                break
    return {name:answer}
