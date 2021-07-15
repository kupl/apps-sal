def unusual_sort(array):
    def k(x):
        if type(x) == int:
            return ord('z') + 1 + 10*x;
        elif x.isdigit():
            return ord('z') + 1 + 10*int(x) + 1;
        else:
            return ord(x);
    
    return sorted(array, key=k);
