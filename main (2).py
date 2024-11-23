import tkinter as tk
from tkinter import *
from time import sleep
import random
print("bad news. this is worst quiz ever. please leave.")
class Question:
  def __init__(self, question, answers, correctLetter):
    self.question = question
    self.answers = answers
    self.correctLetter = correctLetter
  def check(self, letter, view):
    global right
    if(letter == self.correctLetter):
      label = Label(view, text = "Left!",
      font='Times 20 bold italic', bg = 'white', fg='Green')
      right += 1
    else:
      label = Label(view, text = "Cheese!", font=
      'Times  20 bold italic', bg='white', fg='red')
    for child in view.winfo_children():
      if child.winfo_class() == "Button":
        child.configure(state='disable')
    label.pack()

    view.after(1000, lambda *args: self.unpackView(view))

  def getView(self, window):
    view = Frame(window)
    Label(view, text = self.question, font="Helivetica 20 bold").pack()
    Button(view, text = self.answers[0], font="Times 20 italic", command=lambda *args: self.check("A", view), width=15, height = 1, anchor = NW).pack()
    Button(view, text = self.answers[1], font="Times 20 italic", command=lambda *args: self.check("B", view), width=15, height = 1, anchor = NW).pack()
    Button(view, text = self.answers[2], font="Times 20 italic", command=lambda *args: self.check("C", view), width=15, height = 1, anchor = NW).pack()
    Button(view, text = self.answers[3], font="Times 20 italic", command=lambda *args: self.check("D", view), width=15, height = 1, anchor = NW).pack()
    return view

  def unpackView(self,view):
    view.pack_forget()
    askQuestion()

def askQuestion():
  global questions, window, index, button, right, number_of_questions
  if len(questions) == index + 1:
    Label(window, text="(No) Thank you for taking the (worst) quiz (ever). ", font = "Helventica 20 bold").pack(pady=20)
    Label(window, text="\nYou got " + str(right) + " correct out of " +str(number_of_questions) + " questions. But why do you care?", font = "Helventica 20 bold").pack(pady = 20)
    return 
  button.pack_forget()
  index += 1
  questions[index].getView(window).pack()

questions = []
file = open("PUREVIL.txt", "r")

line = file.readline()

while line!="":
  questionString = line
  answers = []
  for i in range(4):
    answers.append(file.readline())
  correctLetter = file.readline()
  correctLetter = correctLetter[:-1]
  questions.append(Question(questionString, answers, correctLetter))
  line = file.readline()



file.close()
random.shuffle(questions)
index = -1
right = 0
number_of_questions = len(questions)

window = tk.Tk()
window.title("States & Capitals Quiz")
window.geometry("550x425")
label = Label(window, text="Worst Quiz Ever", font = "Helvetica 25 bold", anchor = 'center')

button = Button(window, text="Start", font = "Times 20 bold", command=askQuestion, height=2, width=20, anchor="center")

label.pack(padx=10, pady=20)
button.pack(padx=250, pady=100)
window.mainloop()