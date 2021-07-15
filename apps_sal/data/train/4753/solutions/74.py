geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    answer = []
    for bird in birds:
        if bird in geese:
            continue
        answer.append(bird)     
    return answer
