import numpy as np


n = 7
k = 4
# 2.1
I_k = np.eye(k, dtype=int)
X = np.array([[1, 1, 0], [0, 1, 1],
              [1, 1, 1], [1, 0, 1]], dtype=int)

G = np.hstack([I_k, X])
print(f"G:\n{G}")
# 2.2
I_nk = np.eye(n - k, dtype=int)
H = np.vstack([X, I_nk])
print(f"H:\n{H}")
# 2.3
errors = np.eye(len(H), dtype=int)
syndromes = {tuple(err @ H): err.tolist() for err in errors}
print(f"Table of syndromes:\n{syndromes}")
# 2.4
word = np.array([1, 0, 1, 0])
right_word = word @ G % 2
print(f"Right word: {right_word}")
wrong_word = right_word.copy()
wrong_word[-3] = (wrong_word[-3] + 1) % 2
print(f"Word with 1 error: {wrong_word}")
where_the_error = syndromes[tuple(wrong_word @ H % 2)]
print(f"Where's the error:{where_the_error}")
print(f"Сorrected word:{(wrong_word + where_the_error) % 2}")
# 2.5
print(f"Right word: {right_word}")
wrong_word[-4] = (wrong_word[-4] + 1) % 2
print(f"Word with 2 errors: {wrong_word}")
print(f"Сorrected(not) word:{(wrong_word + where_the_error) % 2}")

# 2.6
X_2 = np.array([[0, 1, 1, 1, 1, 0, 1, 0, 0],
                [1, 0, 0, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 1, 1, 1, 1, 0, 0]])

I_k2 = np.eye(len(X_2), dtype=int)
G_2 = np.hstack([I_k2, X_2])
print(f"New G:\n{G_2}")
# 2.7
I_nk2 = np.eye(len(X_2.T), dtype=int)
H_2 = np.vstack([X_2, I_nk2])
print(f"New H:\n{H_2}")
# 2.8
errors_2 = np.eye(len(H_2), dtype=int)
syndromes_2 = {tuple(err @ H_2): err.tolist() for err in errors_2}
combinations = [(i, j) for i in range(len(H_2)) for j in range(i + 1, len(H_2))]

for x in combinations:
    error_2 = np.zeros(len(H_2), dtype=int)
    for i in x:
        error_2[i] = 1
    syndromes_2[tuple((error_2 @ H_2) % 2)] = error_2
print(syndromes_2)
# 2.9
right_word2 = word @ G_2 % 2
print(f"Right word:\n{right_word2}")
wrong_word2 = right_word2.copy()
wrong_word2[0] = (wrong_word2[0] + 1) % 2
print(f"Word with 1 error:\n{wrong_word2}")
where_the_error2 = syndromes_2[tuple(wrong_word2 @ H_2 % 2)]
#print(f"Where's the error:\n{where_the_error2}")
print(f"Сorrected word:\n{(wrong_word2 + where_the_error2) % 2}")
# 2.10                        #две ошибки
wrong_word2[2] = (wrong_word[2]+1) % 2
print(f"Word with 2 errors:\n{wrong_word2}")
where_the_error2 = syndromes_2[tuple(wrong_word2 @ H_2 % 2)]
#print(f"Where's the error:\n{where_the_error2}")
print(f"Сorrected word:\n{(wrong_word2 + where_the_error2) % 2}")
# 2.11                        # три ошибки
wrong_word2[4] = (wrong_word[4]+1) % 2
print(f"Word with 3 errors:\n{wrong_word2}")
where_the_error2 = syndromes_2[tuple(wrong_word2 @ H_2 % 2)]
#print(f"Where's the error:\n{where_the_error2}")
print(f"Сorrected(not) word:\n{(wrong_word2 + where_the_error2) % 2}")
print(f"Real right word:\n{right_word2}")


