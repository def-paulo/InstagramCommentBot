from tkinter import *
from time import sleep
from backend import bot
from selenium import webdriver
import threading
from PIL import ImageTk, Image

palet = [{'bg':'#141414', 'fg':'#cfcfcf', 'exit_bg':'#ff2f2f', 'df_bg':'#676767', 'wd_bg':'#1d1d1d', 'bd':'#4d4d4d'}]
cont_maximizado = 0
comentarios = []
v_comment = None
width, height = 700, 550
quant_comentarios = None
click_x, click_y = 0, 0

def managment_window():
    global cont_maximizado;global maximizar;global top;global fechar;global maximize;global resize_maximize;global minimizar;global palet;global click_x;global click_y

    def x_enter(e):
        fechar.config(bg = palet[0]['exit_bg'])

    def x_leave(e):
        fechar.config(bg = palet[0]['bg'])

    # def max_enter(e):
    #     maximizar.config(bg = palet[0]['df_bg'])

    # def max_leave(e):
    #     maximizar.config(bg = palet[0]['bg'])

    def min_enter(e):
        minimizar.config(bg = palet[0]['df_bg'])

    def min_leave(e):
        minimizar.config(bg = palet[0]['bg'])
        
    # def maxi():
    #     global cont_maximizado
    #     cont_maximizado += 1
    #     if cont_maximizado % 2 != 0:
    #         top.geometry(f'{top.winfo_screenwidth()}x{top.winfo_screenheight()}+0+0')
    #         maximizar.config(image = resize_maximize)
    #     else:
    #         top.geometry('700x530+360+160')
    #         maximizar.config(image = maximize)

    def minimizing():
        top.withdraw()
        # top.deiconify()

    def last_click(event):
        global click_x;global click_y
        click_x = event.x
        click_y = event.y
        print(click_y)

    def move_window(event):
        x, y = event.x - click_x + top.winfo_x(), event.y - click_y + top.winfo_y()
        top.geometry(f'+{x}+{y}')

    move_area = Label(top, bg = palet[0]['bg'], width = 150, height = 4)
    move_area.place(x = 0, y = 0)

    fechar = Button(top, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 5, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = root.destroy)
    fechar.pack(anchor = NE, side = RIGHT)

    maximize = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\max.png')
    maximize = maximize.subsample(45, 45)

    # resize_maximize = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\res_max.png')
    # resize_maximize = resize_maximize.subsample(45, 45)

    maximizar = Button(top, image = maximize, compound = CENTER, pady = 100, height = 36, width = 50, bd = 0, activebackground = palet[0]['df_bg'], bg = palet[0]['bg'], highlightcolor = palet[0]['exit_bg'], state = DISABLED, cursor = 'X_cursor')
    maximizar.pack(anchor = NE, side = RIGHT)

    minimizar = Button(top, text = '-', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 5, font = ('Antipasto', 15, 'bold'), activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = minimizing)
    minimizar.pack(anchor = NE, side = RIGHT)

    fechar.bind('<Enter>', x_enter)
    fechar.bind('<Leave>', x_leave)
    # maximizar.bind('<Enter>', max_enter)
    # maximizar.bind('<Leave>', max_leave)
    minimizar.bind('<Enter>', min_enter)
    minimizar.bind('<Leave>', min_leave)
    move_area.bind('<Button-1>', last_click)
    move_area.bind('<B1-Motion>', move_window)

root = Tk()
root.iconbitmap('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\instagram.ico')
root.attributes('-alpha', 0.0)
root.title('Instagram Bot')
root.config(bg = palet[0]['bg'])
top = Toplevel(root)
top.grab_set()
top.geometry(f'{width}x{height}+360+120')
top.config(bg = palet[0]['bg'])
top.overrideredirect(True)
top.attributes('-toolwindow')

# def mouse(event):
#     print(f'X: {event.x}, Y: {event.y}')

# top.bind('<Motion>', mouse)

def on(event):
    top.withdraw()
root.bind("<Unmap>", on)
def off(event):
    top.deiconify()
root.bind("<Map>", off)

