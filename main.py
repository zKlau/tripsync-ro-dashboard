import random

fem_ = open("female-names-list.txt", "r")
fem_names = fem_.readlines()

mal_ = open("male-names-list.txt", "r")
mal_names = mal_.readlines()

sur_ = open("surnames-list.txt", "r")
sur_names = sur_.readlines()

name_list = []
line = 0

for i in range(1000):
    name = fem_names[random.randrange(0,1000)].replace("\n"," ")
    surname = sur_names[random.randrange(0,1000)].replace("\n"," ")
    name_list.append(f"{name}{surname}")
    line += 1
    
for i in range(1000):
    name = mal_names[random.randrange(0,1000)].replace("\n"," ")
    surname = sur_names[random.randrange(0,1000)].replace("\n"," ")
    name_list.append(f"{name}{surname}")
    line += 1

print(name_list)

with open('names.txt', 'w') as f:
    for line in name_list:
        f.write(line + '\n')
        print(line)