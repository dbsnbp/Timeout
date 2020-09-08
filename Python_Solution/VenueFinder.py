import Utils
import json
import os

def Solution(membersgoing,user_file,venue_file):
    
    users = Utils.ReadJsonFile(user_file)
    venues = Utils.ReadJsonFile(venue_file)
    
    # Set defaults for the variables to be used for the processing
    venues_going = []
    reasons_notgoing = []
    output = {}

    # Loop through the venue:
    # Loop through each member going:
    # Populate a dictionary  for each with the Venue as key and reasons for each user going or not going.
    # Filter the venues where there is no reason as valid venues where all members can go
    # Filter the venues where is atleast one reason for any user not to go.These venues are those where all members cannot go.
    # Perform formatting to show the output as desired.
    for v in venues:
        # Dictionary to store venue as key & list of reasons as  values.Reasons would be blank for valid venues a each can go,non-blank value for venues where a
        # user cannot go.
        dict_nvg = {}
        # Default the dictionary name to the venue name
        dict_nvg['name'] = v['name']
        dict_nvg['reason'] = []
        # Populate the reasons for each venue where a user cannot go. In case if a user can go then the value would be blank.
        for u in users:
            if u['name'] in membersgoing:

                # Normalise the data & convert them to lowercase so as to do comparison
                # Convert the list into set for finding common drinks or food items between a venue and user
                userwonteat_ , venueeat_ = set(Utils.CleanStringData(u['wont_eat'])), set(Utils.CleanStringData(v['food']))
                userdrink_ , venuedrink_ = set(Utils.CleanStringData(u['drinks'])), set(Utils.CleanStringData(v['drinks']))
                # Check if there is one food item  available at a venue for the user to eat
                if bool(userwonteat_ & venueeat_) == True:
                    dict_nvg['reason'].append(
                        'There is nothing for  '+u['name'].split()[0] + ' to eat.')
                # Check if there is one drink item  available at a venue for the user to drink.
                if bool(userdrink_ & venuedrink_) == False:
                    dict_nvg['reason'].append(
                        'There is nothing for  '+u['name'].split()[0]+' to drink.')
                    # print('User '+u['name'].split()[0] +' have nothing to drink at '+v['name'])

        # Populate the list reasons_notgoing with the list of dictionary storing venue & the reasons why each user cannot go to the venue
        if dict_nvg['reason']:
            reasons_notgoing.append(dict_nvg)
        # Populate the list venues_going with the list of venue names where all users can go
        else:
            venues_going.append(dict_nvg['name'])
    output["places to visit"] = venues_going
    output['places to avoid'] = reasons_notgoing

    return json.dumps(output,indent=4)



