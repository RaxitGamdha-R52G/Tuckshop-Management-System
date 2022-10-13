import csv
import getpass
import pickle


def Title():
    print('|{:^64}|'.format('Tuckshop management system').title())


def showItem(v='', d1='y', d2='y'):
    if d1 == 'y':
        print('+' + '=' * 64 + '+')
    if d2 == 'y':
        print('| {:<10}| {:<15}| {:<10}| {:<10}| {:<10}'.format(v[0], v[1].title(), v[2], v[3], v[4]), end='|\n')


def changeStock(b):
    with open('currentstock.csv', 'w', newline='') as cfh:
        cfh_w = csv.writer(cfh)
        for v in b:
            cfh_w.writerow(v)


def showStock(d: list, e='currentstock.csv'):
    """

    :param d:
    :type e: str
    """
    if d is None:
        d = []
    with open(e, 'r') as bfh:
        bfh_r = csv.reader(bfh)
        for i in bfh_r:
            showItem(i)
            if d != '':
                d.append(i)
        showItem(v='', d1='y', d2='n')
    if d != '':
        return d


def passwordInput():
    try:
        ps = getpass.getpass('Please enter password to procced :->')
    except any(Exception):
        ps = input('Please enter password to procced :->')
    return ps


def SalerLogin():
    b = passwordInput()
    c = open('Passwords.dat', 'rb')
    d = pickle.load(c)
    while d != '':
        if b == d:
            c.close()
            return 'successLogin'
        else:
            try:
                d = pickle.load(c)
            except any(Exception):
                print('Incorrect Password ! Please enter a valid password of Manager.')
                c.seek(0)
                b = passwordInput()


def show(x):
    showItem(v='', d1='y', d2='n')
    for i in x:
        print("|{:<64}|".format(i))
    showItem(v='', d1='y', d2='n')


def logOut():
    hl = ['Thank you for login inside the Tuckshop Management System...',
          'Please login regularly to check the stock management...']
    show(hl)
    tuckshopManagementSystem()


def changePassword():
    old = ''
    old_password_check = SalerLogin()
    new_password: str
    confirm_password: str
    new_password = confirm_password = ''
    if old_password_check == 'successLogin':
        new_password = input('Please enter new password to procced :->')
        confirm_password = input('Please re-enter new password to confirm and procced :->')
        old = '1'
    if old == '1':
        if new_password == confirm_password:
            if confirm_password == '':
                print("Manager password cannot be empty for security, Kindly enter another password.")
            else:
                c = open('Passwords.dat', 'wb')
                pickle.dump(confirm_password, c)
                c.close()
                print("Seller password successfully changed.")
            print()
            input('Press any key to go to main menu :->')
        else:
            print("Your entered password and re-entered password did not match.")
            print("Please enter new password and confirm password again...")
            changePassword()


def currentStock():
    showStock(None)
    input('Press any key to go to main menu :->')


def updateStock(d='y'):
    editing_list = showStock(None)
    while d != 'n':
        up_no = str(input('Enter item number or enter exit to exit :->'))
        if up_no in ('exit', 'EXIT', 'Exit'):
            return 'a'
        for i in editing_list:
            if i[2] == up_no:
                showItem(i)
                showItem(v='', d1='y', d2='n')
                a_1 = input('Enter quantity :->')
                a_2 = input('Enter the price :->')
                if a_1 == '':
                    a_1 = i[3]
                if a_2 == '':
                    a_2 = i[4]
                showItem([i[0], i[1], i[2], a_1, a_2])
                showItem(v='', d1='y', d2='n')
                while (d_1 := str(input('Are you confirmed(y or n) ? :->')).lower()) == '':
                    pass
                if d_1 == 'y':
                    i[3] = a_1
                    i[4] = a_2
                while (d := input('Do you want to enter more(y or n) :->').lower()) == '':
                    pass
    changeStock(editing_list)
    showStock(None)
    input('Press any key to go to main menu :->')
    print()
    del editing_list


def addItemStock(d='y'):
    editing_list = showStock(None)
    print('\nPlease check item you want to add if it is already in the above list.\n')
    while d != 'n':
        while (n_1 := str(input('Enter new item name or enter exit to exit :->'))) == '':
            pass
        if n_1 in ('exit', 'EXIT', 'Exit'):
            return 'a'
        while (n_2 := str(input('Enter new item quantity :->'))) == '':
            pass
        while (n_3 := str(input('Enter new item price :->'))) == '':
            pass
        c = 0
        f = 1000000
        for i in editing_list:
            if i[3] != 'Quantity':
                c = int(i[0])
                f = i[2]
            elif i[3] == 'Quantity':
                pass
        l1 = [str(c + 1), n_1, str(int(f) + 1), n_2, n_3]
        showItem(l1)
        showItem(v='', d1='y', d2='n')
        while (d_1 := str(input('Are you confirmed(y or n) ? :->')).lower()) == '':
            pass
        if d_1 == 'y':
            editing_list.append(l1)
        while (d := input('Do you want to enter more(y or n) :->').lower()) == '':
            pass
    changeStock(editing_list)
    showStock(None)
    input('Press any key to go to main menu :->')
    del editing_list


