# Lógica e próximo elemento das sequências:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

def next_element(sequence):
    if sequence == 'a':
        return 9
    elif sequence == 'b':
        return 128
    elif sequence == 'c':
        return 49
    elif sequence == 'd':
        return 100
    elif sequence == 'e':
        return 13
    elif sequence == 'f':
        return 200

# Exemplos de uso


print(next_element('a'))  # 9
print(next_element('b'))  # 128
print(next_element('c'))  # 49
print(next_element('d'))  # 100
print(next_element('e'))  # 13
print(next_element('f'))  # 200
