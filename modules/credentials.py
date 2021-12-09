#!/usr/bin/env python3
import os

#Clear screen
def clear():
    os.system("clear")

#Menu
def menu():
    print("1- Enter credentials")
    print("2- Restore credentials")
    option = input("[+] Input option [1-2]: ")

    if option == "1":
        return "1"
    elif option == "2":
        return "2"
    else:
        print("Invalid option")
        input("Press [ENTER] to continue...")
        clear()
        menu()

#Encrypt
def encrypt(string):
    new_string = str()
    for x in range(0, len(string)):
    	new_string += chr(ord(string[x])+7)
    return new_string

#Decrypt
def decrypt(string):
    new_string = str()
    for x in range(0, len(string)):
	    new_string += chr(ord(string[x])-7)
    return new_string

#Input
def input_credentials():
    username = input("- Input username: ")
    password = input("- Input password: ")
    return username, password

#Save
def save_credentials(username, password):
    save = input("Do you want to save the credentials for the next time ?[y/n]")
    if save == "y":
	    with open("credentials.txt", "w") as file:
		    file.write(f"{username}\n")
		    file.write(f"{password}")
	    print(f"Credentials saved in '{os.getcwd()}/credentials.txt'")
    elif save == "n":
	    pass
    else:
	    print("Invalid option [!]")
	    input("Press [ENTER] to continue...")
	    clear()
	    save_credentials(username, password)

#Restore
def restore_credentials():
    with open(f"{os.getcwd()}/credentials.txt", "r") as file:
	    username = file.readline()
	    password = file.readline()
    return username, password
