# Programa para verificar a existência da letra 'a' (maiúscula ou minúscula) em uma string:

def count_a_in_string(s):
    count = s.lower().count('a')
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Exemplo de uso


string = input("Informe uma string: ")
count_a_in_string(string)
