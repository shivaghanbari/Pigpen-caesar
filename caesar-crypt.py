def caesar_encrypt(root_txt, shift):
    result_txt = ''
    for char in root_txt:
        if char == ' ':
            result_txt = result_txt + char
        elif char.isupper():
            result_txt = result_txt + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result_txt = result_txt + chr((ord(char) + shift - 97) % 26 + 97)
    print(result_txt)


def caesar_dencrypt(root_txt, shift):
    result_txt = ''
    for char in root_txt:
        if char == ' ':
            result_txt = result_txt + char
        elif char.isupper():
            result_txt = result_txt + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            result_txt = result_txt + chr((ord(char) - shift - 97) % 26 + 97)
    print(result_txt)


def pigpen_encrypt(t):
    alphabet = {"a": chr(5287), "b": chr(8852), "c": chr(5290), "d": chr(8848),
                "e": chr(9633), "f": chr(8847), "g": chr(5283), "h": chr(8851), "i": chr(5285),
                "j": chr(5287) + "x", "k": chr(8852) + "x", "l": chr(5290) + "x", "m": chr(8848) + "x",
                "n": chr(9633) + "x", "o": chr(8847) + "x", "p": chr(5283) + "x", "q": chr(8851) + "x",
                "r": chr(5285) + "x",
                "s": chr(5287) + "o", "t": chr(8852) + "o", "u": chr(5290) + "o", "v": chr(8848) + "o",
                "w": chr(9633) + "o", "x": chr(8847) + "o", "y": chr(5283) + "o", "z": chr(8851) + "o"}
    result_txt = ' '
    for i in range(len(t)):
        if t[i] in alphabet and t[i] != ' ':
            char = alphabet[t[i]]
            result_txt = result_txt + char
        else:
            result_txt += ' '

    print(result_txt)


def pigpen_dencrypt():
    print(""" pig pen characters :
        a( ᒧ ),b( ⊔ ), c( ᒪ ), d( ⊐ ), e( □ ), f( ⊏ ), g( ᒣ ), h( ⊓ ), i( ᒥ ), j( ᒧx ), k( ⊔x ) ,l( ᒪx ), m( ⊐x ),
        n( □x ), o( ⊏x ), p( ᒣx ), q( ⊓x ), r( ᒥx ), s( ᒧo ), t( ⊔o ), u( ᒪo ), v( ⊐o ), w( □o ), x( ⊏o), y( ᒣo ),Z( ⊓o )
        """)


root_txt = input("Please write a string \n")
choice = input("Caesar Or Pig-pen cipher ?\nhint : Enter name or first letter of it\n")
if choice == "caesar" or choice == "c" or choice == "C":
    your_answer = input("Do you want to encrypt this string or decrypt ?\nhint : enter 'e' or 'd'\n")
    if your_answer == "e":
        caesar_encrypt(root_txt, shift=4)
    elif your_answer == "d":
        caesar_dencrypt(root_txt, shift=4)
    else:
        print("Your choice doesn't exist in the list !!!")
elif choice == 'pigpen' or choice == 'p' or 'P':
    your_answer = input("Do you want to encrypt this string or decrypt ?\nhint : enter 'e' or 'd'\n")
    if your_answer == "e":
        t = root_txt.lower()
        pigpen_encrypt(t)
    elif your_answer == "d":
        pigpen_dencrypt()
    else:
        print("Your choice doesn't exist in the list !!!")
