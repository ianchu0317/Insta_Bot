from time import sleep
from modules import credentials
import os

#Declare variables: the username and the password of the user
username = str()
password = str()

def clear():
    os.system("clear")
'''
def options():
    print("1- Follow")
    print("2- Like")
    print("3- Comment\n")
    option = input("-Enter option [1-3]: ").lower().strip()

    if option == "1":
        return option
    elif option == "2":
        return option
    elif option == "3":
        return option
    else:
        print("[+] Invalid option!")
        input("[+] Press enter to continue..")
        clear()
        options()
'''


if __name__ == "__main__":
    option = credentials.menu()
    if option == "1":
        username, password = credentials.input_credentials()
        username = credentials.encrypt(username)
        password = credentials.encrypt(password)
        credentials.save_credentials(username, password)
        username = credentials.decrypt(username)
        password = credentials.decrypt(password)
        username = username[:-1]
    elif option == "2":
        username, password = credentials.restore_credentials()
        username = credentials.decrypt(username)
        password = credentials.decrypt(password)

    from modules import automation
    automation.sign_in(username, password)
    sleep(2)
    automation.follow()
