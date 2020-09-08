import Solution_Final
import json


# def main():
# Accept  input for the name of the team member  who plan to go out for food+drinks
membersgoing = [(n) for n in input(
    'Enter Team Member name who plan to go for food+drinks:').split(',')]
UserFile = './users.json'
VenueFile = './venues.json'
print(json.dumps(Solution_Final.Solution(
    membersgoing, UserFile, VenueFile), indent=4))

#   if __name__ == "__main__":
#      main()
