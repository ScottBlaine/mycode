#!/usr/bin/env python3
heroes=  {
    "wolverine":
        {"real name": "James Howlett",
         "powers": "regeneration",
         "archenemy": "Sabertooth",},
   "harry potter":
       {"real name": "Harry Potter",
        "powers": "magic",
        "archenemy": "Voldemort",},
   "captain america":
      {"real name": "Steve Rogers",
       "powers": "frisbee shield",
       "archenemy": "Hydra",}
                        }

char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)?")
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)?")

print("The character:", char_name.title()," ", char_stat, "is", heroes[char_name][char_stat])



