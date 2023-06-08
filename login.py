import mysql.connector
def login():
    print("Tela de Login ")
    email = str(input("Email "))
    senha = str(input("Senha "))

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="098078",
        database="login"

    )
    cursor = conexao.cursor()

    comando = "select * from login_user"
    cursor.execute(comando)
    Login = cursor.fetchall()

    for logins in Login:
        if email == logins[2] and senha == logins[3]:
            print("CORRETO PODE FAZER O LOGIN")

        elif email != logins[2] and senha != logins[3]:
            print("incorreto")







    cursor.close()
    conexao.close()

login()
