#code attribution
#author: Zahava Gopin
#title: gopin_hobbies.py
#description: list of hobbies and days
#date: 10 April 2023

#list of at least 5 hobbies
hobbies = ["Running", "Piano", "Reading", "Drawing", "Cooking"]
#a for loop to iterate over the list of hobbies and print them to the console window
for hobby in hobbies:
    print(hobby)

#list of days 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#a for loop to iterate over the list of days, an if…else statement to display what the day is with appropriate message. 
for day in days:
    if day == "Sunday":
        print("Today is Sunday, enjoy your hobbies.")
    else:
        print("Today is {}, its a work day.".format(day))

        
