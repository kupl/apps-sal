def check_exam(answer_sheet,test):
    score = 0
    for correct, answer in zip(answer_sheet, test):
        if not answer:
            continue
        score += 4 if correct == answer else -1
    return max(0, score)
