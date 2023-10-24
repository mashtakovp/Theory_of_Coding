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
print(f"G:\n{G}\nH:\n{H}")

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
print("")
def right_word2(H, syndrome2, word2error):
    k = None
    d = None
    for i in range(len(H)):
        if np.array_equal(syndrome2, H[i]):
            k = i
            break
        for j in range(i + 1, len(H)):
            if np.array_equal(syndrome2, H[i] + H[j]):
                k = i
                d = j
                break
        if k is not None:
            break
    if k == None:
        print("Синдрома нет в таблице")
    else:
        word2error[k] ^= 1
        if d != None:
            word2error[d] ^= 1
    print(f"Слово: {word2error} после исправления")
    return 0
word2error = create_errors(word, G, 2)
syndrome2 = word2error@H%2
right_word2(H, syndrome2, word2error)
print("")
def right_word3(H, syndrome3, word3error):
    k = None
    d = None
    g = None
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
            if k is not None:
                break
        if k is not None:
            break
    if k == None:
        print("Синдрома нет в таблице")
    else:
        word3error[k] ^= 1
        if d is not None:
            word3error[d] ^= 1
        if g is not None:
            word3error[g] ^= 1
    print(f"Слово: {word3error} после исправления")
    return 0
word3error = create_errors(word, G, 3)
syndrome3 = word3error@H%2
right_word3(H, syndrome3, word3error)
print("")
def right_word4(H, syndrome4, word4error):
    k = None
    d = None
    g = None
    z = None
    for i in range(len(H)):
        if np.array_equal(syndrome4, H[i]):
            k = i
            break
        for j in range(i + 1, len(H)):
            if np.array_equal(syndrome4, H[i] + H[j]):
                k = i
                d = j
                break
            for e in range(j + 1, len(H)):
                if np.array_equal(syndrome4, H[i] + H[j] + H[e]):
                    k = i
                    d = j
                    g = e
                    break
                for y in range(e + 1, len(H)):
                    if np.array_equal(syndrome4, H[i] + H[j] + H[e] + H[y]):
                        k = i
                        d = j
                        g = e
                        z = y
                        break
                if k is not None:
                    break
            if k is not None:
                break
        if k is not None:
            break
    if k == None:
        print("Синдрома нет в таблице", '\n')
    else:
        word4error[k] ^= 1
        if d is not None:
            word4error[d] ^= 1
        if g is not None:
            word4error[g] ^= 1
        if z is not None:
            word4error[z] ^= 1
    print(f"Слово: {word4error} после исправления")
    return 0
word4error = create_errors(word, G, 4)
syndrome4 = word4error@H%2
right_word3(H, syndrome4, word4error)
print("")

#4.3 Написать функцию формирования порождающей и проверочных матриц кода Рида-Маллера RM(r, m) на основе параметров r и m.

def G_RM(r, m):
    if 0 < r < m:
        leftup = G_RM(r, m - 1)
        rightlow = G_RM(r - 1, m - 1)
        return np.hstack([np.vstack([leftup, np.zeros((len(rightlow), len(leftup.T)), int)]), \
                                                             np.vstack([leftup, rightlow])])
    elif r == 0:
        return np.ones((1, 2 ** m), dtype=int)
    elif r == m:
        up = G_RM(m - 1, m)
        low = np.zeros((1, 2 ** m), dtype=int)
        low[0][len(low.T) - 1] = 1
        return np.vstack([up, low])

def H_RM(i, m):
    H_k = np.array([[1, 1],
                    [1, -1]])
    left = np.kron(np.eye(2 ** (m - i), dtype=int), H_k)
    result = np.kron(left, np.eye(2 ** (i - 1), dtype=int))
    return result
#4.4. Провести исследование кода Рида-Маллера RM(1,3) для одно- и двукратных ошибок.
def research13(word, G, count):
    word_err = create_errors(word, G, count)
    for i in range(len(word_err)):
        if word_err[i] == 0:
            word_err[i] = -1

    H1 = H_RM(1, 3)
    word1 = word_err@H1
    H2 = H_RM(2, 3)
    word2 = word1@H2
    H3 = H_RM(3, 3)
    word3 = word2@H3

    max_val = -1000000000000
    max_val_pos = 0
    for j in range(len(word3)):
        if word3[j] > max_val:
            max_val = word3[j]
            max_val_pos = j

    binary = np.binary_repr(max_val_pos, 3)[::-1]
    if max_val > 0:
        binary = "1" + binary
    else:
        binary = "0" + binary
    print(f"Количество ошибок: {count}")
    print(f"Максимальное значение: {max_val}")
    print(f"Декодированное сообщение: {binary}")

print(f"Порождающая матрица Рида-Маллера (1,3)\n{G_RM(1, 3)}")
word2 = np.array([i % 2 for i in range(len(G_RM(1, 3)))])
research13(word2, G_RM(1, 3), 1)
research13(word2, G_RM(1, 3), 2)
#4.5. Провести исследование кода Рида-Маллера RM(1,4) для одно-, двух-,трёх- и четырёхкратных ошибок.
def research14(word, G, count):
    word_err = create_errors(word, G, count)
    for i in range(len(word_err)):
        if word_err[i] == 0:
            word_err[i] = -1

    H1 = H_RM(1, 4)
    word1 = word_err @ H1
    H2 = H_RM(2, 4)
    word2 = word1 @ H2
    H3 = H_RM(3, 4)
    word3 = word2 @ H3
    H4 = H_RM(4, 4)
    word4 = word3 @ H4
    
    max_val = -1000000000000
    max_val_pos = 0
    for j in range(len(word4)):
        if word4[j] > max_val:
            max_val = word4[j]
            max_val_pos = j

    binary = np.binary_repr(max_val_pos, 4)[::-1]
    if max_val > 0:
        binary = "1" + binary
    else:
        binary = "0" + binary

    print("Количество ошибок: ", count, '\n')
    print("Максимальное значение", max_val, '\n')
    print("Декодированное сообщение ", binary, '\n')

word3 = np.array([i % 2 for i in range(len(G_RM(1, 4)))])
print(f"Порождающая матрица Рида-Маллера (1,4)\n{G_RM(1, 4)}")
research14(word3, G_RM(1, 4), 1)
research14(word3, G_RM(1, 4), 2)
research14(word3, G_RM(1, 4), 3)
research14(word3, G_RM(1, 4), 4)