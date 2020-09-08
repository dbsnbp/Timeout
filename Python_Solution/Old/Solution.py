# Import the module to parse the json files.
import urllib.request
import json

# Accept  input for the name of the team member  who plan to go out for food+drinks
#membersgoing = [(n) for n in input('Enter Team Member name who plan to go for food+drinks:').split(',')]
membersgoing = ['Gary Jones', 'John Davis', 'Robert Webb']

print(membersgoing)

# read json files
users = json.load(open('users.json'))
venues = json.load(open('venues.json'))


# print(users)
# print(venues)

venues_prev = [item['name'] for item in venues]
v_venues = []
venues_notgoing = {}
for u in users:

    if u['name'] in membersgoing:
        #print("Printing u")
        # print(u)
        for v in venues:

            #print("Printing v")
            # print(v)
            userwonteat_, venueeat_ = map(
                set, [map(str.lower, set(u['wont_eat'])), map(str.lower, set(v['food']))])
            #print("printing userwonteat,venueeat")
            #print(userwonteat_, venueeat_)
            userdrink_, venuedrink_ = map(
                set, [map(str.lower, set(u['drinks'])), map(str.lower, set(v['drinks']))])

            if bool(userwonteat_ & venueeat_) == False and bool(userdrink_ & venuedrink_) == True:
                v_venues.append(v['name'])

            if bool(userwonteat_ & venueeat_) == True:
                if v['name'] in venues_notgoing.keys():
                    venues_notgoing[v['name']].append(
                        'There is nothing for '+u['name']+' to eat.')

            if bool(userdrink_ & venuedrink_) == False:
                if v['name'] in venues_notgoing.keys():
                    venues_notgoing[v['name']].append(
                        'There is nothing for '+u['name']+' to drink')
                else:
                    venues_notgoing[v['name']] = [
                        'There is nothing for '+u['name']+' to drink']
output = {}
# print(venues_notgoing)
output['places_to_visit'] = list(set(v_venues))
output['places_to_avoid'] = venues_notgoing
print(output)

#print("Venues not going")
# print(venues_notgoing)
#print("Venues going")
# print(v_venues)
