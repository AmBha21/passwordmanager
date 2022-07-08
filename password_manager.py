#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Password Manager
@author: AmBha
"""
from cryptography.fernet import Fernet


def load_key () :
    file = open("key.key", "rb")
    key=file.read()
    file.close()
    return key



# master_pwd=input("What is the master password? ")
#Might be a future idea

key=load_key() #+ master_pwd.encode()
fer=Fernet(key)



'''
def write_key():
    key=Fernet.generate_key()
    with open("key.key",'wb') as key_file:
        key_file.write(key)
        
# write_key()'''


#Functions
def view():
    with open('passwords.txt','r') as f:
        for i in f.readlines():
            data=i.rstrip()
            user,pwd=data.split("|")
            #returns [username,pwd] for each line
            #user=username pwd=pwd
            print("Username: ",user, " |Password: ",fer.decrypt(pwd .encode()).decode())
                    

def add():
    name = input("Account Username: ")
    password=input("Password: ")
    with open('passwords.txt','a') as f:
        f.write(name+'|'+fer.encrypt(password.encode()).decode()+'\n')
        f.close()
    

while True:
    mode=input("Would you like to add a new password or view an existing one (view, add)? Press q to quit. ").lower()
    if mode=="q":
        break 
    elif mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print ("Invalid mode. ")
        continue
    
