import json


def ReadJson(file):
    with open(file, "r") as json_file:
        data = json.load(json_file)
    return data


def NormaliseData(lst):
    normalised_list = []
    for item in lst:
        normalisted_item = item.lower()
        normalised_list.append(normalisted_item)
        return normalised_list


d = ["d2", "d3", "d4", "Whisky", "Cider"]
e = NormaliseData(d)
print(e)