def removeItemStock(d='y'):
    editing_list = showStock(None)
    while d != 'n':
        n_1 = str(input('Enter item number to delete record or enter exit to exit :->'))
        if n_1 in ('exit', 'EXIT', 'Exit'):
            return 'a'
        for i in editing_list:
            if i[2] == n_1:
                showItem(i)
                showItem(v='', d1='y', d2='n')
                while (n_2 := str(input('Are you confirmed to delete record(y or n) ? :->')).lower()) == '':
                    pass
                c = 0
                if n_2 == 'y':
                    for j in editing_list:
                        c += 1
                        if j[3] == 'Quantity':
                            c -= 1
                        elif j[2] == n_1:
                            editing_list.pop(c)
                            break
                    for w in editing_list:
                        if w[3] == 'Quantity':
                            pass
                        elif w[2] != n_1 and w[2] > n_1:
                            w[0] = str(int(w[0]) - 1)
                            w[2] = str(int(w[2]) - 1)
                while (d := str(input('Do you want to enter more(y or n) ? :->')).lower()) == '':
                    pass
    changeStock(editing_list)
    print()
    showStock(None)
    input('Press any key to go to main menu :->')
    print()
    del editing_list


def Customer(d='y'):
    showItem(v='', d1='y', d2='n')
    Title()
    showItem(v='', d1='y', d2='n')
    print('\nNote: Use only the Item number in for finding suitable item.\n')
    showItem(v='', d1='y', d2='n')
    editing_list2 = []
    editing_list = showStock(None)
    editing_list2.append(['Sr no.', 'Item Name', 'Item no.', 'Quantity', 'Price'])
    while (xn := input('Enter your Customer name :->')) == '':
        print('Please enter Customer name of 10 letters :->')
    while d != 'n':
        n_1 = str(input('Enter item number or enter exit to exit  :->'))
        if n_1 in ('exit', 'EXIT', 'Exit'):
            return 'a'
        for i in editing_list:
            if i[2] == n_1:
                showItem(i)
                showItem(v='', d1='y', d2='n')
                while (n_1 := str(input("Enter the total number quantity which you want to buy :->"))) == '':
                    pass
                while (n_2 := str(input("Are you confirmed to buy (y or n) ? :->")).lower()) == '':
                    pass
                c = len(editing_list2) - 1
                if n_2 == 'y':
                    if int(n_1) > int(i[3]):
                        print('Item out of stock...')
                    elif n_1 == '0':
                        pass
                    else:
                        c += 1
                        lk = [str(c), i[1], i[2], n_1, str(int(n_1) * int(i[4]))]
                        editing_list2.append(lk)
                        i[3] = str(int(i[3]) - int(n_1))
                while (d := str(input("Do you want to enter more (y or n) ? :->")).lower()) == '':
                    pass
    changeStock(editing_list)
    vc = xb = 0
    show(['Your purchased items are given below :'])
    print('|{:<13} : {:<10}{:<38}|'.format('Customer name', xn, ' ' * 38))
    for i in editing_list2:
        showItem(i)
        if i[0] != 'Sr no.':
            vc = vc + int(i[3])
            xb = xb + int(i[4])
    showItem(v='', d1='y', d2='n')
    print('| {:<14}: {:<5} | {:<11} : {:>7} {:<3}{:<14}|'.format('Total quantity', vc, 'Total Price', xb, 'Rs.',
                                                                 ' ' * 14))
    showItem(v='', d1='y', d2='n')
    del editing_list
    del editing_list2
    input('Press any key to go to main menu :->')
    tuckshopManagementSystem()


def Saler():
    choice_dict = {
        '1': currentStock,
        '2': updateStock,
        '3': addItemStock,
        '4': removeItemStock,
        '5': changePassword,
        '6': logOut
    }
    m = [
        'Press-1 to see the current stock...',
        'Press-2 to update the stock...',
        'Press-3 to add new items to stock...',
        'Press-4 to remove items from stock...',
        'Press-5 to change Seller password...',
        'Press-6 to Logout...'
    ]
    show(m)
    while (schoice := input(':->').strip()) == '':
        if schoice not in choice_dict.keys():
            pass
    print()
    choice_dict[schoice]()
    if schoice != '6':
        tuckshopManagementSystem(a='1', b='successLogin')


def login():
    m1 = [
        'Press-1 to login as Seller:',
        'Press-2 to login as Customer:',
        'Press-3 to exit:'
    ]
    showItem(v='', d1='y', d2='n')
    Title()
    show(m1)
    while (a := input(':->').strip()) != '':
        if a in ('1', '2', '3'):
            return a


def tuckshopManagementSystem(a=0, b=0):
    if a == 0:
        print()
        a = login()
    if a == '1':
        print()
        print('Welcome')
        if b != 'successLogin':
            b = SalerLogin()
    elif a == '2':
        Customer()
    elif a == '3':
        show([' ' * 23 + 'Please Visit Again' + ' ' * 23])
        input('')
    if b == 'successLogin':
        print()
        showItem(v='', d1='y', d2='n')
        Title()
        show(['Welcome back here..', 'Now you can modify your stocks...'])
        Saler()


tuckshopManagementSystem()
