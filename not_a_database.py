import os
import time
import csv
import getpass

"""  to add extra funtionality, make __str__ enumerate its lists
(maybe a dictionary with entries as values and an incrementing number key)
from there give the option
to update entries
add password strengening
"""


def clear():
    os.system("clear")


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_database(self):  # don't
        user_list = []
        with open('not_the_database.txt', "r") as csvfile:  # display database
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                user_list.append(row)
            for credentials in user_list:
                print(credentials)

    def check_login(self):  # don't
        user_list = []
        with open('not_the_database.txt', "r") as csvfile:  # display database
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                user_list.append(row)
            for credentials in user_list:
                return credentials

    def add_new_entry(self, username, password, full_name, date_of_b):
        user_list = [self.username, self.password,
                     self.full_name, self.date_of_b]
        with open("not_the_database.txt", "a") as database:  # update database
            database.writelines(','.join(user_list))
            database.write("\n")

    def login(self, username, password):
        user_list = []
        with open('not_the_database.txt', "r") as csvfile:  # verify login
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                user_list.append(row)
                if len(user_list) == 0:  # easy access if database is empty
                    return True
            for credentials in user_list:
                if credentials[0] == username and credentials[1] == password:
                    return True


def update_database(user):
    while True:
        clear()
        print("Adding new entries to database...")

        user.username = input("Enter a username: ")
        if user.check_login() is True:
            if user.username in user.check_login():
                print("Username is unavailable, try again.")
                time.sleep(1.2)
                continue

        user.password = input("Enter password: ")

        user.full_name = input("Enter full name for user: ")

        user.date_of_b = input("Enter DOB (MM/DD/YYYY): ")

        if not 8 <= len(user.date_of_b) <= 10:
            print("Invalid DOB, try again.")
            time.sleep(1.2)
            continue

        else:
            user.add_new_entry(user.username,
                               user.password,
                               user.full_name,
                               user.date_of_b)

        print("Added {} to database.".format(user.full_name))
        input("Hit ENTER to return to menu. ")
        menu(user)


def menu(user):
        print("\nWhat would you like to do?")
        print("\t1) Add a user to the database")
        print("\t2) View database")
        print("\t3) Logout")
        print("\t4) Quit")
        prompt = input("\nChoose from menu: ")

        if prompt == '1':  # add new entry
            update_database(user)

        elif prompt == '2':  # prints current database
            print(user.display_database())
            input("Hit ENTER to return to menu. ")
            menu(user)

        elif prompt == '3':  # logout
            login()

        elif prompt == '4':  # quit program
            exit()


def login():
    clear()
    print("\t\t\tWelcome.")
    print("\tProvide the correct login information.\n")
    username = input("Please, enter your username: ")
    password = getpass.getpass("...and your password: ")
    user = User(username, password)

    if user.login(username, password):  # fix
        print("\nLogin successful, here is your menu.")
        menu(user)

    else:
        print("\nInvalid inputs, try again.")
        time.sleep(1.2)
        login()


if __name__ == "__main__":
    login()
