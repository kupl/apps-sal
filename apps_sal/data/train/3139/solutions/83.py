def index(array, N):
    res = 0
    uzunluk = len(array)
    if N>=uzunluk:
        return -1
    
    ussuAlinacakSayi = array[N]
    return ussuAlinacakSayi**N
