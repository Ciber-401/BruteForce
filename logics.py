def Simple_logic(login_generator, password_generator, query):
    login = login_generator.generate()
    if login is None:
        return

    while True:
        password = password_generator.generate()
        if password is None:
            return

        if query(login, password):
            print('SUCCES', login, password)
            return

def Get_accounts_logic(login_genrator, password_generator, query, login_limit = 1000, password_limit=1000):
    succes_logins = set()

    for i in range(password_limit):
        password = password_generator.generate()
        if password is None:
            return

        login_genrator.reset()
        for j in range(login_limit):
            login = login_genrator.generate()
            if login is None:
                break

            if login not in succes_logins and query(login, password):
                print('SUCCES', 'LOGIN:', login, 'PASSWORD:', password)
                succes_logins.add(login)


def Get_password_logic(login_genrator, password_generator, query, password_limit=1000):
    while True:
        login = login_genrator.generate()
        if login is None:
            break

        password_generator.reset()
        for j in range(password_limit):
            password = password_generator.generate()
            if password is None:
                break

            if query(login. password):
                print('SUCCES', login, password)
                break








































