
import VenueFinder
import json

def run():
    """ This function calls the VenueFinder functionality to get recommendations for venues to visit based on members planning to go.
        It takes inputs of the list of members planning to go, reference user file, reference venue file."""
    membersgoing = [(n) for n in input(
       'Enter Team Member name who plan to go for food+drinks:').split(',')]
    UserFile = 'files/input/users.json'
    VenueFile = 'files/input/venues.json'
    print("Output:")
    print(VenueFinder.Solution(
        membersgoing, UserFile, VenueFile))

if __name__=="__main__":
    run()