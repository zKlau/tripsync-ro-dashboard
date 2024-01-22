import json
import random
import csv

# List of months
months = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]

# List of capitals
capitals = [
    "Alba Iulia", "Arad", "Bacau", "Buzau", "Baia Mare", "Bistrita", "Botosani",
    "Braila", "Brasov", "Bucharest", "Calarasi", "Cluj-Napoca", "Constanta",
    "Craiova", "Deva", "Drobeta-Turnu Severin", "Focsani", "Galati", "Giurgiu",
    "Hunedoara", "Iasi", "Miercurea Ciuc", "Oradea", "Piatra Neamt", "Pitesti",
    "Ploiesti", "Ramnicu Valcea", "Resita", "Satu Mare", "Sfantu Gheorghe",
    "Sibiu", "Slatina", "Slobozia", "Suceava", "Tulcea", "Targoviste", "Targu Jiu",
    "Timisoara", "Tirgu Mures", "Vaslui", "Zalau"
]

# Read names from file
with open('names.txt', 'r') as file:
    names = [line.strip() for line in file]

# Generate a flat list of records
records = []
for county in capitals:
    for month in months:
        for _ in range(random.randint(10, 30)):
            user_name = random.choice(names)
            vacation_length = random.randint(1, 15)
            record = {
                "county": county,
                "month": month,
                "user_name": user_name,
                "vacation_length": vacation_length
            }
            records.append(record)

# Write records to CSV file
csv_columns = ["county", "month", "user_name", "vacation_length"]
csv_file = "output2.csv"
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for record in records:
        writer.writerow(record)

# Write records to JSON file (optional)
json_data = {"records": records}
json_file = "output2.json"
with open(json_file, 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=2)
