import json
import requests
import csv


request = requests.get("http://45.148.145.173/csv_data")
csv_data = []
for data in request.json():
    row = {}
    if data["isActive"]:
        row["name"] = data["name"]
        row["age"]= data["age"]
        row["gender"]= data['gender']
        row["company"]= data['company']
        row["email"]= data['email']
        row["phone"]= data['phone']
        row["address"]= data['address']
        row["balance"]= data['balance']
        csv_data.append(row)


# header = json_data.keys()
fieldnames = ["name", "age", "gender" , 'company','email', 'phone', 'address', 'balance']
csv_file = open('file.csv', "w", newline="")
write = csv.DictWriter(csv_file, fieldnames=fieldnames)
write.writeheader()
write.writerows(csv_data)