def about():
    def ab():
        global bg_img
        sleep(.1)
        about_window = Toplevel(top)
        about_window.config(bg = palet[0]['bg'])
        about_window.geometry('456x302+460+240')
        about_window.grab_set()
        about_window.overrideredirect(True)
        about_window.config(highlightbackground = palet[0]['fg'])
        # about_window.attributes('-alpha', 0.95)

        bg_img = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\about_bg.png')

        bg = Label(about_window, image = bg_img, bg = palet[0]['bg'])
        bg.place(x = 0, y = 0)

        w1 = Frame(about_window, bg = palet[0]['bg'])
        w1.pack(anchor = NW)
        w2 = Frame(about_window, bg = palet[0]['bg'])
        w2.pack(anchor = SE, side = BOTTOM)

        def x_pop_enter(e):
                fechar_popup.config(bg = palet[0]['exit_bg'])

        def x_pop_leave(e):
            fechar_popup.config(bg = palet[0]['bg'])

        def link_enter(e):
                profile_link.config(font = ('Antipasto', 22, 'underline'))

        def link_leave(e):
            profile_link.config(font = ('Antipasto', 22))

        def last_click(event):
            global click_x;global click_y
            click_x = event.x
            click_y = event.y

        def move_window(event):
            if 32 >= click_y >= 0 and 0 <= click_x <= 456:
                x, y = event.x - click_x + about_window.winfo_x(), event.y - click_y + about_window.winfo_y()
                about_window.geometry(f'+{x}+{y}')

        def profile():
            def tg():
                driver = webdriver.Firefox(executable_path = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\geckodrive\\geckodriver.exe')
                driver.get('https://github.com/def-paulo')
            
            threading.Thread(target = tg).start()

            profile_link.config(state = DISABLED, cursor = 'X_cursor')
            about_window.update()
            
            for c in range(100):
                sleep(.1)
                about_window.update()

            profile_link.config(state = ACTIVE, cursor = 'hand2')
            about_window.update()

        fechar_popup = Button(about_window, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = about_window.destroy)
        fechar_popup.pack(anchor = NE, side = RIGHT)

        ig_icon = Label(about_window, image = ig, bg = palet[0]['bg'], bd = 0, height = 38, width = 40)
        ig_icon.pack(anchor = NW, side = TOP)

        ig_lbl = Label(about_window, text = 'Instagram Comment Bot', bd = 0, font = ('Antipasto', 16), bg = palet[0]['bg'], fg = palet[0]['fg'], pady = 3)
        # ig_lbl.pack(anchor = NW)
        ig_lbl.place(x = 40, y = 5)
        
        lbl_info = Message(about_window, text = 'Python                v3.8.1\nSelenium              v3.141.0\nPyInstaller            v4.0\nTkinter                v8.6\nCriado por: Paulo Thiago\nPerfil GitHub:', width = 450, justify = LEFT, bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16), pady = 25, padx = 16)
        lbl_info.pack(anchor = NW, side = TOP, expand = False)

        profile_link = Button(about_window, bd = 0, text = 'github.com/def-paulo', font = ('Antipasto', 22), bg = palet[0]['bg'], fg = '#4f5bd5', padx = 8, cursor = 'hand2', activebackground = palet[0]['bg'], activeforeground = '#4f5bd5', command = profile)
        profile_link.place(x = 0, y = 210)
        
        fechar_popup.bind('<Enter>', x_pop_enter)
        fechar_popup.bind('<Leave>', x_pop_leave)
        about_window.bind('<Button-1>', last_click)
        about_window.bind('<B1-Motion>', move_window)
        profile_link.bind('<Enter>', link_enter)
        profile_link.bind('<Leave>', link_leave)

        about_window.mainloop()

    try:
        threading.Thread(target = ab).start()
    except:
        pass

managment_window()

ig = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\instagram.png')
ig = ig.subsample(13, 13)

warning = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\warning.png')
warning = warning.subsample(4, 4)

in_bot1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_bot_1.png')
in_bot1 = in_bot1.subsample(6, 6)

in_bot2 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_bot_2.png')
in_bot2 = in_bot2.subsample(6, 6)

ig_icon = Button(top, image = ig, bg = palet[0]['bg'], bd = 0, height = 38, width = 40, activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], cursor = 'question_arrow', command = about)
ig_icon.pack(anchor = NW, side = LEFT)

ig_lbl = Button(top, text = 'Instagram Comment Bot', bd = 0, font = ('Antipasto', 16), bg = palet[0]['bg'], fg = palet[0]['fg'], pady = 2, activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], cursor = 'question_arrow', command = about)
ig_lbl.pack(anchor = NW)

def start():
    global warning_lbl
    global palet

    warning_lbl = Label(top, image = warning, bg = palet[0]['bg'])
    warning_lbl.place(x = 180, y = 50)

    w_lbl = Message(top, text = 'Não interrompa o bot enquanto ele estiver em execução. Se quiser encerrá-lo clique no botão "Parar e Voltar ao início"', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 20), justify = CENTER, width = 500)
    w_lbl.place(x = 76, y = 298)

    w1_lbl = Label(top, text = 'O bot está sendo iniciado', font = ('Antipasto', 18), bg = palet[0]['bg'], fg = palet[0]['fg'], pady = 70)
    # w1_lbl.pack(anchor = S, side = BOTTOM)
    w1_lbl.place(x = 183, y = 405)
    top.update()
    sleep(1)

    for ani1 in range(0, 2):
        for ani in range(0, 4):
            w1_lbl.config(text = f'O bot está sendo iniciado{" ." * ani}')
            top.update()
            sleep(.3)

    w1_lbl.config(text = 'O bot está sendo iniciado')
    bot(root, top, warning_lbl, w_lbl, w1_lbl, palet)

