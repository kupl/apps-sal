def to_dec(binary):
    sum = 0
    binary = binary[::-1]
    for (index, bit) in enumerate(binary):
        sum += int(bit) and (-2) ** index or 0
    return sum


def test_to_dec():
    assert to_dec('00000') == 0
    assert to_dec('00001') == 1
    assert to_dec('00010') == -2
    assert to_dec('00011') == -1
    assert to_dec('00100') == 4
    assert to_dec('00101') == 5
    assert to_dec('00110') == 2
    assert to_dec('00111') == 3
    assert to_dec('01000') == -8
    assert to_dec('01001') == -7
    assert to_dec('01010') == -10
    assert to_dec('10000') == 16
    assert to_dec('10001') == 17
    assert to_dec('10010') == 14
    assert to_dec('11000') == 8
    assert to_dec('11001') == 9
    assert to_dec('11010') == 6
    assert to_dec('1001101') == 61
    assert to_dec('0111111') == -21


BINARIES = dict([(to_dec(binary[2:]), binary[2:]) for binary in map(bin, range(2 ** 15))])


def to_binary(decimal):
    return BINARIES[int(decimal)]


def test_to_binary():
    assert to_binary(to_dec('00000')) == '0'
    assert to_binary(to_dec('00001')) == '1'
    assert to_binary(to_dec('00010')) == '10'
    assert to_binary(to_dec('00011')) == '11'
    assert to_binary(to_dec('00100')) == '100'
    assert to_binary(to_dec('00101')) == '101'
    assert to_binary(to_dec('00110')) == '110'
    assert to_binary(to_dec('00111')) == '111'
    assert to_binary(to_dec('01000')) == '1000'
    assert to_binary(to_dec('01001')) == '1001'
    assert to_binary(to_dec('01010')) == '1010'
    assert to_binary(to_dec('10000')) == '10000'
    assert to_binary(to_dec('10001')) == '10001'
    assert to_binary(to_dec('10010')) == '10010'
    assert to_binary(to_dec('11000')) == '11000'
    assert to_binary(to_dec('11001')) == '11001'
    assert to_binary(to_dec('11010')) == '11010'
    assert to_binary(to_dec('1001101')) == '1001101'
    assert to_binary(to_dec('0111111')) == '111111'


def skrzat(base, number):
    basename = base == 'b' and 'binary' or 'decimal'
    result = base == 'b' and to_dec(number) or to_binary(number)
    return 'From {0}: {1} is {2}'.format(basename, number, result)


def test_skrzat():
    assert skrzat('b', '10001011') == 'From binary: 10001011 is -137'
    assert skrzat('b', '110011001') == 'From binary: 110011001 is 137'
    assert skrzat('b', '1001101') == 'From binary: 1001101 is 61'
    assert skrzat('b', '0111111') == 'From binary: 0111111 is -21'
    assert skrzat('d', 0) == 'From decimal: 0 is 0'
    assert skrzat('d', -137) == 'From decimal: -137 is 10001011'
    assert skrzat('d', 137) == 'From decimal: 137 is 110011001'
