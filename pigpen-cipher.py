import turtle
import time

def photographic_encrypy(root_txt):
    colors = turtle.Turtle()
    colorsDict = {" ": "black", "a": "gray", "b": "silver", "c": "whitesmoke", "d": "rosybrown", "e": "firebrick",
                  "f": "red", "g": "darksalmon",
                  "h": "sienna", "i": "sandybrown", "j": "bisque", "k": "tan", "l": "moccasin", "m": "floralwhite",
                  "n": "gold",
                  "o": "darkkhaki", "p": "lightgoldenrodyellow", "q": "olivedrab", "r": "chartreuse", "s": "goldenrod",
                  "t": "lightgreen",
                  "u": "green", "v": "mediumseagreen", "w": "mediumaquamarine", "x": "mediumturquoise",
                  "y": "darkslategray",
                  "z": "cyan"}
    result_txt = ''
    x = -350
    y = 250
    turtle.bgcolor("white")
    turtle.speed("normal")
    for i in range(len(root_txt)):
        if root_txt[i] in colorsDict:
            char = colorsDict[root_txt[i]]
        else:
            break

        if x == 350:
           x = -250
           y = y - 50

        colors.goto(x, y)
        colors.fillcolor(char)
        colors.begin_fill()
        colors.goto(x, y + 50)
        colors.goto(x + 50, y + 50)
        colors.goto(x + 50, y)
        colors.goto(x, y)
        colors.end_fill()
        x = x + 50

    if i == len(root_txt) - 1:
        time.sleep(1)

        print(result_txt)


def photographic_dencrypt():

    print("Please Check The Color's Dictionary")

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
choice = input("Photographic Or Pig-pen cipher Or ?\nhint : Enter name completely\n")
if choice == "Photographic" or choice == "photographic":
    your_answer = input("Do you want to encrypt this string or decrypt ?\nhint : enter 'e' or 'd'\n")
    if your_answer == "e":
        photographic_encrypy(root_txt)
    elif your_answer == "d":
        photographic_dencrypt()
    else:
        print("Your choice doesn't exist in the list !!!")
elif choice == 'Pigpen' or choice == "pigpen":
    your_answer = input("Do you want to encrypt this string or decrypt ?\nhint : enter 'e' or 'd'\n")
    if your_answer == "e":
        t = root_txt.lower()
        pigpen_encrypt(t)
    elif your_answer == "d":
        pigpen_dencrypt()
    else:
        print("Your choice doesn't exist in the list !!!")
