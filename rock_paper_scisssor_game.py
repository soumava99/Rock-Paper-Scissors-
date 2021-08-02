from tkinter import *
from random import randint
from tkinter import ttk 

root = Tk()
root.title('Soumava - Rock,Paper,Scissors')
myLabel = Label(root, text = "Let's Play Rock-Paper-Scissors!!!",font=("Helvetica",20),bg ="sky blue")
myLabel.pack(pady = 10)

root.iconbitmap('D:\Edrive files\Python Programming\Python_Projects\Rock_Papaer_Scissors/rockpaperscissor.ico')
root.geometry("500x800")
#change background color to pink
root.config(bg="sky blue")

#Define our images
rock = PhotoImage(file = 'D:\Edrive files\Python Programming\Python_Projects\Rock_Papaer_Scissors/rock.png')
paper = PhotoImage(file = 'D:\Edrive files\Python Programming\Python_Projects\Rock_Papaer_Scissors\paper.png')
scissors = PhotoImage(file = 'D:\Edrive files\Python Programming\Python_Projects\Rock_Papaer_Scissors\scissor.png')

#Add Images to list
image_list = [rock,paper,scissors]

#Pick random number between 0 and 2
pick_number = randint(0,2)

#Throw up an image when the program starts
image_label = Label(root,image = image_list[pick_number],bd =0)
image_label.pack(pady = 15)

myLabel2 = Label(root, text = "Choose:-",font=("Helvetica",18),bg ="sky blue")
myLabel2.pack(pady = 5)


global player
player = 0
global computer
computer = 0
global tie
tie = 0

#Create spin button
def spin():
	#pick random number
	pick_number = randint(0,2)
	#Show image
	image_label.config(image = image_list[pick_number])

	# 0 = Rock
	# 1 = Paper
	# 2 = Scissors

	# Convert Dropdown choice to a number
	if user_choice.get() == "Rock":
		user_choice_value = 0
	elif user_choice.get() == "Paper":
		user_choice_value = 1
	elif user_choice.get() == "Scissors":
		user_choice_value = 2

	global player
	global computer
	global tie
	
	# Deterine if we won or lost 
	if user_choice_value == 0: #Rock
		if pick_number == 0:
			win_lose_label.config(text = "It's A Tie! Spin Again....")
			tie = tie + 1
			scorelabel3.config(text = "Tie            : " + str(tie))
		elif pick_number == 1: #Paper
			win_lose_label.config(text = "You Lose...Paper Cover Rock!")
			computer = computer + 1
			scorelabel2.config(text = "Computer Score : " + str(computer))
		elif pick_number == 2: #Scissors
			win_lose_label.config(text = "You Win!!!...Rock Smashes Scissors!")
			player = player + 1
			scorelabel1.config(text = "Your Score     : " + str(player))


	if user_choice_value == 1: #Paper
		if pick_number == 1:
			win_lose_label.config(text = "It's A Tie! Spin Again....")
			tie = tie + 1
			scorelabel3.config(text = "Tie            : " + str(tie))
		elif pick_number == 0: #Rock
			win_lose_label.config(text = "You Win!!!...Paper Cover Rock!")
			player = player + 1
			scorelabel1.config(text = "Your Score     : " + str(player))
		elif pick_number == 2: #Scissors
			win_lose_label.config(text = "You Lose...Scissors Cuts Paper!")
			computer = computer + 1
			scorelabel2.config(text = "Computer Score : " + str(computer))

	if user_choice_value == 2: #Scissors
		if pick_number == 2:
			win_lose_label.config(text = "It's A Tie! Spin Again....")
			tie = tie + 1
			scorelabel3.config(text = "Tie            : " + str(tie))
		elif pick_number == 0: #Rock
			win_lose_label.config(text = "You Lose...Rock Smashes Scissors!")
			computer = computer + 1
			scorelabel2.config(text = "Computer Score : " + str(computer))
		elif pick_number == 1: #Paper
			win_lose_label.config(text = "You Win!!!...Scissors Cuts Paper!")
			player = player + 1
			scorelabel1.config(text = "Your Score     : " + str(player))
	
			
	

# Make our choice
user_choice = ttk.Combobox(root,value = ("Rock","Paper","Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)




spin_button = Button(root,text="Spin!",command = spin)
spin_button.pack(pady=10)

#Label for showing if you won or not
win_lose_label = Label(root,text = "", font=("Helvetica",18),bg ="sky blue" )
win_lose_label.pack(pady = 10)

#Creating the score keeper label
scorelabel1 = Label(root, text = "Your Score     : " + str(player),font=("Helvetica",10),bg ="sky blue")
scorelabel1.pack(pady = 2)
scorelabel2 = Label(root, text = "Computer Score : " + str(computer),font=("Helvetica",10),bg ="sky blue")
scorelabel2.pack(pady = 2)
scorelabel3 = Label(root, text = "Tie            : " + str(tie),font=("Helvetica",10),bg ="sky blue")
scorelabel3.pack(pady = 2)


root.mainloop()
