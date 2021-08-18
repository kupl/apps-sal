def sum_of_a_beach(beach):
    words = ["Sand", "Water", "Fish", "Sun"]
    count = 0
    for word in words:
        length = len(word)
        for i in range(len(beach)):
            if beach[i:length + i].lower() == word.lower():
                count += 1
    return count
