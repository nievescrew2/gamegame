import random
import json

openinghooklist = ["Everyone's story starts out differently.", "Most people have normal lives."]
namelist = ["Spencer", "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie", "Drew", "Cameron"]
countrylist = ["America", "Canada", "England", "Australia", "Germany", "France", "Italy", "Spain", "Japan", "China", "Ethiopia", "Nigeria", "South Korea", "North Korea", "Russia", "Mongolia"]
birthplaceslist = ["in a small dingy hospital", "in a fancy hospital", "at home", "in the back of an ambulance"]
namereasonslist = ["after one of your relatives", "after a celebrity", "after a tv show character" ,"after a movie character"]
citylist = ["New York", "Chicago", "Raleigh", "Birmingham", "San Diego", "Nashville", "Naples", "Paris", "Madrid", "Tokyo", "Seoul", "Busan", "Gangnam", "Wuhan", "Beijing", "Hong Kong", "Mumbai", "New Delhi"]
familytypelist = ["a poor family", "a rich family", "a middle class family", "a super evil family", "a super good family", "a family of criminals", "no family"]
daytype = ["a random day", "a calm day", "a completely normal day", "a sad day", "a bad day", "a good day", "a super important day"]

###############

openinghook = random.choice(openinghooklist)
name = random.choice(namelist)
playername = input("What's your name?")
birthplaces = random.choice(birthplaceslist)
namereasons = random.choice(namereasonslist)
city = random.choice(citylist)
country = random.choice(countrylist)
familytype = random.choice(familytypelist)
day = random.choice(daytype)

###############

print(f"Welcome to the game of life, {playername}.\n")
print(f"{openinghook} \n")
print(f"Yours starts {birthplaces}. Your parents named you {name}, {namereasons}. \n")
print(f"You were born in {city}, {country} to {familytype}.")
print(f"On {day}, as you sip your tea, a great earthquake shakes the ground. \n")
print(f"You look outside and see a great tower appear from the ground. As you wonder what is going on, you are suddenly teleported inside of the tower! \n")


def enter(): 
    entry = input(f"You look around and see a door with a 1 over it. Do you enter or not? | Y = Yes | N = No").upper()
    if entry == "N":
        print("You scramble away from the door, and try to find another way out. You can't find a way out, and are trapped for eternity. GAME OVER.")
    elif entry == "Y":
        print("You walk through the door slowly, and are immediately faced with 5 monsters. You scream, and notice a weapon on the floor. You pick it up, and get ready to fight. \n")
    else:
        print("Invalid input. Please enter Y or N.")
        enter()

def combat():
    health = 100
    monsterhealth = 50
    damage = 10

#with open('user_data.json', 'w') as json_file:
 #   json.dump(user_data, json_file, indent=4) # 'indent=4' makes the file human-readable

enter()



with open('data.json', 'r') as json_file:
    data = json.load(json_file)
for n in data["listy"]:
    print(n)