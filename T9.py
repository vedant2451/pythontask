# create programme check credential user and password inserted by user

def check_user_pass(username,password):
    if username == "admin" :
        if password == "admin?123" :
            print("login success")
        else:
            print("password is incorrect")
    else :
        print("username is incorrect")


u = input("Enter your username: ")
p = input("Enter your password: ")
check_user_pass(u,p)