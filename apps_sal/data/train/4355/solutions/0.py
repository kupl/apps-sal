from math import floor, exp
    
def ex_euler(n):
    # fct to study
    F = lambda t,y : 2 - exp(-4 * t) - 2 * y
    # initial conditions
    t0 = 0; y0 = 1; # pt A0
    T = 1; 
    # variables
    h = T / float(n); X = [t0]; Y = [y0]; Z = []; R = []
    # points A1 ... An
    for k in range(0, n):
        X.append((k + 1) * h)
        Y.append(Y[k] + h * F(X[k],Y[k]))
    # pts on the exact curve
    for k in range(0, n + 1):
        # exact solution
        Z.append(1 + 0.5 * exp(-4 * X[k]) - 0.5 * exp(-2 * X[k]))
        # relative error
        R.append(abs(Y[k] - Z[k]) / float(Z[k]))
    return floor((sum(R) / float(n + 1)) * 1e6) / 1e6 
