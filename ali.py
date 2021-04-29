#!/usr/bin/env python3


Alifav  = {"name":{"birth":"Cassius Clay","current":"Muhammad Ali"},"contact":{"phone":"333-444-5555","email":"thebest@boxing.com"},"favorites":{"number":56,"food":{"baked chicken":3.5,"mac and cheese":4.5,"spinach":2,"green peas":2},"drink":{"adult":["none"],"nonadult":["Mr. Champ soda"]}}}

print(" Ali's favorite food is:", Alifav["favorites"]["food"].keys())

print(" Ali's favorite food is:", Alifav["favorites"]["food"].values())

Amount = 0

for x in Alifav["favorites"]["food"].values():
    Amount = Amount + x

print(" The cost of the foos is:" ,Amount)

Amount2 = 0.0
FoodCost = Alifav.get("favorites").get("food").values()

for x in FoodCost :
    print(f"the value of x {x}")
    Amount2 = Amount2 + float(x)

print(f" The cost of the foods is: {Amount2}")


