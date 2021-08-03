geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]


def goose_filter(birds: list) -> list:
    answer: list = []
    for bird in birds:
        if not bird in geese:
            answer.append(bird)
    return answer
