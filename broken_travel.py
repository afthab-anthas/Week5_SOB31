# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) ##Afthab M01033122

if year <= 1900: ##Afthab M01033122
    print("Woah, that's the past!") ##Afthab M01033122
elif year > 1900 and year < 2020: ##Afthab M01033122
    print ("That's totally the present!")
elif year >= 2020: ##Afthab M01033122
    print ("Far out, that's the future!!")