def program():
    global cont_show_pass
    global comment_radio_var
    global user_entry
    global passw_entry
    global link_entry
    global v_comment
    global r1
    global r2
    global comentarios
    global comment_entry
    global r3
    global r4
    global lbl
    global bt_iniciar_bot
    global quant_comments_spinbox
    global remove_coment
    global comments_list
    global view
    global lbl1
    global lbl2
    global lbl3
    global avançar
    global ig_wallp_lbl
    
    cont_show_pass = 0
    cont_atalho = 0
    comment_radio_var = IntVar()
    ncom_radio_var = IntVar()

    avançar.destroy()
    ig_wallp_lbl.destroy()

    def login():
        global lbl
        global lbl1
        global user_entry
        global passw_entry
        global cont_click_user
        global cont_click_passw
        global cont_start
        global entry_img
        global entry_img1
        global entry_img_lbl
        global entry_img_lbl1
        global login_img
        global login_lbl
        global entrar
        global bt_entrar0
        global bt_entrar1
        global bt_entrar2
        global user_lbl
        global passw_lbl
        global lbl_tel
        global lbl_passw
        global var1
        global var2

        user_lbl, passw_lbl = True, True

        def pass_show(event = ''):
            global cont_show_pass
            cont_show_pass += 1
            if cont_show_pass % 2 != 0:
                passw_entry.config(show = '')
                view.config(text = 'Ocultar')
            else:
                passw_entry.config(show = '*')
                view.config(text = 'Mostrar')
                
        cont_click_user = 0
        cont_click_passw = 0
        cont_start = 0

        def user_click(event = ''):
            global cont_click_user
            global cont_click_passw
            global cont_start
            global user_lbl
            global lbl_tel
            global lbl_passw

            user_entry.focus_set()

            # lbl_tel.destroy()
            # print(cont_start)

            # if cont_click_user > 0:
            #     lbl_passw = Label(top, text = 'Senha', font = ('Antipasto'), bg = palet[0]['wd_bg'], fg = palet[0]['fg'])
            #     lbl_passw.place(x = 164, y = 384)

            # cont_start += 1
            # cont_click_user += 1

        def passw_click(event = ''):
            global cont_click_user
            global cont_click_passw
            global cont_start
            global passw_lbl
            global lbl_tel
            global lbl_passw

            # print(cont_start)
            # lbl_passw.destroy()

            # if cont_click_passw > 0:
            #     lbl_tel = Label(top, text = 'Telefone, nome de usuário ou email', font = ('Antipasto'), bg = palet[0]['wd_bg'], fg = palet[0]['fg'])
            #     lbl_tel.place(x = 164, y = 318)

            # cont_start += 1
            # cont_click_passw += 1

        def write1(*args):
            global passw_entry
            global user_entry
            global entrar
            global bt_entrar0
            global bt_entrar1
            global user_lbl
            global lbl_tel

            # if len(str(user_entry.get())) >= 1:
            #     lbl_tel.destroy()

            # if len(str(user_entry.get())) == 0:
            #     lbl_tel = Label(top, text = 'Senha', font = ('Antipasto'), bg = palet[0]['wd_bg'], fg = palet[0]['fg'])
            #     lbl_tel.place(x = 164, y = 384)

            if len(str(user_entry.get())) > 0:
                lbl_tel.destroy()
            else:
                lbl_tel = Label(top, text = 'Senha', font = ('Antipasto'), bg = palet[0]['wd_bg'], fg = palet[0]['fg'])
                lbl_tel.place(x = 164, y = 384)
                top.update()


            # if str(user_entry.get()) == '':
            #     user_lbl = True
            # else:
            #     user_lbl = False

            # if str(user_entry.get()) == '' or len(str(passw_entry.get())) < 6:
            #     entrar.config(image = bt_entrar1, state = DISABLED)
            # else:
            #     entrar.config(image = bt_entrar1, state = ACTIVE)

        def write2(*args):
            global passw_entry
            global user_entry
            global entrar
            global bt_entrar0
            global bt_entrar1
            global passw_lbl

            if str(passw_entry.get()) == 'Senha' or str(passw_entry.get()) == '':
                user_entry.bind('<Button-1>', user_click)
                passw_entry.bind('<Button-1>', passw_click)
            else:
                passw_entry.bind('<Button-1>', lambda e: print)

            if str(user_entry.get()) == '' or len(str(passw_entry.get())) < 6:
                entrar.config(state = DISABLED)
            else:
                entrar.config(state = ACTIVE)

        # lbl = Label(top, text = 'Nome de usuário', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
        # lbl.place(x = 60, y = 100)

        # lbl1 = Label(top, text = '@', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
        # lbl1.place(x = 37, y = 125)

        login_img = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\login_character.png')
        login_img = login_img.subsample(12, 12)

        bt_entrar0 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_entrar0.png')
        bt_entrar0 = bt_entrar0.subsample(8, 8)

        bt_entrar1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_entrar1.png')
        bt_entrar1 = bt_entrar1.subsample(8, 8)

        bt_entrar2 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_entrar2.png')
        bt_entrar2 = bt_entrar2.subsample(8, 8)
        
        # entry_img = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\entry.png')
        # entry_img = entry_img.subsample(4, 6)

        # entry_img1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\entry.png')
        # entry_img1 = entry_img1.subsample(5, 6)

        login_lbl = Label(top, image = login_img, bg = palet[0]['bg'])
        login_lbl.place(x = 242, y = 102)


        img = Image.open('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\entry.png')
        img = img.resize((390, 50), Image.ANTIALIAS)
        entry_img = ImageTk.PhotoImage(img)

        entry_img_lbl = Label(top, image = entry_img, bg = palet[0]['bg'])
        entry_img_lbl.place(x = 142, y = 302)
        
        entry_img_lbl2 = Label(top, image = entry_img, bg = palet[0]['bg'])
        entry_img_lbl2.place(x = 142, y = 368)

        # u_f = Frame(top, bg = '#4d4d4d', width = 366, height = 25, relief = SUNKEN, borderwidth = 0)
        # u_f.place(x = 162, y = 310)

        # user_entry = Entry(top, bg = palet[0]['wd_bg'], bd = 0, width = 30, font = ('Antipasto'), fg = palet[0]['fg'], selectbackground = palet[0]['df_bg'])
        # user_entry.place(x = 164, y = 312)

        var1 = StringVar()
        var1.trace('w', write1)
        
        var2 = StringVar()
        var2.trace('w', write2)

        user_entry = Entry(top, bg = palet[0]['wd_bg'], bd = 0, width = 30, font = ('Antipasto'), textvariable = var1, fg = palet[0]['fg'], selectbackground = palet[0]['df_bg'])
        
        user_entry.place(x = 164, y = 318)

        # user_entry.insert(END, 'Telefone, nome de usuário ou email')

        lbl_tel = Label(top, text = 'Telefone, nome de usuário ou email', font = ('Antipasto'), bg = palet[0]['wd_bg'], fg = palet[0]['fg'])
        lbl_tel.place(x = 164, y = 318)

        # lbl2 = Label(top, text = 'Senha', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
        # lbl2.place(x = 60, y = 165)

        passw_entry = Entry(top, bg = palet[0]['wd_bg'], bd = 0, width = 25, font = ('Antipasto'), textvariable = var2, fg = palet[0]['fg'], selectbackground = palet[0]['df_bg'], show = '*')
        passw_entry.place(x = 164, y = 384)

        lbl_passw = Label(top, text = 'Senha', font = ('Antipasto'), bg = palet[0]['wd_bg'], fg = palet[0]['fg'])
        lbl_passw.place(x = 164, y = 384)

        # passw_entry.insert(END, 'Senha')

        view = Button(top, text = 'Mostrar', bd = 0, bg = palet[0]['wd_bg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], fg = palet[0]['fg'], font = ('Antipasto', 12), cursor = 'hand2', command = pass_show)
        view.place(x = 462, y = 380)

        def ent_enter(e):
            entrar.config(image = bt_entrar2)

        def ent_leave(e):
            entrar.config(image = bt_entrar1)
        
        def prox():
            user_entry.destroy()
            passw_entry.destroy()
            entry_img_lbl.destroy()
            entry_img_lbl2.destroy()
            login_lbl.destroy()
            view.destroy()
            entrar.destroy()
            pub()

        entrar = Button(top, image = bt_entrar0, compound = CENTER, bd = 0, bg = palet[0]['bg'], activebackground = palet[0]['bg'], cursor = 'hand2', command = prox)
        # entrar.pack(anchor = CENTER, side = BOTTOM)
        entrar.place(x = 270, y = 460)

        entrar.bind('<Enter>', ent_enter)
        entrar.bind('<Leave>', ent_leave)
        lbl_tel.bind('<Button-1>', user_click)
        lbl_passw.bind('<Button-1>', passw_click)


    def pub():
        global cont_show_pass
        global comment_radio_var
        global link_entry
        global v_comment
        global r1
        global r2
        global comentarios
        global comment_entry
        global r3
        global r4
        global lbl
        global bt_iniciar_bot
        global quant_comments_spinbox
        global remove_coment
        global comments_list
        global view
        global lbl1
        global lbl2
        global lbl3
        global avançar
        global ig_wallp_lbl

        lbl3 = Label(top, text = 'Link da publicação', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
        lbl3.place(x = 60, y = 95)

        link_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 30, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'])
        link_entry.place(x = 60, y = 130)

        # def user_key(event):
        #     global passw_entry
        #     passw_entry.focus_set()

        # def passw_key(event):
        #     global link_entry
        #     link_entry.focus_set()

        # user_entry.bind('<Return>', passw_entry)
        # passw_entry.bind('<Return>', link_entry)

        def c_unico():
            global comentarios
            global v_comment
            global r1
            global r2
            global comment_entry
            global lbl4
            global comment_entry_verify

            v_comment = False
            r1.config(state = DISABLED, cursor = 'X_cursor')
            r2.config(state = ACTIVE, cursor = 'hand2')

            try:
                comment_entry.destroy()
            except:
                pass
            
            try:
                lbl4.destroy()
            except:
                pass

            try:
                add_comment.destroy()
                comments_list.destroy()
                c_list_f.destroy()
                sb.destroy()
                lbl_list.destroy()
                comentarios = []
            except:
                pass

            def write_comment(*args):
                a = comment_entry.get()

                if a[len(a) - 1:] == '-':
                    comment_entry.delete(len(a) - 1)
            
            comment_entry_verify = StringVar()
            comment_entry_verify.trace('w', write_comment)

            lbl4 = Label(top, text = 'Comentário', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
            lbl4.place(x = 60, y = 230)

            comment_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 24, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'], textvariable = comment_entry_verify)
            comment_entry.place(x = 60, y = 265)


        def varios_c():
            global add_comment
            global comments_list
            global c_list_f
            global sb
            global lbl_list
            global comment_entry_verify
            global sb
            global idx
            global remove_coment
            global v_comment
            global comment_entry
            global r1
            global r2
            global lbl4

            idx = 0
            v_comment = True
            r1.config(state = ACTIVE, cursor = 'hand2')
            r2.config(state = DISABLED, cursor = 'X_cursor')

            try:
                comment_entry.destroy()
            except:
                pass
            
            try:
                lbl4.destroy()
            except:
                pass

            def adicionar_coment(event = ''):
                global comentarios;global sb
                if comment_entry.get() != '':
                    comentarios.append(str(comment_entry.get()))
                    comment_entry.delete(0, END)
                    comments_list.insert(END, comentarios[len(comentarios) - 1])
                    sb.config(command = comments_list.yview)

            def cur_select(evt):
                global idx
                try:
                    idx = comments_list.curselection()[0]
                    remove_coment.config(state = ACTIVE, cursor = 'hand2')
                    comments_list.bind('<Delete>', r_comment)
                except:
                    pass

            def r_comment(event = ''):
                question_window = Toplevel(top)
                question_window.config(bg = palet[0]['bg'])
                question_window.geometry('380x210+466+265')
                question_window.grab_set()
                question_window.overrideredirect(True)
                question_window.attributes('-alpha', 0.95)

                remove_coment.config(state = DISABLED, cursor = 'X_cursor')

                w1 = Frame(question_window, bg = palet[0]['bg'])
                w1.pack(anchor = NW)
                w2 = Frame(question_window, bg = palet[0]['bg'])
                w2.pack(anchor = SE, side = BOTTOM)

                def sim(event = ''):
                    comentarios.pop(idx)
                    comments_list.delete(idx)
                    question_window.destroy()
                    remove_coment.config(state = DISABLED)
                    print(comentarios)

                def not_or_cancel(event = ''):
                    question_window.destroy()
                    remove_coment.config(state = ACTIVE, cursor = 'hand2')

                def x_pop_enter(e = ''):
                    fechar_popup.config(bg = palet[0]['exit_bg'])

                def x_pop_leave(e = ''):
                    fechar_popup.config(bg = palet[0]['bg'])

                def n_enter(e = ''):
                    n.config(bg = palet[0]['df_bg'])

                def n_leave(e = ''):
                    n.config(bg = palet[0]['bg'])

                def s_enter(e = ''):
                    s.config(bg = palet[0]['df_bg'])

                def s_leave(e = ''):
                    s.config(bg = palet[0]['bg'])


                n = Button(w2, text = 'Não', bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], bd = 0, width = 10, font = ('Antipasto', 18), pady = 6, padx = 6, command = not_or_cancel)
                n.pack(anchor = SE, side = RIGHT)

                s = Button(w2, text = 'Sim', bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], bd = 0, width = 10, font = ('Antipasto', 18), pady = 6, padx = 6, command = sim)
                s.pack(anchor = SE, side = BOTTOM)

                n_enter()
                
                lbl_warning1 = Label(question_window, text = 'Você realmente deseja \n   apagar este comentário?', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 18), pady = 25)
                lbl_warning1.pack(anchor = NW, side = LEFT, expand = False)
                    
                fechar_popup = Button(question_window, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = not_or_cancel)
                fechar_popup.pack(anchor = NE, side = RIGHT, before = lbl_warning1)

                def n_f(event):
                    try:
                        s_leave()
                    except:
                        pass
                    n_enter()
                    question_window.bind('<Return>', not_or_cancel)

                def s_f(event):
                    try:
                        n_leave()
                    except:
                        pass
                    s_enter()
                    question_window.bind('<Return>', sim)
                
                fechar_popup.bind('<Enter>', x_pop_enter)
                fechar_popup.bind('<Leave>', x_pop_leave)
                n.bind('<Enter>', n_enter)
                n.bind('<Leave>', n_leave)
                s.bind('<Enter>', s_enter)
                s.bind('<Leave>', s_leave)
                question_window.bind('<Left>', s_f)
                question_window.bind('<Right>', n_f)

                question_window.mainloop()

            def write_comment(*args):
                if str(comment_entry.get()).strip() == '':
                    add_comment.config(state = DISABLED, cursor = 'X_cursor')
                else:
                    add_comment.config(state = ACTIVE, cursor = 'hand2')

                a = comment_entry.get()

                if a[len(a) - 1:] == '-':
                    comment_entry.delete(len(a) - 1)

            def add_comment_enter(e):
                add_comment.config(bg = palet[0]['df_bg'])

            def add_comment_leave(e):
                add_comment.config(bg = palet[0]['bg'])
                
            def remove_coment_enter(e):
                remove_coment.config(bg = palet[0]['df_bg'])

            def remove_coment_leave(e):
                remove_coment.config(bg = palet[0]['bg'])
                
            
            lbl4 = Label(top, text = 'Comentário', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
            lbl4.place(x = 60, y = 230)

            comment_entry_verify = StringVar()
            comment_entry_verify.trace('w', write_comment)

            comment_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 24, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'], textvariable = comment_entry_verify)
            comment_entry.place(x = 60, y = 265)

            add_comment = Button(top, text = 'Adicionar', width = 9, bg = palet[0]['bg'], bd = 0, font = ('Antipasto'), fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], command = adicionar_coment, state = DISABLED, cursor = 'X_cursor')
            add_comment.place(x = 350, y = 262)

            add_comment.bind('<Enter>', add_comment_enter)
            add_comment.bind('<Leave>', add_comment_leave)

            c_list_f = Frame(top, bg = palet[0]['bg'])
            c_list_f.place(x = 450, y = 130)

            sb = Scrollbar(c_list_f)
            sb.pack(side = RIGHT, fill = Y)

            lbl_list = Label(top, text = 'Lista de comentários', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16), highlightthickness = 0)
            lbl_list.place(x = 448, y = 100)

            comments_list = Listbox(c_list_f, bd = 0, width = 17, height = 12, yscrollcommand = sb.set, bg = palet[0]['fg'], fg = palet[0]['bg'], font = ('Antipasto'), selectbackground = palet[0]['df_bg'])
            comments_list.bind('<<ListboxSelect>>', cur_select)
            comments_list.pack()

            remove_coment = Button(c_list_f, text = 'Remover', width = 9, bg = palet[0]['bg'], bd = 0, font = ('Antipasto'), fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], command = r_comment, state = DISABLED, cursor = 'X_cursor')
            remove_coment.pack(side = BOTTOM, fill = X, before = sb)

            remove_coment.bind('<Enter>', remove_coment_enter)
            remove_coment.bind('<Leave>', remove_coment_leave)
            comment_entry.bind('<Return>', adicionar_coment)

        def quant_coment():
            global limit2;global s2;global s1;global quant_comments_spinbox;global quant_comentarios;global r3;global r4
            s1, s2 = '', ''
            quant_comentarios = True
            r3.config(state = DISABLED, cursor = 'X_cursor')
            r4.config(state = ACTIVE, cursor = 'hand2')

            try:
                loop.destroy()
            except:
                pass

            def write2(*args):
                global s2;global s1;global quant_comments_spinbox

                if len(s2) > 0:
                    if not s2[-1].isdigit():
                        limit2.set(s2[:-1])
                    else:
                        limit2.set(s2[:9])

            limit2 = StringVar()

            quant_comments_spinbox = Spinbox(top, from_ = 1, to_ = 100000000, width = 6, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], textvariable = limit2, font = ('Antipasto', 25), selectbackground = palet[0]['bg'], selectforeground = palet[0]['df_bg'], bd = 0, buttonbackground = palet[0]['bg'])
            quant_comments_spinbox.place(x = 60, y = 410)

            limit2.trace('w', write2)


        def sel_comment():
            # global comment_radio_var
            if comment_radio_var.get() == 1:
                c_unico()
            elif comment_radio_var.get() == 2:
                varios_c()

        def sel_ncom():
            global quant_comentarios;global r3;global r4;global loop
            if ncom_radio_var.get() == 1:
                quant_coment()
            elif ncom_radio_var.get() == 2:
                try:
                    quant_comments_spinbox.destroy()
                except:
                    pass
                quant_comentarios = False
                r4.config(state = DISABLED, cursor = 'X_cursor')
                r3.config(state = ACTIVE, cursor = 'hand2')
                loop = Label(top, text = '∞', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 40))
                loop.place(x = 270, y = 410)

        r1 = Radiobutton(top, text = 'Comentário único', font = ('Antipasto', 16), variable = comment_radio_var, value = 1, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_comment, cursor = 'hand2')
        r1.place(x = 60, y = 180)
        
        r2 = Radiobutton(top, text = 'Vários comentários', font = ('Antipasto', 16), variable = comment_radio_var, value = 2, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_comment, cursor = 'hand2')
        r2.place(x = 240, y = 180)

        r3 = Radiobutton(top, text = 'Escolher quantidade \nde comentários', font = ('Antipasto', 16), variable = ncom_radio_var, value = 1, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_ncom, cursor = 'hand2')
        r3.place(x = 60, y = 340)
        
        r4 = Radiobutton(top, text = 'Infinito (Até \nvocê parar)', font = ('Antipasto', 16), variable = ncom_radio_var, value = 2, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_ncom, cursor = 'hand2')
        r4.place(x = 260, y = 350)

        def error(msg):
            question_window = Toplevel(top)
            question_window.config(bg = palet[0]['bg'])
            question_window.geometry('380x210+466+265')
            question_window.grab_set()
            question_window.focus_force()
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

            def last_click(event):
                global click_x;global click_y
                click_x = event.x
                click_y = event.y

            def move_window(event):
                if 32 >= click_y >= 0:
                    x, y = event.x - click_x + question_window.winfo_x(), event.y - click_y + question_window.winfo_y()
                    question_window.geometry(f'+{x}+{y}')
            
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
            question_window.bind('<Button-1>', last_click)
            question_window.bind('<B1-Motion>', move_window)
            question_window.bind('<Return>', question_window.destroy)

            question_window.mainloop()

        def iniciar_bot(event = ''):
            global lbl
            global user_entry
            global passw_entry
            global view
            global link_entry
            global r1
            global r2
            global comment_entry
            global add_comment
            global sb
            global lbl_list
            global comments_list
            global remove_coment
            global quant_comments_spinbox
            global r3
            global r4
            global bt_iniciar_bot
            global comentarios
            global c_list_f
            global loop

            if user_entry.get() == '' or passw_entry.get() == '' or link_entry.get() == '' or v_comment == None or quant_comentarios == None or v_comment == True and comentarios == [] or v_comment == False and comment_entry.get() == '' or len(passw_entry.get()) < 6:
                error('Houve algum erro, insira os dados CORRETAMENTE e tente de novo')
            else:
                def var():
                    variaveis = open('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\variables.txt', 'w')
                    variaveis.write(f'{user_entry.get()}\n') # Nome de usuário
                    variaveis.write(f'{passw_entry.get()}\n') # Senha
                    variaveis.write(f'{link_entry.get()}\n') # Link do post
                    variaveis.write(f'{v_comment}\n') # Comentário único ou vários
                    variaveis.write(f'{quant_comentarios}\n') # Comentários limitados ou ilimitados
                    if comentarios == []:
                        variaveis.write(f'{comentarios}\n')
                    else:
                        for i, item in enumerate(comentarios):
                            if i == len(comentarios) - 1:
                                variaveis.write(f'{item}\n')
                            else:
                                variaveis.write(f'{item}-')

                    variaveis.write(f'{comment_entry.get()}\n') # Comentário único
                    try:
                        variaveis.write(f'{quant_comments_spinbox.get()}') # Número de comentários
                    except:
                        variaveis.write('\n')
                    variaveis.close()

                var()
                user_entry.destroy()
                passw_entry.destroy()
                view.destroy()
                link_entry.destroy()
                r1.destroy()
                r2.destroy()
                comment_entry.destroy()
                r3.destroy()
                r4.destroy()
                bt_iniciar_bot.destroy()
                lbl.destroy()
                lbl1.destroy()
                lbl2.destroy()
                lbl3.destroy()
                lbl4.destroy()
                try:
                    quant_comments_spinbox.destroy()
                except:
                    pass
                if v_comment == True:
                    c_list_f.destroy()
                    sb.destroy()
                    lbl_list.destroy()
                    comments_list.destroy()
                    remove_coment.destroy()
                    add_comment.destroy()
                else:
                    try:
                        loop.destroy()
                    except:
                        pass
                start()

        def iniciar_bot_enter(e):
            bt_iniciar_bot.config(image = in_bot2)

        def iniciar_bot_leave(e):
            bt_iniciar_bot.config(image = in_bot1)

        bt_iniciar_bot = Button(top, image = in_bot1, bd = 0, bg = palet[0]['bg'], activebackground = palet[0]['bg'], cursor = 'hand2', command = iniciar_bot)
        # bt_iniciar_bot.pack(anchor = SE, side = RIGHT)
        bt_iniciar_bot.place(x = width - 180, y = height - 70)

        bt_iniciar_bot.bind('<Enter>', iniciar_bot_enter)
        bt_iniciar_bot.bind('<Leave>', iniciar_bot_leave)
        top.bind('<Shift-Return>', iniciar_bot)

    login()

