import json
import random

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

# Generate random number of users (between 10 and 30) for each month
json_data = {
    "counties": {
        county: {
            "months": {
                month: {
                    "users": {random.choice(names): random.randint(1, 15) for _ in range(random.randint(10, 30))}
                } for month in months
            }
        } for county in capitals
    }
}

# Write JSON to file
with open('output.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=2)
