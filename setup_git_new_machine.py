import os

username = raw_input("Username: ")
email = raw_input("E-mail: ")

os.system('git config --global user.name "%s"' % username)
os.system('git config --global user.email "%s"' % email)

