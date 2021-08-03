FRACTIONS = " . : :. :: :.: S S. S: S:. S:: S:.:".split(" ")
UNITS = " I II III IV V VI VII VIII IX"      .split(" ")
TENS = " X XX XXX XL L LX LXX LXXX XC"      .split(" ")
HUNDREDS = " C CC CCC CD D DC DCC DCCC CM"      .split(" ")
THOUSANDS = " M MM MMM MMMM MMMMM"               .split(" ")


def roman_fractions(n, f=0):
    return ("NaR" if n < 0 or n > 5000 or f < 0 or f > 11
            else "N" if n + f == 0
            else THOUSANDS[n // 1000] +
            HUNDREDS  [n%1000//100] +
                        TENS      [n%100//10] +
                        UNITS     [n%10] +
            FRACTIONS [f] )
