import customtkinter as tk
import sqlite3

conexao = sqlite3.connect("banco.db")
c = conexao.cursor()

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

janela = tk.CTk()
janela.geometry("500x500")


texto = tk.CTkLabel(janela, text="Fazer Login")
texto.pack(padx=10, pady=10)
#########         #########                                                   
        #LOGIN#
#########         #########
email_login = tk.CTkEntry(janela, placeholder_text="Seu e-mail")            
email_login.pack(padx=10, pady=10)

senha_login = tk.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha_login.pack(padx=10, pady=10)
def login():
    nomeb = email_login.get()
    senhab = senha_login.get()
    c.execute(
        """SELECT nomeb,senhab FROM cadastro
         WHERE (nomeb = ? and senhab = ?)""",(nomeb,senhab))
    
    print("LOGIN FEITO")
botao = tk.CTkButton(janela, text="LOGIN", command=login)
botao.pack(padx=10, pady=10)
checkbox = tk.CTkCheckBox(janela, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

#########         #########
        #CADASTRO#
#########         ######### 
email_cadastro = tk.CTkEntry(janela, placeholder_text="Cadastrar e-mail")
email_cadastro.pack(padx=10, pady=10)

senha_cadastro = tk.CTkEntry(janela, placeholder_text="Cadastrar senha", show="*")
senha_cadastro.pack(padx=10, pady=10)
def cadastro():
    emailb = email_cadastro.get()
    senhab = senha_cadastro.get()
    c.execute(
        "INSERT INTO cadastro (nomeb,emailb,senhab)VALUES(?,?,?)",(emailb,senhab)
    )
    conexao.commit()
botao = tk.CTkButton(janela, text="CADASTRAR", command=cadastro)
botao.pack(padx=10, pady=10)




janela.mainloop()
c.close()
conexao.close()