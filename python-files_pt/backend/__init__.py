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

    def error(msg):
        question_window = Toplevel(top)
        question_window.config(bg = palet[0]['bg'])
        question_window.geometry('380x210+466+265')
        question_window.grab_set()
        question_window.overrideredirect(True)
        question_window.attributes('-alpha', 0.95)

        w1 = Frame(question_window, bg = palet[0]['bg'])
        w1.pack(anchor = NW)
        w2 = Frame(question_window, bg = palet[0]['bg'])
        w2.pack(anchor = SE, side = BOTTOM)

        def x_pop_enter(e):
                fechar_popup.config(bg = palet[0]['exit_bg'])

        def x_pop_leave(e):
            fechar_popup.config(bg = palet[0]['bg'])

        def n_enter(e):
            n.config(bg = palet[0]['df_bg'])

        def n_leave(e):
            n.config(bg = palet[0]['bg'])
        
        n = Button(w2, text = 'Ok', bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], bd = 0, width = 10, font = ('Antipasto', 18), pady = 6, padx = 6, command = question_window.destroy)
        n.pack(anchor = SE, side = RIGHT)
        
        lbl_warning1 = Message(question_window, text = msg, width = 310, bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 17), pady = 25, padx = 16)
        lbl_warning1.pack(anchor = NW, side = LEFT, expand = False)
        
        fechar_popup = Button(question_window, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = question_window.destroy)
        fechar_popup.pack(anchor = NE, side = RIGHT, before = lbl_warning1)
        
        fechar_popup.bind('<Enter>', x_pop_enter)
        fechar_popup.bind('<Leave>', x_pop_leave)
        n.bind('<Enter>', n_enter)
        n.bind('<Leave>', n_leave)

        question_window.mainloop()

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
        try:
            logando()
        except:
            error('Usuário ou senha incorretos. Insira os dados CORRETAMENTE e tente de novo')
            driver.close()
            os.system('python python-files_pt\\interface.py')
        finally:
            time.sleep(12)
            try:
                abrir_post()
            except:
                error('Link da publicação incorreto. Insira os dados CORRETAMENTE e tente de novo')
                driver.close()
                os.system('python python-files_pt\\interface.py')
            finally:
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
        global contador;global driver
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

        def stop_leave(e):
            stop.config(image = stop1)

        def parar():
            global driver
            main_window.destroy()
            driver.close()
            os.system('python python-files_pt\\interface.py')

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
            for letra in frase:
                local.send_keys(letra)
                time.sleep(randint(1, 3) / 80)

        while True:
            time.sleep(randint(3, 6) / 4)
            try:
                time.sleep(4)
                if file[4].strip() == 'True':
                    if cont_coment == num_comentarios:
                        break
                        driver.close()

                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                campo_comentario.clear()
                # campo_comentario.send_keys(username)
                time.sleep(randint(3, 6))
                
                if file[3].strip() == 'True':
                    digitando(choice(comentarios), campo_comentario)
                elif file[3].strip() == 'False':
                    digitando(comentario_unico, campo_comentario)

                time.sleep(randint(4, 8) / 4)

                bt_publicar = driver.find_element_by_xpath('//button[contains(text(), \'Publicar\')]')
                bt_publicar.click()
                cont_coment += 1
                contador.config(text = cont_coment)
                atualizar_janela()
                time.sleep(1)
            except:
                time.sleep(randint(12, 16))
                try:
                    driver.find_element_by_xpath('//button[contains(text(), \'Publicar\')]').click()
                    time.sleep(randint(4, 8) / 4)
                except:
                    pass

    obtendo_variaveis()
    threading.Thread(target = abrindo_instagram).start()
    new_window(window, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta)

if __name__ == '__main__':
    os.system('python python-files_pt\\interface.py')
