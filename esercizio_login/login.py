class Login_error(Exception):
    pass
class User_not_found(Login_error):
    pass
from users import Users

user1 = Users ('user1','password1')
user2 = Users ('user2','password2')
user3 = Users ('user3','password3')

utenti = [user1,user2,user3]

nome_utente = input('inserisci nome utente: ').strip()
password_utente = input('inserisci password: ').strip()
try:
    for utente in utenti:
        if nome_utente == utente.user_name and password_utente == utente.user_password:
            print('accesso consentito')
        else:
            raise User_not_found
except User_not_found as ex:
    print(ex)




