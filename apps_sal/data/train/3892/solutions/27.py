def grader(score):
    return "F" if score*10 not in range(6,11) \
      else "A" if score >= 0.9 \
      else "B" if score >= 0.8 \
      else "C" if score >= 0.7 \
      else "D" 
