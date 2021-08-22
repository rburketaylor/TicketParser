import requests

#API Endpoint.
url = 'https://jira.gpei.ca/rest/api/2/search'

#Authentication Header.
headers = {
    "Accept": "application/json",
    "Cookie": "JSESSION-ID Goes Here"
}

#JQL Query With Restrictions To Just Required Fields And Project.
query = {
    "fields": "key",
    "expand": "changelog",
    "maxResults": 4000,
    "jql": """
        project = "PEIP" AND
        issuetype = "COVID PEI Pass" AND 
        status in ("PEIP Full Vaccination", "PEIP Partial Vaccination", "Duplicate") AND 
        assignee in (EMPTY) 
        ORDER BY created ASC
    """
}

#API Call.
response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

#Write Response To File.
f = open("D:\\Code\\TicketParser\\issues.json", 'w', encoding='utf-8')
f.write(response.text)