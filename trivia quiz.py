import easygui
import math
import pygame

pygame.init()
#Music
pygame.mixer.pre_init(44100,16,2,4096)
pygame.mixer.music.load("elevatormusic.mp3")
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(-1)

#Start
easygui.msgbox("This will be a quiz about some strange facts")
score = 0


#Questions
#Q1
answer1 = easygui.buttonbox("True or False: John Adams had a dog named Satan",
                            choices = ['True','False'])

#Correct answer
if(answer1 == 'False'):
    score = score + 0
    easygui.msgbox("Incorrect")
elif(answer1 == 'True'):
    score = score + 10
    easygui.msgbox("Correct")


#Q2
answer2 = easygui.buttonbox("True or False: Bullfrogs sleep 3 hours a day",
                            choices = ['True','False'])

#Correct answer
if(answer2 == 'True'):
    score = score + 0
    easygui.msgbox("Incorrect: they don't sleep at all")
elif(answer2 == 'False'):
    score = score + 10
    easygui.msgbox("Correct: they don't sleep at all")


#Q3
answer3 = easygui.buttonbox("True or False: There are 10 times as many bacterial cells in a human body than there are actual body cells",
                            choices = ['True','False'])

#Correct answer
if(answer3 == 'False'):
    score = score + 0
    easygui.msgbox("Incorrect")
elif(answer3 == 'True'):
    score = score + 10
    easygui.msgbox("Correct")


#Q4
answer4 = easygui.buttonbox("How large was the largest recorded snowflake?",
                            choices = ['3 inches','5.5 inches','13.25 inches','15 inches'])

#Correct answer
if(answer4 == '3 inches'):
    score = score + 0
    easygui.msgbox("Incorrect: it was 15 inches")
elif(answer4 == '5.5 inches'):
    score = score + 0
    easygui.msgbox("Incorrect: it was 15 inches")
elif(answer4 == '13.25 inches'):
    score = score + 0
    easygui.msgbox("Incorrect: it was 15 inches")
elif(answer4 == '15 inches'):
    score = score + 10
    easygui.msgbox("Correct")


#Q5
answer5 = easygui.buttonbox("How fast does the average sneeze travel?",
                            choices = ['45 mph','75 mph','100 mph','120 mph'])

#Correct answer
if(answer5 == '45 mph'):
    score = score + 0
    easygui.msgbox("Incorrect, it was 100 mph")
elif(answer5 == '75 mph'):
    score = score + 0
    easygui.msgbox("Incorrect, it was 100 mph")
elif(answer5 == '120 mph'):
    score = score + 0
    easygui.msgbox("Incorrect, it was 100 mph")
elif(answer5 == '100 mph'):
    score = score + 10
    easygui.msgbox("Correct")


#Q6
answer6 = easygui.buttonbox("Why was Donald Duck banned in Finland?",
                            choices = ['they have a grudge against Disney','he doesnt wear pants','they found him offensive'])

#Correct answer
if(answer6 == 'they have a grudge against Disney'):
    score = score + 0
    easygui.msgbox("Incorrect")
elif(answer6 == 'they found him offensive'):
    score = score + 0
    easygui.msgbox("Incorrect")
elif(answer6 == 'he doesnt wear pants'):
    score = score + 10
    easygui.msgbox("Correct")


#Q7
answer7 = easygui.buttonbox("About how many Americans have a potassium deficiency?",
                            choices = ['3 out of 10','7 out of 10','9 out of 10'])

#Correct answer
if(answer7 == '3 out of 10'):
    score = score + 0
    easygui.msgbox("Incorrect, its 9 out of 10")
elif(answer7 == '7 out of 10'):
    score = score + 0
    easygui.msgbox("Incorrect, its 9 out of 10")
elif(answer7 == '9 out of 10'):
    score = score + 10
    easygui.msgbox("Correct")


#Q8
answer8 = easygui.enterbox("Someone once tried to sell New Zealand on eBay. How much did it go for in dollars?")

#Correct answer
if(answer8 == '3000'):
    score = score + 10
    easygui.msgbox("Correct! How did you know that...")
else:
    score = score + 0
    easygui.msgbox("Incorrect, the answer is 3000")


#Q9
answer9 = easygui.enterbox("What is the only mammal that cant jump?")

#Correct answer
if(answer9 == 'elephant' or answer9 == 'Elephant'):
    score = score + 10
    easygui.msgbox("Correct")
else:
    score = score + 0
    easygui.msgbox("Incorrect, the answer is the elephant")


#Q10
answer10 = easygui.enterbox("What word in the English language has the most dictionary definitions?")

#Correct answer
if(answer10 == 'set' or answer10 == 'Set'):
    score = score + 10
    easygui.msgbox("Correct")
else:
    score = score + 0
    easygui.msgbox("Incorrect, it is the word 'set'")


easygui.msgbox("Thanks for taking my quiz!")

#score math
if(0 < score < 30 or score == 0):
    easygui.msgbox("Your score was " + (str((score) / 10)) + " out of the 10 questions, or " + str(score) + "%. Maybe you can do better next time")
elif(30 < score < 50 or score == 30):
    easygui.msgbox("Your score was " + (str((score) / 10)) + " out of the 10 questions, or " + str(score) + "%. Not too bad, but it could be better")
elif(50 < score < 80 or score == 50 or score == 80):
    easygui.msgbox("Your score was " + (str((score) / 10)) + " out of the 10 questions, or " + str(score) + "%. Nice!")
elif(score == 90):
    easygui.msgbox("Your score was " + (str((score) / 10)) + " out of the 10 questions, or " + str(score) + "%. Almost perfect!")
elif(score == 100):
    easygui.msgbox("Your score was " + (str((score) / 10)) + " out of the 10 questions, or " + str(score) + "%. Impressive! Really, thats surprising. Good job")









