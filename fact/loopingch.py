#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
                      {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
Farm = farms[0]  
for animals in Farm["agriculture"]:
    print(animals)

InFarm = input("what farm are you interested in: NE Farm, W Farm, SE Farm?")
if InFarm == "W Farm":
    Index = 1
elif InFarm == "NE Farm":
    Index = 0
elif InFarm == "SE Farm":
    Index = 2
else:
    print("Invalid Value")

for animals in farms[Index]["agriculture"]:
    print(animals)

print()

for animals in farms[Index]["agriculture"]:
    if animals != "carrots" :
        if animals != "celery":
            print(animals)

