#sabemos que no existe una base B>N donde el número empieze con 1 analizamos los casos 0,1 y los demás enteros
T=input() #casos a analizar
T=int(T)
for a in range(0,T):
    N=input() #número de base
    N=int(N)
    unos = 1
    if N==1:
        print('INFINITY')
    elif N==0:
        print(0)
    else:
        for b in range(3,N+1):
            a=N
            while a>=b:
                a = int(a/b)
                if a==1:
                    unos+=1
        print(unos)
