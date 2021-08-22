import json
from pathlib import Path
import pandas as pd

#Open Response File From Main Script.
f_str = Path("C:\\Users\\burketaylor\\Desktop\\linker\\issues.json").read_text("utf-8")

#Turn String Data From File Into JSON Object.
f_json = json.loads(f_str)

#Check Who Accepted The PEI Pass.
def checkWho(issue):
    #Go Through Change History.
    for history in reversed(issue['changelog']['histories']):
        #Go Through Each Item In Change History.
        for item in reversed(history['items']):
            #Check If It Was Changed To Accepted.
            if item['toString'] == 'PEIP Partial Vaccination' or item['toString'] == 'PEIP Full Vaccination':
                #Return Name Of Who Changed It.
                return [history['author']['name'], issue['key']]

people = {}

#Go Through All Required Issues And Check Who Accepted Them.
for issue in f_json['issues']:
    who = checkWho(issue)
    if who[0] in people:
        people[who[0]].append(who[1])
    else:
        people[who[0]] = []
        people[who[0]].append(who[1])

excel_path = r"C:\Users\burketaylor\Desktop\linker\export.xlsx"

data = pd.DataFrame.from_dict(people, orient='index')

data = data.transpose()
data.to_excel(excel_path)