import random
import webbrowser


with open("saved ships.txt", "r") as f:
	for line in f.readlines():
		if line[8] == "|":
			x, browser = line.split("|")

webbrowser.get(browser)
action = input("View Saved (v) or generate a ship? (g) ")

convert = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

if action.lower() == "g":
	value=""
	for x in range(1, 15):
		y = random.randint(0, 35)
		y = convert[y]
		value += y
	
	print(f"https://ship.shapewright.com/?name={value}")
	webbrowser.open(f"https://ship.shapewright.com/?name={value}")
	save = input("Would you like to save? (y/n) ")
	if save.lower() == "y":
		desc = input("Description? ")
		with open("saved ships.txt", "a") as f:
			f.write(f"{desc}: https://ship.shapewright.com/?name={value}")
	
	elif save.lower() == "n":
		pass
elif action.lower() == "v":
	with open("saved ships.txt", "r") as f:
		for line in f.readlines():
			print(f"{line}\n")

elif action == "%debug%":
	print("You have entered the Debug mode,\nin this mode, you made fix certain problems, as of current, the only\npossible problem you can fix with this is\nthe location of your google chrome. Close the program now if you want to keep your data\nif you do not close it and hit enter, saved ships will be DELETED. Pressing enter will continue.")
	print("However, there is an alternative. To manually add your chrome location via the saved ships.txt file. It is the top line.\nYou must also keep the eight digits and the pipe operator (01011000|filepathhere).")
	input("Are you sure you want to continue? ")
	browser = input("Where is your browser? Default is\nC:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk %s.\nIf that is not it, where is it? (must end in 'Google Chrome.lnk %s').")
	with open("saved ships.txt", "w") as f:
		f.write(f"01011000|{browser}")
	