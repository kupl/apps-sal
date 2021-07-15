def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise 'Error!'
    else:
        count = 0
        for i, x in enumerate(correct):
            for j, y in enumerate(guess):
                if i == j and x == y:
                    count += 1
        return count
    

