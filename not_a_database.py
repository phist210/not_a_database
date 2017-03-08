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

    def __repr__(self):
        user_list = []
        with open('not_the_database.txt', "r") as csvfile:  # display database
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                user_list.append(row)
            for credentials in user_list:
                print(credentials)

    def __str__(self):
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
            if len(user_list) < 1:  # easy access if database is empty
                return True
            for row in reader:
                user_list.append(row)
            for credentials in user_list:
                if credentials[0] == username and credentials[1] == password:
                    return True


def main(user):

        print("\nWhat would you like to do?")
        print("\t1) Add a user to the database")
        print("\t2) View database")
        print("\t3) Logout")
        print("\t4) Quit")

        prompt = input("\nChoose from menu: ")
        if prompt == '1':
            while prompt:
                clear()
                print("Adding new entries to database...")
                user.username = input("Enter a username: ")
                if user.__str__() is True:
                    if user.username in user.__str__():
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
                if input:
                    login()

        elif prompt == '2':  # prints current database
            if user.__str__() is True:
                user.__repr__()
            else:
                print("No entries to show.")
            input("Hit ENTER to return to menu. ")
            if input:
                main(user)

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
    if user.login(username, password):
        print("\nLogin successful, here is your menu.")
        main(user)
    else:
        print("\nInvalid inputs, try again.")
        time.sleep(1.2)
        login()


if __name__ == "__main__":
    login()
