from sys import *


def main():

    nbre1 = int(stdin.readline().strip())
    nbre2 = int(stdin.readline().strip())
    if nbre1 > nbre2:
        difference = nbre1 - nbre2
        stdout.write(str(difference))
    else:
        somme = nbre1 + nbre2
        stdout.write(str(somme))


def __starting_point():
    main()


__starting_point()
