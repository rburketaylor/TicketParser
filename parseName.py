import json
from pathlib import Path

#Open Response File From Main Script.
f_str = Path("D:\\Code\\TicketParser\\issues.json").read_text("utf-8")

#Turn String Data From File Into JSON Object.
f_json = json.loads(f_str)

#Check Who Accepted The PEI Pass.
def checkWho(issue):
    #Go Through Change History.
    for history in reversed(issue['changelog']['histories']):
        #Go Through Each Item In Change History.
        for item in reversed(history['items']):
            #Check If It Was Changed To Accepted.
            if item['toString'] == 'PEIP Partial Vaccination' or item['toString'] == 'PEIP Full Vaccination' or item['toString'] == "Duplicate":
                #Return Name Of Who Changed It.
                return issue['key'] + " - " + history['author']['name']

#Go Through All Required Issues And Check Who Accepted Them.
count = 0

for issue in f_json['issues']:
    temp = checkWho(issue)
    if temp.find('burketaylor') != -1:
        count += 1
        print(temp)
print('You didn\'t assign yourself ' + str(count) + ' times.')