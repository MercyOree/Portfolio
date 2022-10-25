# Mercy Oreoluwa koku
# Oct/18/2022
# Program helps compute MPG for a car.

miles = float(input("How many miles were driven on your recent trip?"))
gallons = float(input("How many gallons of gas were use?"))
mpg = (miles / gallons)
#solve MPG

print("Your car offers", mpg, "miles per gallon of fuel.")

if (mpg < 30):
    # messages based on what MPG value is
    print("Try Again")
if (mpg>30 and mpg<80):
    print("Almost there")
if (mpg>80):
    print("You did it")