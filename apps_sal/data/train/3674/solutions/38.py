def add_binary(a,b):
    results_dec =  a + b
    results_bin = bin(results_dec)
    results_bin = results_bin[2:len(results_bin)]
    return results_bin

