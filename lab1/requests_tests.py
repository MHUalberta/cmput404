import requests

#Get version
print(requests.__version__)
print()

#GET request
response1 = requests.get("https://www.google.com/")
print(response1)
print()

#Print from github
response2 = requests.get("https://raw.githubusercontent.com/MHUalberta/CMPUT404/main/labs/lab1/requests_tests.py?token=GHSAT0AAAAAAB5BAD352OD6GUHRO4GTUWLSY546EDA")
print(response2.text)
print()