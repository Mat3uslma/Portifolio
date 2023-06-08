import mysql.connector
def cadastro():
    print("Tela de Login ")
    user = str(input("Usuario "))
    email = str(input("Email "))
    senha = str(input("Senha "))

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="098078",
        database="login"

    )
    cursor = conexao.cursor()

    comando = "INSERT INTO login_user (user,email,senha) VALUES (%s,%s,%s)"
    dados = ((user),(email),(senha))
    cursor.execute(comando,dados)
    conexao.commit()


    cursor.close()
    conexao.close()
cadastro()





