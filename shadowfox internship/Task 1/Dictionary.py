                                # DICTIONARY TASK IN Beginner Level
#-------------------------------------------------------------------------------------------------------------------#

# 1. Create a list of your friends' names. The list should have at least 5 names. Create a list of tuples.
#    Each tuple should contain a friend's name and the length of the name.
#    For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)


friend_name_list = ["sunny","Hemanth","saideep","praneeth","sreekar"]

friend_name_length = [(name, len(name)) for name in friend_name_list]

print(friend_name_length)

#--------------------------------------------------------------------------------------------------------------------#

'''
2.You and your partner are planning a trip, and you want to track expenses. 
Create two dictionaries, one for your expenses and one for your partner's expenses. 
Each dictionary should contain at least 5 expense categories and their corresponding amounts.
For example:
Your expenses
your_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}
Your partner's expenses
partner_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}
Calculate the total expenses for each of you and print the results.
Determine who spent more money overall and print the result.
Find out the expense category where there is a significant difference in spending between you and your partner.
Print the category and the difference.
'''

# Create two dictionaries, one for your expenses and one for your partner's expenses. 

sreekar = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

Nithin = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

#------------------------------------------------------------------------------------------------------------------#

# Calculate the total expenses for each of you and print the results.


t_sreekar_exp = sum(sreekar.values()) 
print(f"The total expense of Nitin is {t_sreekar_exp}")
t_Nithin_exp = sum(Nithin.values())
print(f"The total expense of sreekar is {t_Nithin_exp}")

#------------------------------------------------------------------------------------------------------------------#

# Determine who spent more money overall and print the result.

if t_Nithin_exp > t_sreekar_exp :
    print("sreekar has spent more than Nithin" )
elif t_sreekar_exp < t_Nithin_exp :
    print("sreekar has spent more than Nitin")
else :
    print("Both spent the same amount")

#------------------------------------------------------------------------------------------------------------------#

# Find out the expense category where there is a significant difference in spending between you and your partner.

for catogory in sreekar :
    if sreekar != Nithin :
        difference = (sreekar[catogory] - Nithin[catogory])
        print(f"The Difference in {catogory} is {difference}")
    
#-------------------------------------------------------------------------------------------------------------------#