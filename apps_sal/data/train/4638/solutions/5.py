def fizz_buzz_cuckoo_clock(t):
    return ' '.join(['Cuckoo'] * (int(t[:2]) % 12 + 12 * (t[:2] in ['00', '12'])) if t[3:] == '00' else ['Cuckoo'] if t[3:] == '30' else ['Fizz'] * (int(t[3:]) % 3 == 0) + ['Buzz'] * (int(t[3:]) % 5 == 0) or ['tick'])
