from statistics import mean
lst = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
d = {lst.index(i): i for i in lst}
def average_string(s):
    try:
        return d.get(int(mean([lst.index(i) for i in s.split()])),'n/a')
    except:
        return 'n/a'
