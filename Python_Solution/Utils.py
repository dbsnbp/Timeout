"""This file contains utility functions required for data processing."""

import json

def ReadJsonFile(f):
    """Reads a json data file & outputs the data."""
    with open(f, "r") as json_file:
        data = json.load(json_file)
    return data

def CleanStringData(lst):
    """Lowercase all the items in the input list."""   
    output_lst = []
    for item in lst:
        output_item = item.lower()
        output_lst.append(output_item)
    return output_lst


def SearchInJson(search_item,search_value,json_output):
    """It searches a json file data for the search_item & passes the whole dictionary for that search item"""
    pass






