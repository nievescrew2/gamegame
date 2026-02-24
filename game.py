import random
import json


namelist = ["Spencer", "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Riley", "Jamie", "Drew", "Cameron"]
countrylist = ["America", "Canada", "England", "Australia", "Germany", "France", "Italy", "Spain", "Japan", "China", "Fakecountrya"]
joblist = ["rodeo clown", "jazz trombonist", "professional dog walker", "trash novelist"]
herotypelist = ["rapid resonse hero", "espionage hero", "rescue and recovery hero", "crowd control hero", "disaster relief hero", "hacker hero", "celebrity hero", "sandwich gyro"]
villaintypelist = ["supervillain", "politician", "CEO of a Fortune 500 company", "bad teacher", "Jake Paul", "secret villain", "fashion villain", "environmental villain", ]

name = random.choice(namelist)
country = random.choice(countrylist)

print(f"You were born. You parents named you {name}. \n")
print(f"You are from {country}.")