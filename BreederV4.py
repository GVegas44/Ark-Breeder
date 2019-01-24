#!/usr/bin/python3
import os
import readline
import re
import string
import pickle
import json


CommandlineInput = input("Add Tame? Y or N: ").upper()
""" Starting script that checks commandline input and sends user in to ether Add Tame Functions or Search Functions"""
def firstrun(CommandlineInput):
	startupcheck()
	check = False
	while not check:
		if CommandlineInput == 'Y':
			addtame()
			return check == True
		elif CommandlineInput == 'N':			
			Initialize()
			return check == True
		elif not CommandlineInput == 'Y' or 'N': 
			print('Not Valid Input')
			return check == False

""" Checks to see if Database exists if not creates it"""
def startupcheck():
	if os.path.isfile('/root/Documents/Ark/data.json' )== True:
		return True
	else:
		with open('data.json', 'w') as fp:
			json.dump({}, fp)

""" Main Searching function Takes user Input and checks to see if search is in database. If it is then it prints all the Attributes of the tame"""
def Initialize():
	search = input("What is the name of the Tame you want to search for?: ")
	with open('data.json', 'r') as fp:
		database = json.load(fp)
	if search in database:
#		print('Breed: {}'.format(database[search]['Breed']))
		printall(search)
	else:
		print('Tame does not exist')

"""Search Function that prints all Tames attributes"""
def printall(search):
	with open('data.json', 'r') as fp:
		database = json.load(fp)
	print('\nBreed: {} \nName: {} \nLevel {} \nSex: {} \nHealth: {}\nStamina: {}\nOxygen :{}\nFood: {}\nWeight: {}\nMelee: {}'.format(database[search]['Breed'], database[search]['Name'], database[search]['Sex'], database[search]['Level'], database[search]['Health'], database[search]['Stamina'], database[search]['Oxygen'], database[search]['Food'], database[search]['Weight'], database[search]['Melee']))


#def printallbreeds(search):
#	with open('data.json', 'r') as fp:
#		database = json.load(fp)
#	for i, y in database.items():
#		if y == search:
#			print(i)
#		if 'Breed' == search:
#			print(name)

"""Adds Takes user input and puts all values in to dictonary"""
def addtame():
	Tames = {}
	Breed = input("Breed: ")
	Name = input("Name: ")
	Sex = input("M or F: ")
	Level = input("Level: ")
	Health = input("Health: ")
	Stam = input("Stam: ")
	Oxy = input("Oxygen: ")
	Food = input("Food: ")
	Weight = input("Weight: ")
	Melee = input("Melee: ")
	Tames[Name] = {"Breed":Breed, 'Name':Name, 'Sex':Sex, "Level":Level, "Health":Health, "Stamina":Stam, "Oxygen":Oxy, "Food":Food, "Weight":Weight, "Melee":Melee}
	Database(Tames)
#	writer(Breed, Name, Sex, Level, Health, Stam, Oxy, Food, Weight, Melee)

""" Loads data base and updates it with Newly added Tame"""
def Database(data):
	with open('data.json') as fp:
		database = json.load(fp)

	database.update(data)
	with open('data.json', 'w') as fp:
		json.dump(database, fp)
""" Writes all User input in to a text file in Current Directory 

TO ENABLE THIS FUNCTION UNHASH IN ADDTAME FUCTION"""
def writer(Breed, Name, Sex, Level, Health, Stam, Oxy, Food, Weight, Melee):
	with open(Breed+"_"+Name+".txt", "w") as text_file:
		text_file.write("Name: "+Breed+"\n")
		text_file.write("Level: "+Sex+"\n")
		text_file.write("Name: "+Name+"\n")
		text_file.write("Level: "+Level+"\n")
		text_file.write("Health: "+Health+"\n")
		text_file.write("Stamina: "+Stam+"\n")
		text_file.write("Oxygen: "+Oxy+"\n")
		text_file.write("Food: "+Food+"\n")
		text_file.write("Weight: "+Weight+"\n")
		text_file.write("Melee: "+Melee+"\n")
		text_file.close()
		newtame = print(Breed+"_"+Name)		
		newtame = Tames(Breed, Name, Level, Sex, Health, Stam, Oxy, Food, Weight, Melee)

#		print(newtame.Showall())


""" Creates objects of all tames entered by user Not being used right now"""
class Tames(object):
	def __init__(self, Breed, Name, Sex, Level, Health, Stam, Oxy, Food, Weight, Melee):
		super(Tames, self).__init__()
		self.Breed = Breed 
		self.Name = Name
		self.Sex = Sex
		self.Level = Level
		self.Health = Health
		self.Stam = Stam
		self.Oxy = Oxy
		self.Food = Food
		self.Weight = Weight
		self.Melee = Melee
		Memory = json.dumps(Tames.__dict__)
	def Showall(self):
		return('{} {} }} {} {} {} {} {} {} {}'.format(self.Breed, self.Name, self.Sex, self.Level, self.Health, self.Stam, self.Oxy, self.Food, self.Weight, self.Melee))

def main(newtame):
    newtame = Tames(Breed, Name, Sex, Level, Health, Stam, Oxy, Food, Weight, Melee)
    print(newtame.Showall())


firstrun(CommandlineInput)