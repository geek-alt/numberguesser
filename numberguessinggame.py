import tkinter as tk
from tkinter import *
import random


win = tk.Tk()
win.geometry("700x700")
win.title("NumberGuess")


#Main function of the game using random module

num=random.randint(1,50) #This generates random number from 1 - 50. "num" is a variable which stores this function

hint=StringVar() #This specifies "hint" is a string variable
score=IntVar() #This specifies "score" variable is a integer variable meaning numbers.
final_score=IntVar() #This specifies "Final_Score" is a integer variable
guess=IntVar() #This specifies "guess" is a integer variable. This also stores the number that user has guessed


def fun():
    x = guess.get()
    final_score.set(score.get())
    if score.get()>0:


        if x > 50 or x < 1:
            hint.set("You lost 1 chance")
            score.set(score.get()-1)
            final_score.set(score.get())

        elif num==x:
            hint.set("Congratulation YOU WON!!!👍")
            score.set(score.get()-1)
            final_score.set(score.get())
        
        elif num > x: # if the random number to guess (num) is higher than the guessed number by player which is X than show hint
            hint.set("Your guess was too low: Guess a number Higher")
            score.set(score.get()-1) # subtract -1 from the total score
            final_score.set(score.get()) #Show the final score.
        
        elif num < x: #if the random to guess (num) is lower than the guessed number by player which is X than show hint.
            hint.set("Your guess is too high: Guess a lower number")
            score.set(score.get()-1) # subtract -1 from the total score
            final_score.set(score.get()) #Show the final score.
        
    else:
        hint.set("GAME OVER!❌, You Lost💀") #If the number of Guess is finished without guessing correct number it prints GAME OVER, YOU LOST

            

hint.set("Guess the number between 1 to 50")
score.set(5)
final_score.set(score.get())



Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE, bg='silver', fg='pink').place(relx=0.5, rely=0.35, anchor=CENTER) #prints text which writes "Guess"

Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief = GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER) #It displays "hint"

Entry(win, textvariable=final_score, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER) #This shows final score

Label(win, text='Can you guess the number?', font=("Courier", 25)).place(relx= 0.5, rely = 0.09, anchor=CENTER) # A text which shows when playing the game

Label(win, text='Score out of 5!', font=("Courier", 25)).place(relx=0.3, rely= 0.85, anchor=CENTER)

Button(win, width=8, text='CHECK', font=('Courier',25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER) #it is a button which has text "Check in it", it checks the number that user guessed and checks in the system if they match


win.mainloop()


if __name__ == "__main__":
    fun()