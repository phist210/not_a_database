import os
import re
import time
import csv


def clean_sentence(sentence):
    return re.sub(r'[^A-Za-z]', '', sentence.lower())


def clear():
    os.system("clear")


class User:
    def __init__(self, username, password, full_name=None):
        self.username = username
        self.password = password
        self.full_name = full_name

    def __str__(self):
        user_list = []
        with open('not_the_database.txt', "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                user_list.append(row)
            for credentials in user_list:
                print(credentials)

    def add_new_entry(self, username, password, full_name):
        user_list = [self.username, self.password, self.full_name]
        with open("not_the_database.txt", "a") as database:
            database.writelines(','.join(user_list))
            database.write("\n")

    def login(self, username, password):
        user_list = []
        valid_users = []
        with open('not_the_database.txt', "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                user_list.append(row)
            for credentials in user_list:
                if credentials[0] == username and credentials[1] == password:
                    valid_users.append(user_list)
            if valid_users:
                return True
            else:
                return False


def main(user):

        print("\nWhat would you like to do?")
        print("\t1) Add a user to the database")
        print("\t2) View database")
        print("\t3) Logout")

        prompt = input("\nChoose from menu: ")
        if prompt == '1':  # add to database
            clear()
            print("Adding new entries to database...")
            user.username = input("Enter a username: ")
            user.password = input("Enter password: ")
            user.full_name = input("Enter full name for user: ")

            user.add_new_entry(user.username.strip(), user.password.strip(), user.full_name)
            print("Added {} to database.".format(user.full_name))
            input("Hit ENTER to return to menu. ")
            if input:
                login()

        elif prompt == '2':  # prints current database
            user.__str__()
            input("Hit ENTER to return to menu screen. ")
            if input:
                main(user)

        elif prompt == '3':  # logout
            login()


def login():
    clear()
    print("\t\t\tWelcome.")
    print("\tProvide the correct login information\n")
    username = input("Please, enter your username: ")
    password = input("...and your password: ")
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
