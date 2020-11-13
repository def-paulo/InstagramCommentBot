from tkinter import *
import time
from random import choice, randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import threading
from pygame import mixer

def bot(main_window, window, x, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta):
    global comentarios
    global cont_coment
    global link_pub

    comentarios = []
    cont_coment = 0
    link_pub = None

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

        f = open('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\variables.txt', 'r')
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

    def error(msg):
        question_window = Toplevel(main_window)
        question_window.overrideredirect(True)
        question_window.config(bg = paleta[0]['bg'])
        question_window.geometry('380x210+466+265')
        question_window.grab_set()
        question_window.attributes('-alpha', 0.95)

        w1 = Frame(question_window, bg = paleta[0]['bg'])
        w1.pack(anchor = NW)
        w2 = Frame(question_window, bg = paleta[0]['bg'])
        w2.pack(anchor = SE, side = BOTTOM)

        def x_pop_enter(e):
                fechar_popup.config(bg = paleta[0]['exit_bg'])

        def x_pop_leave(e):
            fechar_popup.config(bg = paleta[0]['bg'])

        def n_enter(e):
            ok.config(bg = paleta[0]['df_bg'])

        def n_leave(e):
            ok.config(bg = paleta[0]['bg'])

        def sair(event = ''):
            main_window.destroy()
            os.system(f'cd {os.getcwd()} & python python_files_pt\\interface.py')
            # subprocess.Popen(f'cd {os.getcwd()}', shell = True)
            # subprocess.Popen('python python_files_pt\\interface.py', shell = True)

        def last_click(event):
            global click_x
            global click_y

            click_x = event.x
            click_y = event.y

        def move_window(event):
            if 32 >= click_y >= 0:
                x, y = event.x - click_x + question_window.winfo_x(), event.y - click_y + question_window.winfo_y()
                question_window.geometry(f'+{x}+{y}')
        
        ok = Button(w2, text = 'Ok', bg = paleta[0]['bg'], fg = paleta[0]['fg'], activebackground = paleta[0]['df_bg'], activeforeground = paleta[0]['fg'], bd = 0, width = 10, font = ('Antipasto', 18), pady = 6, padx = 6, command = sair)
        ok.pack(anchor = SE, side = RIGHT)
        
        lbl_warning1 = Message(question_window, text = msg, width = 310, bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 17), pady = 25, padx = 16)
        lbl_warning1.pack(anchor = NW, side = LEFT, expand = False)
        
        fechar_popup = Button(question_window, text = 'X', bd = 0, bg = paleta[0]['bg'], fg = paleta[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = paleta[0]['exit_bg'], activeforeground = paleta[0]['fg'], highlightcolor = paleta[0]['exit_bg'], command = sair)
        fechar_popup.pack(anchor = NE, side = RIGHT, before = lbl_warning1)

        mixer.init()
        mixer.music.load('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\media\\songs\\error.mp3')
        mixer.music.play()
        
        fechar_popup.bind('<Enter>', x_pop_enter)
        fechar_popup.bind('<Leave>', x_pop_leave)
        ok.bind('<Enter>', n_enter)
        ok.bind('<Leave>', n_leave)
        ok.bind_all('<Return>', sair)
        question_window.bind('<Button-1>', last_click)
        question_window.bind('<B1-Motion>', move_window)

        try:
            question_window.mainloop()
        except:
            pass

    def abrindo_instagram():
        global driver
        global campo_usuario
        global campo_senha
        global usuario
        global senha
        global driver
        global link
        global cont_coment
        global campo_comentario
        global driver
        global file
        global bt_publicar
        global comentarios
        global top
        global contador
        global aviso_senha
        global post_id
        global aviso_link

        post_id = None
        aviso_senha = None
        aviso_link = None
        
        opt = webdriver.FirefoxOptions()
        opt.add_argument('-headless')
        # driver = webdriver.Firefox(options = opt, executable_path = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\geckodrive\\geckodriver.exe')

        driver = webdriver.Firefox(executable_path = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\geckodrive\\geckodriver.exe') # Especifique o caminho completo, Ex.: 'C:\\Users\\root\\documents\\InstagramBot\\python_files_pt\\'
        driver.get('https://instagram.com')
        time.sleep(10)
        logando()
        try:
            aviso_senha = driver.find_element_by_class_name('eiCW-')
        except:
            if link[0:26] != 'https://www.instagram.com/':
                error('!LINK DA PUBLICAÇÃO INCORRETO! Insira os dados CORRETAMENTE e tente de novo')
                window.destroy()
                driver.close()
            else:
                time.sleep(9)
                try:
                    abrir_post()
                except:
                    error('!LINK DA PUBLICAÇÃO INCORRETO! Insira os dados CORRETAMENTE e tente de novo')
                    window.destroy()
                    driver.close()
                else:
                    comentando()
                    if not link_pub:
                        print('ERRO')
                        error('!LINK DA PUBLICAÇÃO INCORRETO! Insira os dados CORRETAMENTE e tente de novo')
                        window.destroy()
                        driver.close()
                    # try:
                    #     aviso_link = driver.find_element_by_class_name('SCxLW  o64aR ')
                    #     print('aviso_link is defined!', aviso_link)
                    # except:
                    #     time.sleep(randint(7, 14))
                    #     comentando()
                    # finally:
                    #     if aviso_link != None:
                    #         error('!LINK DA PUBLICAÇÃO INCORRETO! Insira os dados CORRETAMENTE e tente de novo')
                    #         window.destroy()
                    #         driver.close()
        finally:
            if aviso_senha != None:
                error('!USUÁRIO OU SENHA INCORRETOS! Insira os dados CORRETAMENTE e tente de novo')
                window.destroy()
                driver.close()

    def logando():
        global campo_usuario
        global campo_senha
        global usuario
        global senha

        campo_usuario = driver.find_element_by_xpath('//input[@name = \'username\']')
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(usuario)

        campo_senha = driver.find_element_by_xpath('//input[@name = \'password\']')
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(senha)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(randint(3, 4))
        
        try:
            aviso_senha = driver.find_element_by_class_name('eiCW-')
        except:
            pass

    def abrir_post():
        global driver
        global link

        driver.get(link)
        time.sleep(randint(4, 8))

    def new_window(main_window, window, x, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta):
        global contador
        global driver
        
        imagem_aviso.destroy()
        mensagem_aviso.destroy()
        mensagem_iniciando.destroy()

        main_window.iconbitmap('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\media\\mascote.ico') # Especifique o caminho completo, Ex.: 'C:\\Users\\root\\documents\\InstagramBot\\python_files_pt\\'

        space_contador = Frame(window, bg = paleta[0]['bg'], width = 80)
        space_contador.pack(anchor = W, side = LEFT)

        contador = Label(window, text = cont_coment, bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 128), pady = 40, padx = 2700)
        # contador.place(x = 280, y = 120)
        contador.pack(anchor = CENTER)
        
        lbl_contador = Label(window, text = 'Comentários publicados', bg = paleta[0]['bg'], fg = paleta[0]['fg'], font = ('Antipasto', 22))
        lbl_contador.place(x = 205, y = 320)

        def fechar(event = ''):
            try:
                driver.close()
            except:
                pass
            main_window.destroy()

        def stop_enter(e):
            stop.config(image = stop2)

        def stop_leave(e):
            stop.config(image = stop1)

        def parar(event = ''):
            global driver
            main_window.destroy()
            try:
                driver.close()
            except:
                pass
            os.system(f'cd {os.getcwd()} & python python_files_pt\\interface.py')
            # subprocess.Popen(f'cd {os.getcwd()}', shell = True)
            # subprocess.Popen('python python_files_pt\\interface.py False', shell = True)


        stop1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\media\\stop_1.png') # Especifique o caminho completo, Ex.: 'C:\\Users\\root\\documents\\InstagramBot\\python_files_pt\\'
        stop1 = stop1.subsample(4, 4)

        stop2 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\media\\stop_2.png') # Especifique o caminho completo, Ex.: 'C:\\Users\\root\\documents\\InstagramBot\\python_files_pt\\'
        stop2 = stop2.subsample(4, 4)
        
        stop = Button(window, image = stop1, bg = paleta[0]['bg'], bd = 0, font = ('Antipasto', 16), command = parar, activebackground = paleta[0]['bg'], cursor = 'hand2')
        # stop.pack(anchor = S, side = BOTTOM)
        stop.place(x = 216, y = 482)

        x.config(command = fechar)

        stop.bind('<Enter>', stop_enter)
        stop.bind('<Leave>', stop_leave)
        window.bind('<Escape>', parar)
        window.update()

    def comentando():
        global cont_coment
        global campo_comentario
        global driver
        global file
        global bt_publicar
        global comentarios
        global top
        global contador
        global link_pub

        def digitando(frase, local):
            for letra in frase:
                local.send_keys(letra)
                time.sleep(randint(1, 3) / 80)

        while True:
            time.sleep(randint(3, 6) / 4)
            try:
                campo_comentario = driver.find_element_by_class_name('Ypffh')
            except:
                break
                link_pub = False
            else:                
                try:
                    time.sleep(4)
                    if file[4].strip() == 'True':
                        if cont_coment == num_comentarios:
                            lbl_sucess_final = Label(window, text = 'Comentários publicados com sucesso!', bg = paleta[0]['bg'], fg = '#0dff90', font = ('Antipasto', 22))
                            lbl_sucess_final.place(x = 125, y = 380)
                            mixer.init()
                            mixer.music.load('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python_files_pt\\media\\songs\\sucess.mp3')
                            mixer.music.play()
                            break

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
                    link_pub = True
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
    atualizar_janela()
    time.sleep(randint(3, 6))
    new_window(main_window, window, x, imagem_aviso, mensagem_aviso, mensagem_iniciando, paleta)

if __name__ == '__main__':
    os.system(f'cd {os.getcwd()} & python python_files_pt\\interface.py')
    # subprocess.Popen(f'cd {os.getcwd()}', shell = True)
    # subprocess.Popen('python python_files_pt\\interface.py', shell = True)
