"""by Zakhar M."""
import re
import numpy as np
from math import gcd


ALPHABET = {chr(letters): letters - 65 for letters in range(65, 91)}
REVERSE_ALPHABET = {number_symbol: symbol for symbol, number_symbol in list(ALPHABET.items())}


def checking_key_for_validity(matrix_key, length_alphabet):
    determinant = np.linalg.det(matrix_key)
    nod_determinant_and_length_alphabet = gcd(int(round(determinant)), length_alphabet)

    if nod_determinant_and_length_alphabet == 1 and nod_determinant_and_length_alphabet != 0:
        return True
    return False


def get_matrix_key(key, length_block=2):
    tmp_list = list()
    matrix_key = list()
    length_key = len(key)

    if length_key % 2 != 0:
        return ''

    for symbol in key:
        number_symbol_in_alphabet = ALPHABET[symbol]
        tmp_list.append(number_symbol_in_alphabet)
        length_tmp_list = len(tmp_list)

        if length_tmp_list != length_block:
            continue

        matrix_key.append(tmp_list)
        tmp_list = list()

    return matrix_key


def get_matrix_open_text(open_text, length_blocks=2):
    tmp_list = list()
    matrix_open_text = list()
    pattern_only_letters = re.compile(r'[^a-zA-Z]*')
    prepared_open_text = pattern_only_letters.sub('', open_text).upper()
    length_prepared_open_text = len(prepared_open_text)

    if length_prepared_open_text % 2 != 0:
        prepared_open_text += 'Z'

    for symbol in prepared_open_text:
        number_symbol_in_alphabet = ALPHABET[symbol]
        tmp_list.append(number_symbol_in_alphabet)
        length_tmp_list = len(tmp_list)

        if length_tmp_list != length_blocks:
            continue

        matrix_open_text.append(tmp_list)
        tmp_list = list()
        
    return matrix_open_text


def smart_mul_matrix(matrix_1, matrix_2):
    result_matrix = list()
    
    for i in range(len(matrix_1)):
        tmp_sum = 0
        
        for j in range(len(matrix_2)):
            tmp_sum += (matrix_1[i][j] * matrix_2[j])
        result_matrix.append(tmp_sum % 26)
        
    return result_matrix

def encrypt(open_text, key):
    cipher_text = ''
    length_alphabet = len(ALPHABET)
    matrix_cipher_text = list()
    
    pattern_only_letters = re.compile(r'[^a-zA-Z]*')
    prepared_key_text = pattern_only_letters.sub('', key).upper()
    matrix_key = get_matrix_key(prepared_key_text)
    
    matrix_open_text = get_matrix_open_text(open_text)
    
    for current_list_open_text in matrix_open_text:
        matrix_multiplication = smart_mul_matrix(matrix_key, current_list_open_text)
        matrix_cipher_text.append(matrix_multiplication)
        
    for list_cipher_text in matrix_cipher_text:
        for number_cipher_text in list_cipher_text:
            cipher_text += REVERSE_ALPHABET[number_cipher_text]
    return cipher_text


