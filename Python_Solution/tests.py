import VenueFinder
"""Scenario 1:Food No,Drink Yes """
print("Testing Scenario 1:Food,Drink Available")
    membersgoing = [(n) for n in input(
        'Enter Team Member name who plan to go for food+drinks:').split(',')]
    UserFile = 'files/tests/users.json'
    VenueFile = 'files/tests/venues.json'
    print(VenueFinder.Solution(
        membersgoing, UserFile, VenueFile))
"""Scenario 2:Food Yes,Drink No """

"""Scenario 3:Food Yes,Drink Yes """



