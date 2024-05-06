# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

vocals =['A', 'E', 'I', 'O', 'U']

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter not in vocals:
        print(letter, end="\n")
        continue

    
        



