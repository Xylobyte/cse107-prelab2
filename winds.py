#CSE 107, Prelab 2, Exercise 3.2 Annika Davenport and Donovan Griego
wind = int(input("Please enter a wind speed as a whole number. ")) 

if 0 < wind < 1:
    print("All is calm. You feel nothing.")
    
elif 1 <= wind <= 3:
    print("There is light air brushing your beautiful face.")

elif 4 <= wind <= 27:
    print("It's breezy. You're a magazine model.")

elif 28 <= wind <= 47:
    print("You've found yourself in a gale. Hope you aren't on a boat. :) ")

elif 48 <= wind <= 63:
    print("This is a storm. Go inside.")

elif wind > 63:
    print("A hurricane and/or tornado has developed in your area. :( ")

else:
    silly = (str(wind) + " is not a valid wind speed.")
    print(silly)