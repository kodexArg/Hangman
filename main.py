import os
import random


ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"


def random_word():
    with open("./files/data.txt") as f: data = f.readlines()
    word = random.choice(data).upper()
    k, word_dict = 0, {}
    for letter in word[:-1]:                #removes line break
        word_dict[k] = letter
        k += 1
    return word_dict


def hanguin_man_ascii(attempt):
    assert 8 > attempt, "Número no permitido de intentos"
    filename = "./files/hangman{}.txt".format(attempt)
    with open(filename, "r") as f:
        for line in f:
            print(line)


def guess_the_word(objective_word, hidden_word, customer_choice):
    exists_ = False
    for i in objective_word:
        letter = objective_word[i]
        if letter == customer_choice:
            hidden_word[i] = letter.upper()
            exists_ = True
    return hidden_word, exists_


def run():
    success = False
    attempt = 0
    message = ""
    objective_word = random_word()
    hidden_word = {k: "_" for k in range(len(objective_word))}
    history = []

    def ascii_drawing(attempt, message, hidden_word, history):
        os.system("clear")
        if message != "": #messages fixed at top
            print(f"{message}\n")
            message = ""
        else:
            print("\n")
        hanguin_man_ascii(attempt)
        print("\nPalabra: {}".format(" ".join(hidden_word.values())))
        print("\nLetras probadas: {}".format(",".join(history)))

    while attempt < 6 and not success:
        ascii_drawing(attempt, message, hidden_word, history) #because DRY!
        customer_choice = input("\nAdivina una letra:").upper()      
        if customer_choice not in ALPHABET:
            message = "Sólo puedes intentar con letras"
            continue
        if customer_choice in history:
            message = "Ya has intentado esa letra, no la endré en cuenta..."
            continue

        history.append(customer_choice)
        hidden_word, found_letter = guess_the_word(objective_word, hidden_word,
                                                   customer_choice)
        if not found_letter: attempt += 1
        if "_" not in hidden_word.values(): success = True

    
    if success:
        message = "          MUY BIEN!!!"
        ascii_drawing(attempt, message, hidden_word, history)
    else:
        message = " Ahoracdo!!! :(    La palabra secreta era {}.".format(
                "".join(objective_word.values()).upper())
        ascii_drawing(attempt, message, hidden_word, history)        

if __name__ == "__main__":
    run()
    print("\n-----------------end-----------------\n")
