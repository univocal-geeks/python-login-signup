# LOGIN Function here...
def login():
    uname = input('Enter username: ')
    uname = uname.lower()
    pswd = input('Enter password: ')
    myfile = open('db/data.txt', 'r')
    u_name = myfile.read()
    x = uname in u_name
    if x == False:
        print("User '"+uname+"' not exist, Try again...")
    if x == True:
        first_char = u_name.index(uname)
        start = first_char + len(uname) + 4
        end = start + len(pswd)
        y = u_name[start:end]
        if y != pswd or pswd == '':
            print("Login Fail, Try again...")
        if y == pswd and pswd != '':
            print("Login Successfully")


# Sign up Function here...
def sign_up():
    f = open('db/data.txt', 'a')
    user = dict()
    uname = input('Enter a username: ')
    uname = uname.lower()
    pswd = input('Enter password: ')
    user[uname] = pswd
    user = str(user)
    f.write(user)
    f.close()
    print('Account Created successfully\n')
    login()


# Main Body here...
print('Welcome!')
choice = input('Login or Sign up? (L/S): ')
choice = choice.lower()
choice = choice[0:1]

if choice == 'l':
    login()

elif choice == 's':
    sign_up()

else:
    print('Oops! Invalid selection.')
input("\n\nPress any key to exit...")
