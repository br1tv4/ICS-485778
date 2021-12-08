import json
from pokanzyki import nounlist1
from dovidnyk import nounlist2

def convertToJSON():
    with open("1.json", "w") as write_file:
        json.dump(nounlist1, write_file)


def convertInJSON():
    with open("2.json", "w") as write_file:
        json.dump(nounlist2, write_file)