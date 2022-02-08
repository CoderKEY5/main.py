import turtle, random

word_list = ['livre', 'doigt', 'heure', 'froid', 'danse', 'arbre', 'lundi', 'orage', 'bisou', 'chien', 'chiot', 'aigle',
             'lapin', 'court', 'merci', 'blanc', 'salut', 'verre', 'voire', 'chair', 'short', 'veste', 'grand', 'pomme',
             'gomme', 'avoir', 'autre', 'temps', 'trois', 'aussi', 'terre', 'jenre', 'image', 'monde', 'vivre', 'forme',
             'juste', 'aider', 'ligne', 'avant', 'droit', 'vivux', 'quand', 'votre', 'faire', 'pizza', 'biere', 'pates',
             'aimer', 'porte']
answer = random.choice(word_list)  # choose a random word from the list
y = 250  # y location
print(answer)


def draw_square(x, y, col):  # takes in x,y coordinates and a color
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(col)  # set the fillcolor
    turtle.begin_fill()  # start the filling color
    for i in range(4):  # drawing the square
        turtle.forward(50)
        turtle.right(90)
    turtle.end_fill()  # ending the filling of the color


def input_guess(prompt):
    my_input = turtle.textinput("Mots de cinq lettres", prompt)
    if my_input == None:
        return "     "  # if you press cancel or submit with nothing
    elif len(my_input) != 5:
        return my_input[0:5]  # sends the first five characters
    else:
        return my_input.lower()  # sends lower case of the word. Means case does not make a difference.


def check_guess(my_input, answer, y):
    count = 0  # Need a count, because of for loop used
    x = -250  # x location
    for i in my_input:
        if i == answer[count]:
            draw_square(x, y, "green")  # exact character match draws a green square
        elif i in answer:
            draw_square(x, y, "yellow")  # else if character anywhere in word draws yellow
        else:
            draw_square(x, y, "red")  # otherwise draws red
        count += 1  # add 1 to the count
        x += 75  # move x coordinate along by 75
    turtle.penup()  # Moves the turtle penup
    turtle.goto(x, y - 25)  # Moves it slightly down for the word
    turtle.write(my_input, font=("Verdana", 15, "normal"))  # font verdana, size 15, normal style


for i in range(6):  # Where the program starts
    guess_prompt = "qu'est-ce que deviner" + str(i + 1) + "?"  # Makes a nice string for the prompt
    my_input = input_guess(guess_prompt)  # calls input_guess function
    check_guess(my_input, answer, y)  # checks the guess
    y -= 75  # y down by 75
    if my_input == answer:
        turtle.penup()
        turtle.goto(-300, -200)  # Always draws the congratulations in the same place
        turtle.write("Well Done!", font=("Verdana", 42, "normal"))
        break
else:  # Only runs if the for loop executes completely. i.e. You've used all your guesses.
    turtle.penup()
    turtle.goto(-300, -200)
    turtle.write(answer, font=("Verdana", 42, "normal"))
turtle.done()  # Needs if you are using Pycharm and some other Python editors.


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
