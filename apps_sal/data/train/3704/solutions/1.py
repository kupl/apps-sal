import re


def solve_for_x(equation):
    (left, right) = equation.split('=')
    answer = False
    TrialAndErrorRipMs = -1000
    while answer == False:
        FinalLeft = re.sub('x', str(TrialAndErrorRipMs), left)
        FinalRight = re.sub('x', str(TrialAndErrorRipMs), right)
        if eval(FinalLeft) == eval(FinalRight):
            return TrialAndErrorRipMs
        TrialAndErrorRipMs += 1
