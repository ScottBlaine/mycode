#!/usr/bin/env python3

#Create the Michigan dictionary
Michigander = {"pop":["Vernors", "Faygo", "Town Club"],
                "auto makers":["Chrysler", "General Motors", "Ford"],
                "coney dog":["Lafayette", "American"],
                "Michmap":"Hand"
                }
print (Michigander.keys())

print (Michigander.values())

#Welcome to the Michigander Test

Tryagain = "Y"

while Tryagain == "Y":
  print(" This is a test to determine if you are a true Michigander")
  print("Please enter the questions to determine if you are can call yourself a Michigander")

  
  Count = 0
  print("One of the Big Three automakers is?")
  car = input(">>>").lower().title()
  print(car)
  if (car in Michigander["auto makers"]):
     Count = Count + 1
     print("You entered a correct car maker")
  else:
     print("That's not from Michigan!")

  print("A Detroit manufacturer of soft drinks is")
  pop = input(">>>").lower().title()
  print (pop)

  if (pop in Michigander["pop"]):
      Count = Count + 1
      print("Good pop choice")
  else:
      print("I bet you call software drinks Soda")

  print("Enter one of the original two places to eat coney dogs in downtown Detroit?")  
  coney = input(">>>").lower().title()
  print(coney)
  
  if (coney in Michigander["coney dog"]):
      Count = Count + 1
      print("Yummy")
  else:
      print("Yuk")

  print("What body part does a Michigander use as a map?")
  map = input(">>>").lower().title()
  print(map)

  if (map == Michigander["Michmap"]):
      Count = Count + 1
      print("You know how to get around Michigan")
  else:
      print("I think you are lost")

  if (Count == 4):
      print("You are a true Michigander")
  else:
      print("Sorry I think you are from New York")
  print("Would you like to try again Y/N")
  Tryagain = input("<<<")
  

