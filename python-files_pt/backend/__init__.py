from tkinter import *
from time import sleep
from random import choice, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def bot(window, imagem_aviso, mensagem_aviso, mensagem_iniciando):
    global comentarios
    comentarios = []
    
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
        global campo_usuario;global campo_senha
        campo_usuario = driver.find_element_by_xpath('//input[@name = \'username\']')
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

        campo_senha = driver.find_element_by_xpath('//input[@name = \'password\']')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)

    obtendo_variaveis()
