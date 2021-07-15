def calculate_grade(scores):
    score = (sum(scores)/len(scores))/100
    grades = { 0.6:"D",0.7:"C",0.8:"B",0.9:"A"}
    return grades[round(score,1)] if score > 0.6 else "F"

