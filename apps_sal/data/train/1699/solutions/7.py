# Professor Chambouliard hast just discovered a new type of magnet material.
# He put particles of this material in a box made of small boxes arranged
# in K rows and N columns as a kind of 2D matrix K x N where K and N
# are postive integers. He thinks that his calculations show that
# the force exerted by the particle in the small box (k, n) is:
# https://www.codecogs.com/latex/eqneditor.php?latex=%5Cbg_green&space;v(k,&space;n)&space;=&space;%5Cfrac%7B1%7D%7Bk(n+1)%5E%7B2k%7D%7D
# The total force exerted by the first row with k = 1 is:
# https://www.codecogs.com/latex/eqneditor.php?latex=%5Cbg_green&space;u(1,&space;N)&space;=&space;%5Csum_%7Bn=1%7D%5E%7Bn=N%7Dv(1,&space;n)&space;=&space;%5Cfrac%7B1%7D%7B1.2%5E2%7D&space;+&space;%5Cfrac%7B1%7D%7B1.3%5E2%7D+...+%5Cfrac%7B1%7D%7B1.(N+1)%5E2%7D
# We can go on with k = 2 and then k = 3 etc ... and consider:
# https://www.codecogs.com/latex/eqneditor.php?latex=%5Cbg_green&space;S(K,&space;N)&space;=&space;%5Csum_%7Bk=1%7D%5E%7Bk=K%7Du(k,&space;N)&space;=&space;%5Csum_%7Bk=1%7D%5E%7Bk=K%7D(%5Csum_%7Bn=1%7D%5E%7Bn=N%7Dv(k,&space;n))&space;%5Crightarrow&space;(doubles(maxk,&space;maxn))
# Task: To help Professor Chambouliard can we calculate the function
# doubles that will take as parameter maxk and maxn such that
# doubles(maxk, maxn) = S(maxk, maxn)? Experiences seems to show that
# this could be something around 0.7 when maxk and maxn are big enough.
# Examples: doubles(1, 3)  => 0.4236111111111111;
# doubles(1, 10) => 0.5580321939764581; doubles(10, 100) => 0.6832948559787737
# Notes: In u(1, N) the dot is the multiplication operator.
# Don't truncate or round: Have a look in "RUN EXAMPLES" at "assertFuzzyEquals".

def v(k, n):
    return 1 / (k * ((n + 1)**(2 * k)))


def u(k, N):
    u_res = 0
    for n in range(0, N):
        u_res += v(k, n + 1)
    return u_res


def S(K, N):
    S_res = 0
    for k in range(0, K):
        S_res += u(k + 1, N)
    return S_res


def doubles(maxk, maxn):
    return S(maxk, maxn)
