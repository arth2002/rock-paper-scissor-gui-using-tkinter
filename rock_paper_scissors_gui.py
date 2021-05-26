from tkinter import *
import random
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg

choice = None
user_score = 0
computer_score = 0


# this function is for choice = rock
def rock():
    global choice
    choice = "Rock"
    rock_img = ImageTk.PhotoImage(Image.open("rock.png"))
    label = Label(root, image=rock_img)
    label.configure(image=rock_img, width=220, height=180)
    label.image = rock_img  # keep a reference!
    label.place(x=10, y=100)
    # print("You choose rock")
    computer_choice()


# this function is for choice = paper
def paper():
    global choice
    choice = "Paper"
    paper_img = ImageTk.PhotoImage(Image.open("paper.png"))
    label = Label(root, image=paper_img)
    label.configure(image=paper_img, width=220, height=180)
    label.image = paper_img  # keep a reference!
    label.place(x=10, y=100)
    # print("You choose paper")
    computer_choice()


# this function is for choice = scissor
def scissor():
    global choice
    choice = "Scissor"
    scissor_img = ImageTk.PhotoImage(Image.open("scissors.png"))
    label = Label(root, image=scissor_img)
    label.configure(image=scissor_img, width=220, height=180)
    label.image = scissor_img  # keep a reference!
    label.place(x=10, y=100)
    # print("You choose scissor")
    computer_choice()


# this function will decide who won the game
def winner(c_player, c_computer):
    global user_score
    global computer_score
    if c_player == "Paper" and c_computer == "Rock" or c_player == "Rock" and c_computer == "Scissor" or \
            c_player == "Scissor" and c_computer == "Paper":
        winner_var.set("User Got 1 Point")
        # print("User Win")
        user_score += 1
        main_score.set(f"User:{user_score}\nComputer:{computer_score}")
    elif c_player == c_computer:
        winner_var.set("Draw")
        # print("It's Draw")
    else:
        winner_var.set("Computer Got 1 Point")
        computer_score += 1
        main_score.set(f"User:{user_score}\nComputer:{computer_score}")
        # print("Computer Win")


def computer_choice():
    global choice
    make_choice = ["Rock", "Paper", "Scissor"]
    c_choice = random.choice(make_choice)

    if choice == "Rock":
        if c_choice == "Rock":
            img = ImageTk.PhotoImage(Image.open("rockReverse.png"))
        elif c_choice == "Paper":
            img = ImageTk.PhotoImage(Image.open("paperReverse.png"))
        elif c_choice == "Scissor":
            img = ImageTk.PhotoImage(Image.open("scissorsReverse.png"))

        label = Label(root, image=img)
        label.configure(image=img, width=220, height=200)
        label.image = img  # keep a reference!
        label.place(x=470, y=100)
        # print("computer choose " + c_choice)
        winner("Rock", c_choice)
    elif choice == "Paper":
        if c_choice == "Rock":
            img = ImageTk.PhotoImage(Image.open("rockReverse.png"))
        elif c_choice == "Paper":
            img = ImageTk.PhotoImage(Image.open("paperReverse.png"))
        elif c_choice == "Scissor":
            img = ImageTk.PhotoImage(Image.open("scissorsReverse.png"))

        label = Label(root, image=img)
        label.configure(image=img, width=220, height=200)
        label.image = img  # keep a reference!
        label.place(x=470, y=100)
        # print("computer choose " + c_choice)
        winner("Paper", c_choice)
    elif choice == "Scissor":
        if c_choice == "Rock":
            img = ImageTk.PhotoImage(Image.open("rockReverse.png"))
        elif c_choice == "Paper":
            img = ImageTk.PhotoImage(Image.open("paperReverse.png"))
        elif c_choice == "Scissor":
            img = ImageTk.PhotoImage(Image.open("scissorsReverse.png"))

        label = Label(root, image=img)
        label.configure(image=img, width=220, height=200)
        label.image = img  # keep a reference!
        label.place(x=470, y=100)
        # print("computer choose " + c_choice)
        winner("Scissor", c_choice)

# this funtion will show message about who won the game
def result():
    global user_score
    global computer_score
    if user_score > computer_score:
        tmsg.showinfo("Result", "You won the Game")
        # print("User won this whole game")
        root.destroy()
    elif user_score == computer_score:
        tmsg.showinfo("Result", "Match Draw")
    else:
        tmsg.showinfo("Result", "You Lose the Game")
        # print("computer won this whole game")
        root.destroy()


root = Tk()
root.geometry("700x500")
root.minsize(700, 500)
root.maxsize(700, 500)
root.title("Rock Paper Scissors")

mainLabel = Label(root, text="Let's Play Rock Paper Scissor", font="Ariel 15 bold", bg="Red", fg="white")
mainLabel.pack(fill="x")

# for user choice here are three buttons
user_options = Label(root, text="User Options:  ", bg="black", fg="white", height=1)
user_options.pack(side=LEFT, anchor=NW, pady=5)
rockBtn = Button(root, text="Rock", width=7, height=1, command=rock)
rockBtn.pack(side=LEFT, anchor=NW, pady=5)

paperBtn = Button(root, text="Paper", width=7, height=1, command=paper)
paperBtn.pack(side=LEFT, anchor=NW, pady=5)

scissorBtn = Button(root, text="Scissor", width=7, height=1, command=scissor)
scissorBtn.pack(side=LEFT, anchor=NW, pady=5)

# this for computer (random choice for game)
label_c = Label(root, text="Computer ", bg="black", fg="white", font="Ariel 15")
label_c.pack(side=RIGHT, anchor=NE, padx=2, pady=5)

# this will show(prints) who won the game
winner_var = StringVar()
winner_var.set("Let's see who'll won?")
print_winner = Label(root, textvariable=winner_var, bg="black", fg="white", width=20, height=2, font="Ariel 15 bold")
print_winner.place(x=250, y=330)

# this will show(prints) score of user and computer
main_score = IntVar()
main_score.set(f"User:{user_score}\nComputer:{computer_score}")
print_score = Label(root, textvariable=main_score, bg="red", fg="white", width=10, height=2, font="Ariel 10 bold")
print_score.place(x=325, y=380)

# End the game button
end_game = Button(root, text="End Game", width=7, height=1, command=result)
end_game.place(x=340, y=450)
root.mainloop()
