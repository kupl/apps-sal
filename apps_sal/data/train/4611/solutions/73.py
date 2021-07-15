def animals(heads, legs):
    return (2*heads-legs//2,legs//2-heads) if legs%2==0 and legs<= heads*4 and legs >= heads*2 else 'No solutions'
