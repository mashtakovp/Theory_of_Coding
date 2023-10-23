import numpy as np
import random

# Расширенный код Голея
B = np.array([
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]])
# 4.1 Написать функцию формирования порождающей и проверочной матриц расширенного кода Голея (24,12,8).
def G_H(B):
    k = 12
    I = np.eye(k, dtype=int)
    G = np.hstack((I, B))
    H = np.vstack((G[:, k:].T, I))
    return G, H

G, H = G_H(B)
#print(f"G:\n{G}\nH:\n{H}")

#4.2 Провести исследование расширенного кода Голея для одно-, двух-,трёх- и четырёхкратных ошибок.
word = np.array([i % 2 for i in range(len(G))])
print(f"Слово: {word}")
def create_errors(word, G, count):
    codeword = word@G%2
    print(f"Слово: {codeword} без ошибок")
    err_positions = random.sample(range(len(codeword)), count)
    wrong_codeword = codeword
    for err_position in err_positions:
        wrong_codeword[err_position] ^= 1        #xor
    print(f"Слово: {wrong_codeword} с кол-ом ошибок: {count}")
    return codeword

#errors = np.eye(len(H), dtype=int)
#S = {tuple(err @ H): err.tolist() for err in errors}
def right_word1(H, syndrome1, word1error):
    k = None
    for i in range(len(H)):
        if np.array_equal(syndrome1, H[i]):
            k = i
    if k == None:
        print("Синдрома нет в таблице")
    else:
        word1error[k] ^= 1
        print(f"Слово: {word1error} после исправления")
    return 0

word1error = create_errors(word, G, 1)
syndrome1 = word1error@H%2
right_word1(H, syndrome1, word1error)
#word1error@H%2
print("")
def right_word2(H, syndrome2, word2error):
    k = -1
    d = -1
    for i in range(len(H)):
        if np.array_equal(syndrome2, H[i]):
            k = i
            break
        for j in range(i + 1, len(H)):
            if np.array_equal(syndrome2, H[i] + H[j]):
                k = i
                d = j
                break
        if k >= 0:
            break
    if k == -1:
        print("Синдрома нет в таблице")
    else:
        word2error[k] ^= 1
        if d != -1:
            word2error[d] ^= 1
    print(f"Слово: {word2error} после исправления")
    return 0
word2error = create_errors(word, G, 2)
syndrome2 = word2error@H%2
right_word2(H, syndrome2, word2error)
print("")
def right_word3(H, syndrome3, word3error):
    k = -1
    d = -1
    g = -1
    for i in range(len(H)):
        if np.array_equal(syndrome3, H[i]):
            k = i
            break
        for j in range(i + 1, len(H)):
            if np.array_equal(syndrome3, H[i] + H[j]):
                k = i
                d = j
                break
            for e in range(j + 1, len(H)):
                if np.array_equal(syndrome3, H[i] + H[j] + H[e]):
                    k = i
                    d = j
                    g = e
                    break
            if k >= 0:
                break
        if k >= 0:
            break
    if k == -1:
        print("Такого синдрома нет в матрице синдромов", '\n')
    else:
        word3error[k] ^= 1
        if d != -1:
            word3error[d] ^= 1
        if g != -1:
            word3error[g] ^= 1
    print(f"Слово: {word3error} после исправления")
    return 0

word3error = create_errors(word, G, 3)
syndrome3 = word3error@H%2
right_word3(H, syndrome3, word3error)




"""
word2error = create_errors(word, G, 2)
syndrome2 = word2error@H%2
word3error = create_errors(word, G, 3)
syndrome3 = word3error@H%2
"""

