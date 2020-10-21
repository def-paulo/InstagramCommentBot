from tkinter import *
import time
from random import choice, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import threading

def bot(main_window, window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta):
    global comentarios;global cont_coment
    comentarios = []
    cont_coment = 0

    def atualizar_janela():
        main_window.update()
        window.update()

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

        f = open('C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\InstagramBot\\python-files_pt\\variables.txt', 'r')
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
            num_comentarios = int(file[7].strip())
            print(f'Número de comentários: {num_comentarios}')

    def abrindo_instagram():
        global driver
        driver = webdriver.Firefox(executable_path = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\InstagramBot\\python-files_pt\\geckodrive\\geckodriver.exe')
        driver.get('https://instagram.com')
        time.sleep(10)
        logando()
        time.sleep(12)
        abrir_post()
        time.sleep(randint(7, 14))
        comentando()

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
        time.sleep(randint(7, 14))

    def new_window(window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta):
        global contador
        imagem_aviso.destroy()
        mensagem_aviso.destroy()
        mensagem_iniciando.destroy()

        space_contador = Frame(window, bg = paleta[0]['bg'], width = 20)
        space_contador.pack(anchor = W, side = LEFT)

        contador = Label(window, text = cont_coment, bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 128), pady = 40, padx = 1200)
        # contador.place(x = 280, y = 120)
        contador.pack(anchor = CENTER)
        
        lbl_contador = Label(window, text = 'Comentários publicados', bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 22))
        lbl_contador.place(x = 195, y = 320)

        def stop_enter(e):
            stop.config(image = stop2)
            atualizar_janela()

        def stop_leave(e):
            stop.config(image = stop1)
            atualizar_janela()

        def parar():
            main_window.destroy()
            os.system('python python-files_pt\\interface.py')
            driver.close()

        stop1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\InstagramBot\\python-files_pt\\media\\stop_1.png')
        stop1 = stop1.subsample(4, 4)

        stop2 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Downloads\\scripts\\python_curso_em_video\\Exercicios e Ideias\\Exercicios extras\\InstagramBot\\python-files_pt\\media\\stop_2.png')
        stop2 = stop2.subsample(4, 4)
        
        stop = Button(window, image = stop1, bg = paleta[0]['bg'], bd = 0, font = ('Antipasto', 16), command = parar, activebackground = paleta[0]['bg'])
        stop.pack(anchor = S, side = BOTTOM)

        stop.bind('<Enter>', stop_enter)
        stop.bind('<Leave>', stop_leave)

        window.update()

    def comentando():
        global cont_coment;global campo_comentario;global driver;global file;global bt_publicar;global comentarios;global top;global contador

        def digitando(frase, local):
            atualizar_janela()
            for letra in frase:
                atualizar_janela()
                local.send_keys(letra)
                atualizar_janela()
                time.sleep(randint(1, 3) / 80)
                atualizar_janela()

        while True:
            atualizar_janela()
            time.sleep(randint(3, 6) / 4)
            try:
                time.sleep(4)
                atualizar_janela()
                if file[4].strip() == 'True':
                    if cont_coment == num_comentarios:
                        break
                        driver.close()

                atualizar_janela()
                driver.find_element_by_class_name('Ypffh').click()
                atualizar_janela()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                atualizar_janela()
                campo_comentario.clear()
                atualizar_janela()
                # campo_comentario.send_keys(username)
                time.sleep(randint(3, 6))
                atualizar_janela()
                
                if file[3].strip() == 'True':
                    digitando(choice(comentarios), campo_comentario)
                elif file[3].strip() == 'False':
                    digitando(comentario_unico, campo_comentario)

                atualizar_janela()
                time.sleep(randint(4, 8) / 4)
                atualizar_janela()

                bt_publicar = driver.find_element_by_xpath('//button[contains(text(), \'Publicar\')]')
                atualizar_janela()
                bt_publicar.click()
                atualizar_janela()
                cont_coment += 1
                atualizar_janela()
                contador.config(text = cont_coment)
                atualizar_janela()
                print(cont_coment)
                atualizar_janela()
                time.sleep(1)
                atualizar_janela()
            except:
                atualizar_janela()
                time.sleep(randint(12, 16))
                atualizar_janela()
                try:
                    atualizar_janela()
                    driver.find_element_by_xpath('//button[contains(text(), \'Publicar\')]').click()
                    atualizar_janela()
                    time.sleep(randint(4, 8) / 4)
                    atualizar_janela()
                except:
                    pass

    obtendo_variaveis()
    threading.Thread(target = abrindo_instagram).start()
    new_window(window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta)

if __name__ == '__main__':
    os.system('python python-files_pt\\interface.py')
