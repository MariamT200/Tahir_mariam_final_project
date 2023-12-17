import sys 

sys.argv
if sys.argv[0] == "Tahir_mariam_final_project.py":
    print("This is the name of the program:", sys.argv[0] )
if len(sys.argv) > 1:
    print(sys.argv[1])

#item 5.7 creat a list manually

my_favorite_numbers = [2, 3, 5, 7, 21, 18]

#item 5.8 you appended an item to a list 

my_favorite_numbers.append("36") #I am adding "36" to my_favorite_numbers list
print(my_favorite_numbers)

#item 5.10 you removed an item from a list

my_favorite_numbers.remove("36") # I am removing "36" from my_favorite_numbers list
print(my_favorite_numbers)

#items 5.9 and 5.11 you appended/removed an item from a list iteratively, I am doing it through a for loop

new = [] #I will create an empty list in order to add items from an existing list through a loop
def new_list(x):
    for item in range(len(x)): 
        if x[item] < 10:   #add numbers under 10
            new.append(x[item])
        if x[item] == 2: #remove any number equal to 2
            new.remove(x[item])
    return new #this is so it doesn't repeadetly go through the loop

result = new_list(my_favorite_numbers)
print(result)

#item 5.12 you created a tuple manually 
my_tuple = ("bob", "stewy", "roman", "ken", "logan")

#item 5.13 you assigned tuple members to seperate variables in one assignmenr statement
(family, friends, *teachers) = my_tuple #assigning the tuple values to variables
print(family)
print(friends)
print(teachers)
#item 5.14 you used a tuple to return multiple values from a function 
# I created a simple math function so I can fulfill this requirement 

def number_function(num1, num2):
    result = num1 * num2
    result_2 = num1 % num2
    return result, result_2

number_function(2, 6) #this returns a tuple 

#item 5.15 you created a dictionary manually

job_salaries = {"librarian": 40000, "electrician": 70000, "chef": 75000}

#item 5.17 you accessed the keys of a dictionary
print(job_salaries.keys()) 

#item 5.18 you iterated through items of a dictionary to access both keys and values
job_salaries.keys()
job_salaries.values()
job_salaries.items()

for jobsalary in job_salaries.items():
    print(f"Being a {jobsalary[0]} makes ${jobsalary[1]} yearly")

#item 5.19 you updated values in a dictionary programmatically
new_dict = {}
#i created a list with the dictionary listed inside it
dict_list = [{"librarian": 40000, "electrician": 70000, "chef": 75000}]
#now i can update the new dictionary with the values from the dictionary list
for jobsalary in dict_list:
    new_dict.update(jobsalary)

print("new dictionary", new_dict)


#3.19 you read user input from a file to use in your program
#import os
#os.getcwd()
# C:\Users\Tahir\OneDrive\Desktop\test\user_file.txt

user_file_directory = input("what is the path directory to your file: ")

user_file = open(user_file_directory, "r")
list_data = user_file.read()
user_data_list = list_data.split("\n")
print(user_data_list)
user_file.close()


