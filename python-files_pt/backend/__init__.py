from tkinter import *
import time
from random import choice, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def bot(window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta):
    global comentarios;global cont_coment
    comentarios = []
    cont_coment = 0

    def obtendo_variaveis():
        global file
        global idx_comentarios
        global comentarios
        global usuario
        global senha
        global link
        global coments
        global comentario_unico
        global num_comentarios

        f = open('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\variables.txt', 'r')
        file = f.readlines()
        
        usuario = file[0].strip()
        senha = file[1].strip()
        link = file[2].strip()
        print(f'Usuário: {usuario}\nSenha: {senha}\nLink do post: {link}')

        if file[3] == 'True\n':
            coments = file[5].strip()
            idx_coments = ''
            for c in range(0, len(coments)):
                if coments[c] == '-':
                    comentarios.append(idx_coments)
                    idx_coments = ''
                else:
                    idx_coments += coments[c]
            print(f'Lista de comentários: {comentarios}')
        elif file[3] == 'False\n':
            comentario_unico = file[6].strip()
            print(f'Comentário: {comentario_unico}')

        if file[4] == 'True\n':
            num_comentarios = file[7].strip()
            print(f'Número de comentários: {num_comentarios}')

    def abrindo_instagram():
        global driver
        driver = webdriver.Firefox(executable_path = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\geckodrive\\geckodriver.exe')
        driver.get('https://instagram.com')

    def logando():
        global campo_usuario;global campo_senha;global usuario;global senha
        campo_usuario = driver.find_element_by_xpath('//input[@name = \'username\']')
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

        campo_senha = driver.find_element_by_xpath('//input[@name = \'password\']')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)

    def abrir_post():
        global driver;global link
        driver.get(link)
        time.sleep(randint(8, 16))

    def new_window(window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta):
        imagem_aviso.destroy()
        mensagem_aviso.destroy()
        mensagem_iniciando.destroy()

        contador = Frame(window, bg = paleta[0]['bg'], width = 20)
        contador.pack(anchor = W, side = LEFT)

        contador = Label(window, text = cont_coment, bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 128), pady = 40, padx = 1200)
        # contador.place(x = 280, y = 120)
        contador.pack(anchor = CENTER)
        
        contador = Label(window, text = 'Comentários publicados', bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 22))
        contador.place(x = 195, y = 320)

        window.update()


    obtendo_variaveis()
    # abrindo_instagram()
    # time.sleep(10)
    # logando()
    # time.sleep(12)
    # abrir_post()
    new_window(window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta)
