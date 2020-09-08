import VenueFinder
import json
def run():
    membersgoing = [(n) for n in input(
        'Enter Team Member name who plan to go for food+drinks:').split(',')]
    UserFile = 'files/input/users.json'
    VenueFile = 'files/input/venues.json'
    print(VenueFinder.Solution(
        membersgoing, UserFile, VenueFile))

if __name__=="__main__":
    run()