#!/usr/bin/env python3
# 


for x in range (1,101) :
    if not x % 3 and not x % 5 :
        print("FizzBuzz")
    elif not x % 3:
        print("Fizz")
    elif not x % 5:
        print("Buzz")
    else:    
        print("The number is :",x)


print("\nOur loop has ended.")  # when the loop ends print this

