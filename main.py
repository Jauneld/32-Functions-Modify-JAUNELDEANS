#Jaunel Deans
#October 13, 2023
#In this program we renamed the function so that it has a sensible name. Then it got the user to input a country. Store it in a variable. Call the function again with the variable as the parameter.

name = input("Hello. What is your name user? ") #ask for the user to input their name
origin = input("That is a nice name. What country are you from? ") #ask for the user to input their place of origin


def place(country):#rename the function my_function to place
  print(name + " is from " + country) #added the variable name to make that answer more personal


place(origin)#change the name of the function to place to it can work without errors and made a universal variable that will take the input that the user used in place of a parameter


