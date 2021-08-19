import sys


def main():
    s = sys.stdin.readline
    t = int(s())
    for i in range(t):
        name = s().strip().lower()
        if ' ' in name:
            name = name.replace(' ', '')
        crush = s().strip().lower()
        if ' ' in crush:
            crush = crush.replace(' ', '')
        namecounter = {}
        crushcounter = {}
        for letter in name:
            if letter in namecounter:
                namecounter[letter] += 1
            else:
                namecounter[letter] = 1
        for letter in crush:
            if letter in crushcounter:
                crushcounter[letter] += 1
            else:
                crushcounter[letter] = 1
        counter = 0
        already = []
        for letter in name:
            if letter in crush:
                if letter not in already:
                    if namecounter[letter] == crushcounter[letter]:
                        already.append(letter)
                        continue
                    else:
                        counter += abs(namecounter[letter] - crushcounter[letter])
            else:
                counter += 1
            already.append(letter)
        for letter in crush:
            if letter not in already:
                counter += 1
        values = {1: 'FRIENDS', 2: 'LOVE', 3: 'ADORE', 4: 'MARRIAGE', 5: 'ENEMIES', 6: 'SISTER'}
        result = 0
        for i in range(1, 6 + 1):
            result = (result + counter) % i
        print(values[result + 1])


def __starting_point():
    main()


__starting_point()