def welcome_interface():
    global ig_wallp
    # global welcome
    global avançar
    global ig_wallp_lbl
    # global a
    global ani_cont
    # welcome = Frame(top, bg = palet[0]['bg'])
    # welcome.pack(anchor = CENTER, side = RIGHT)
    ani_cont = None

    def animation1():
        global ani_cont
        ig_wallp_lbl.config(state = DISABLED)
        avançar.config(state = DISABLED, cursor = 'X_cursor')
        for ani in range(600, 140, -5):
            if ani_cont == False:
                break
            ig_wallp_lbl.place(x = ani, y = 130)
            top.update()
            sleep(0.0001)
        ig_wallp_lbl.config(state = ACTIVE)
        avançar.config(state = ACTIVE, cursor = 'hand2')

    def animation2():
        global ani_cont
        ig_wallp_lbl.config(state = DISABLED)
        avançar.config(state = DISABLED, cursor = 'X_cursor')
        for ani2 in range(130, -550, -5):
            if ani_cont == False:
                break
            ig_wallp_lbl.place(x = ani2, y = 130)
            top.update()
            sleep(0.0001)
        sleep(0.1)
        ig_wallp_lbl.config(state = ACTIVE)
        avançar.config(state = ACTIVE, cursor = 'hand2')
        animation1()


    ig_wallp = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\title.png')
    ig_wallp = ig_wallp.subsample(6, 6)

    bt_start_1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_start_1.png')
    bt_start_1 = bt_start_1.subsample(5, 5)

    bt_start_2 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_start_2.png')
    bt_start_2 = bt_start_2.subsample(5, 5)

    ig_wallp_lbl = Button(top, image = ig_wallp, bg = palet[0]['bg'], bd = 0, activebackground = palet[0]['bg'], command = animation2, cursor = 'exchange')
    # ig_wallp_lbl.pack()
    ig_wallp_lbl.place(x = 130, y = 130)

    def com_enter(e):
        avançar.config(image = bt_start_2)

    def com_leave(e):
        avançar.config(image = bt_start_1)

    def nxt(event = ''):
        global ani_cont
        # welcome.destroy()
        ig_wallp_lbl.destroy()
        avançar.destroy()
        # a.destroy()
        ani_cont = False
        program()

    avançar = Button(top, image = bt_start_1, compound = CENTER, bd = 0, bg = palet[0]['bg'], activebackground = palet[0]['bg'], command = nxt, cursor = 'hand2')
    # avançar.pack(anchor = CENTER, side = BOTTOM)
    avançar.place(x = 250, y = 430)

    avançar.bind('<Enter>', com_enter)
    avançar.bind('<Leave>', com_leave)
    avançar.bind_all('<Shift-Return>', nxt)

    # threading.Thread(target = animation1).start()
    animation1()

    # a = welcome = Frame(top, bg = palet[0]['bg'], height = 80)
    # a.pack(anchor = S, side = BOTTOM)

welcome_interface()
top.mainloop()
