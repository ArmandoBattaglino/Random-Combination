import random
from probability import *

chosen_file = "namess.txt"
#chosen_file = input("Choose the txt file to lookup for names: ")

with open("result.txt", "w") as f:
  f.write("")

with open(chosen_file, "r") as f:
  lines = f.readlines()
  names = [name.strip() for name in lines]

teams = []

with open("result.txt", "a") as f:
  for x in range(3):
    f.write(f"TEAM {str(x+1)}")
    f.write("\n")
    temp_team = []
    for x in range(7):
      temp_choice = random.choice(names)
      temp_team.append(temp_choice)
      names.remove(temp_choice)
      f.write(temp_choice)
      f.write("\n")
    f.write("\n")
    teams.append(temp_team)

  teamleaders = []
  for x in teams:
    teamleaders.append(random.choice(x))

  f.write("TEAMLEADERS:")
  f.write("\n")
  for x in teamleaders:
    f.write(x)
    f.write("\n")


with open("result.txt", "r") as f:
  file = f.read()

print(file)
