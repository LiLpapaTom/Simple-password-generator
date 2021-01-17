#Thomas Papaloukas, ICSD14155
import string
import random

print("Please fill the elements bellow.\n")
list = []
pwd_list = []
pass_len = 0
pwd = ""
password =""
filled = ""

var = input('What\'s your fav colour? ')
pass_len += len(var)
list.append(var)
var = input('What\'s your pet\'s name? ')
pass_len += len(var)
list.append(var)
var = input('What\'s your fav number? ')
pass_len += len(var)
list.append(var)
#Until user doesnt want to generate more passwords
while True:
    pwd_len = input("Whats the desired pwd's length?(length recommended above 8 characters) ")
    #For every element in list, change certain characters to special characters
    for y in range(3): #For every list item
        for x in range(pass_len): #For every item, change characters to special ones
            if x < len(list[0])+2:
                if list[y][x:x+1] == 'a':
                    pwd = pwd + "@"
                elif list[y][x:x+1] == 'i':
                    pwd = pwd + "!"
                elif list[y][x:x+1] == "e":
                    pwd = pwd + "3"
                elif list[y][x:x+1] == "o":
                    pwd = pwd + "0"
                elif list[y][x:x+1] == "s":
                    pwd = pwd + "$"
                else:
                    pwd = pwd + list[y][x:x+1]
    #In case the elements the user filled, are less than the password's
    #desirable length, fill the rest cells with random generated chars/nums
    if (int(len(pwd)) < int(pwd_len)):
        fill = int(pwd_len) - int(len(pwd))
        for x in range(fill): #Remaining cells that have to be filled
            filled = filled + random.choice(string.ascii_letters + string.digits)
        password = pwd + filled
    #In case the elements are larger than the desirable password's size
    #keep the elemnts that corespond to the desirable length
    else:
        password = pwd[0:int(pwd_len)]

    print("Generated password: " + password)
    pwd_list.append(password)
    var =input("Generate more passwords?(y/n)")
    #If user is happy with the generated passwords (y), the programm exits
    #displaying the total passwords generated, else keep entering desirable
    #password lengths to generate more passwords
    pass_len = 0
    password =""
    filled = ""

    if var == 'n':
        print("\nGenerated passwords:")
        print(pwd_list)
        break
