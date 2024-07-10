import string
import random

def remove_char(string, n):
    return string[n:string(len)-n]

def random_string(length):
    letters = string.ascii_letters + string.digits
    # print(random.choices(letters, k=length))        #It produces value in list
    return ("".join(random.choices(letters, k=length)))

print("        WELCOME TO THE ENCRYPTOR / DECRYPTOR         ")

while True:
    try:
        print("\nSelect your choice:\n1. Encryptor\n2. Decryptor\n3. Exit")
        a = int(input())
        if  a == 1:
            code = str(input("Enter the message for encryption:\n"))
            code_list = code.split(" ")  #This will split the string words and put them in a list
            space = []

            for i in code_list[0:len(code_list)]:
                b =  random_string(3)
                c =  random_string(3)
                if len(i) <= 2:
                    space.append(i[::-1])
                elif len(i) >=3:
                    space.append(b + i[1:] + i[0] + c)

            encrypted = (" ".join(space))
            print ("\nYour message is encrypted successfully!")
            print ("\nYour encrypted message is","\"", encrypted, "\"")

        elif a==2:
            code = str(input("Enter the message for decryption:\n"))
            code_list = code.split(" ")
            space = []

            for i in code_list[0:len(code_list)]:
                if len(i) <= 2:
                    space.append(i[::-1])
                elif len(i) >=3:
                    space.append(i[-4] + i[3:len(i)-4])

            decrypted = (" ".join(space))
            print ("\nYour message is decrypted successfully!")
            print ("\nYour decrypted message is","\"", decrypted, "\"")
        elif a == 3:
            exit()
        else:
            print ("You have given a wrong choice, Try Again!") #This will be printed when any other integer will be input
    except ValueError:
        print ("Are you using any other character?, Please only use an integer!") #This will be printed when any other data type will be input