# assuptions:
''' the username and password are saved in a file named as pwd_file. it will have only two entries.
1st line as username and 2nd line as password.
special characters can be added and/or modified in special_char_l list
'''

special_char_l = ['!','<','>','<','.','+','-','_','%','#','&','@','^','*','$','/','(',')']
print ('Enter 1 : Registraion: ' )
print ('Enter 2 : Login: ')
print ('Enter 3 : Reset Password : ')
choice = input()

def valid_user_name(u_name):
        if u_name[0].isdigit():
                print('Invalid Username: Can not start with a number,try again')
                return False
        if u_name.count('@.') >0:
                print('Invalid Username: @can not be followed by a .Try again')
                return False
        if any(u_name.startswith(s) for s in special_char_l):
                print("Invalid username: Can't start with a special character,Try again")
                return False
        return True
def valid_pwd(pwd):

        if pwd.isnumeric():
                print("Password should have atleast one character: ")
                return False
        elif pwd.islower():
                print("password should have atleast one uppercase letter: ")
                return False
        elif pwd.isupper():
                print("Password should have atleast one lowercase letter: ")
                return False
        elif pwd.isalpha():
                print(" Password should have atleast one number")
                return False
        elif any(pwd.find(s) for s in special_char_l) != -1:
                print("should have atleast one special charater")
                return False
        return True
# REGISTRATION
if choice == '1':
        name = input("Enter UserName: ")
        if valid_user_name(name):
                p_file = open("pwd_file", "r")
                user_name = p_file.readline()
                p_file.close()
                if user_name.upper().strip() == name.upper().strip():
                        print("User already exists, can LOGIN")
                        exit()
                else:
                        pwd = input("Enter password: ")
                        if valid_pwd(pwd):
                                p_file = open("pwd_file","w")
                                p_file.write(name)
                                p_file.write('\n')
                                p_file.write(pwd)
                                print("Registration Successful")
                                p_file.close()

                #print("Registration Successful")
elif choice == '2':
        name = input("Enter UserName:")
        pwd = input("Enter Password: ")
        p_file = open("pwd_file", "r")
        user_name = p_file.readline()

        if user_name.upper().strip() == name.upper().strip():
                user_pwd = p_file.readline()
                if user_pwd.upper().strip() == pwd.upper().strip():
                        print("Login Successul !!!")
                        exit()
                else:
                        print(" Password entered is incorrect: ")
                p_file.close()
        else:
                print("Username doesn't exit. Please create login credentials !!!")
elif choice == '3':
        name = input("Enter UserName:  ")
        p_file = open("pwd_file", "r")
        user_name = p_file.readline()
        if user_name.upper().strip() != name.upper().strip():
                print("User name entered doesn't exits, try again")
                exit()
        else:
                user_pwd = p_file.readline()
                print('Your password is :',user_pwd)
        p_file.close()
else:
        print("Please enter 1 or 2 or 3 ")

