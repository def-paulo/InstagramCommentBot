from tkinter import *
from time import sleep
from backend import bot

palet = [{'bg':'#141414', 'fg':'#f1f1f1', 'exit_bg':'#ff2f2f', 'df_bg':'#676767'}]
cont_maximizado = 0
comentarios = []
v_comment = None
width, height = 700, 550
quant_comentarios = None

def managment_window():

    def x_enter(e):
        fechar.config(bg = palet[0]['exit_bg'])

    def x_leave(e):
        fechar.config(bg = palet[0]['bg'])

    def max_enter(e):
        maximizar.config(bg = palet[0]['df_bg'])

    def max_leave(e):
        maximizar.config(bg = palet[0]['bg'])

    def min_enter(e):
        minimizar.config(bg = palet[0]['df_bg'])

    def min_leave(e):
        minimizar.config(bg = palet[0]['bg'])
        
    def maxi():
        global cont_maximizado
        cont_maximizado += 1
        if cont_maximizado % 2 != 0:
            top.geometry(f'{top.winfo_screenwidth()}x{top.winfo_screenheight()}+0+0')
            maximizar.config(image = resize_maximize)
        else:
            top.geometry('700x530+360+160')
            maximizar.config(image = maximize)

    def minimizing():
        top.withdraw()
        # top.deiconify()

    fechar = Button(top, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = top.destroy)
    fechar.pack(anchor = NE, side = RIGHT)

    maximize = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\max.png')
    maximize = maximize.subsample(45, 45)

    resize_maximize = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\res_max.png')
    resize_maximize = resize_maximize.subsample(45, 45)

    maximizar = Button(top, image = maximize, compound = CENTER, pady = 100, height = 36, width = 40, bd = 0, activebackground = palet[0]['df_bg'], bg = palet[0]['bg'], highlightcolor = palet[0]['exit_bg'], command = maxi, state = DISABLED)
    maximizar.pack(anchor = NE, side = RIGHT)

    minimizar = Button(top, text = '-', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15, 'bold'), activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = minimizing)
    minimizar.pack(anchor = NE, side = RIGHT)

    fechar.bind('<Enter>', x_enter)
    fechar.bind('<Leave>', x_leave)
    # maximizar.bind('<Enter>', max_enter)
    # maximizar.bind('<Leave>', max_leave)
    minimizar.bind('<Enter>', min_enter)
    minimizar.bind('<Leave>', min_leave)

root = Tk()
root.iconbitmap('C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\instagram.ico')
root.attributes('-alpha', 0.0)
root.title('Instagram Bot')
root.config(bg = palet[0]['bg'])
top = Toplevel(root)
top.geometry(f'{width}x{height}+360+120')
top.config(bg = palet[0]['bg'])
top.overrideredirect(True)
top.attributes('-toolwindow')

def on(event):
    top.withdraw()
root.bind("<Unmap>", on)
def off(event):
    top.deiconify()
root.bind("<Map>", off)

managment_window()

ig = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\instagram.png')
ig = ig.subsample(13, 13)

warning = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\warning.png')
warning = warning.subsample(4, 4)

ig_icon = Label(top, image = ig, bg = palet[0]['bg'], height = 38, width = 40)
ig_icon.pack(anchor = NW, side = LEFT)

ig_lbl = Label(top, text = 'Instagram Bot', font = ('Antipasto', 16), bg = palet[0]['bg'], fg = palet[0]['fg'], pady = 7)
ig_lbl.pack(anchor = NW)

def start():
    global warning_lbl;global palet
    # w = Frame(top, bg = palet[0]['bg'])
    # w.pack()

    warning_lbl = Label(top, image = warning, bg = palet[0]['bg'])
    warning_lbl.place(x = 180, y = 50)

    w_lbl = Message(top, text = 'Não interrompa o bot enquanto ele estiver em execução. Se quiser encerrá-lo clique no botão "Parar"', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 20), justify = CENTER, width = 500)
    w_lbl.place(x = 76, y = 298)

    w1_lbl = Label(top, text = 'O bot está sendo iniciado', font = ('Antipasto', 18), bg = palet[0]['bg'], fg = palet[0]['fg'], pady = 70)
    # w1_lbl.pack(anchor = S, side = BOTTOM)
    w1_lbl.place(x = 183, y = 405)
    top.update()
    sleep(1)

    # for ani1 in range(0, 2):
    #     for ani in range(0, 4):
    #         w1_lbl.config(text = f'O bot está sendo iniciado{" ." * ani}')
    #         top.update()
    #         sleep(.3)

    # w1_lbl.config(text = 'O bot está sendo iniciado')
    bot(top, warning_lbl, w_lbl, w1_lbl, palet)

def program():
    global cont_show_pass;global comment_radio_var;global user_entry;global passw_entry;global link_entry;global v_comment;global r1;global r2;global comentarios;global comment_entry;global r3;global r4;global lbl;global bt_iniciar_bot;global quant_comments_spinbox;global remove_coment;global comments_list;global view;global lbl1;global lbl2;global lbl3
    cont_show_pass = 0
    comment_radio_var = IntVar()
    ncom_radio_var = IntVar()
    global welcome
    global avançar
    global ig_wallp_lbl
    global a

    a.destroy()
    welcome.destroy()
    avançar.destroy()
    ig_wallp_lbl.destroy()

    def pass_show():
        global cont_show_pass
        cont_show_pass += 1
        if cont_show_pass % 2 != 0:
            passw_entry.config(show = '')
            view.config(text = 'o')
        else:
            passw_entry.config(show = '*')
            view.config(text = 'ø')


    lbl = Label(top, text = 'Nome de usuário', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
    lbl.place(x = 60, y = 100)

    lbl1 = Label(top, text = '@', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
    lbl1.place(x = 37, y = 125)

    user_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 30, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'])
    user_entry.place(x = 60, y = 130)

    lbl2 = Label(top, text = 'Senha', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
    lbl2.place(x = 60, y = 165)

    passw_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 20, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'], show = '*')
    passw_entry.place(x = 60, y = 195)

    view = Button(top, text = 'ø', bd = 0, bg = palet[0]['bg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], fg = palet[0]['fg'], font = ('Antipasto', 20), command = pass_show)
    view.place(x = 310, y = 177)

    lbl3 = Label(top, text = 'Link da publicação', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 16))
    lbl3.place(x = 60, y = 230)

    link_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 30, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'])
    link_entry.place(x = 60, y = 260)

    def c_unico():
        global comentarios;global v_comment;global r1;global r2;global comment_entry;global lbl4;global comment_entry_verify

        v_comment = False
        r1.config(state = DISABLED)
        r2.config(state = ACTIVE)

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
        lbl4.place(x = 60, y = 340)

        comment_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 24, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'], textvariable = comment_entry_verify)
        comment_entry.place(x = 60, y = 375)


    def varios_c():
        global add_comment;global comments_list;global c_list_f;global sb;global lbl_list;global comment_entry_verify;global sb;global idx;global remove_coment;global v_comment;global comment_entry;global r1;global r2;global lbl4

        idx = 0
        v_comment = True
        r1.config(state = ACTIVE)
        r2.config(state = DISABLED)

        try:
            comment_entry.destroy()
        except:
            pass
        
        try:
            lbl4.destroy()
        except:
            pass

        def adicionar_coment():
            global comentarios;global sb
            comentarios.append(str(comment_entry.get()))
            comment_entry.delete(0, END)
            comments_list.insert(END, comentarios[len(comentarios) - 1])
            sb.config(command = comments_list.yview)

        def cur_select(evt):
            global idx
            try:
                idx = comments_list.curselection()[0]
                remove_coment.config(state = ACTIVE)
            except:
                pass

        def r_comment():
            question_window = Toplevel(top)
            question_window.config(bg = palet[0]['bg'])
            question_window.geometry('380x210+466+265')
            question_window.grab_set()
            question_window.overrideredirect(True)
            question_window.attributes('-alpha', 0.95)

            remove_coment.config(state = DISABLED)

            w1 = Frame(question_window, bg = palet[0]['bg'])
            w1.pack(anchor = NW)
            w2 = Frame(question_window, bg = palet[0]['bg'])
            w2.pack(anchor = SE, side = BOTTOM)

            def sim():
                comentarios.pop(idx)
                comments_list.delete(idx)
                question_window.destroy()
                print(comentarios)

            def not_or_cancel():
                question_window.destroy()
                remove_coment.config(state = ACTIVE)

            def x_pop_enter(e):
                fechar_popup.config(bg = palet[0]['exit_bg'])

            def x_pop_leave(e):
                fechar_popup.config(bg = palet[0]['bg'])

            def n_enter(e):
                n.config(bg = palet[0]['df_bg'])

            def n_leave(e):
                n.config(bg = palet[0]['bg'])

            def s_enter(e):
                s.config(bg = palet[0]['df_bg'])

            def s_leave(e):
                s.config(bg = palet[0]['bg'])


            n = Button(w2, text = 'Não', bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], bd = 0, width = 10, font = ('Antipasto', 18), pady = 6, padx = 6, command = not_or_cancel)
            n.pack(anchor = SE, side = RIGHT)

            s = Button(w2, text = 'Sim', bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], bd = 0, width = 10, font = ('Antipasto', 18), pady = 6, padx = 6, command = sim)
            s.pack(anchor = SE, side = BOTTOM)
            
            lbl_warning1 = Label(question_window, text = 'Você realmente deseja \n   apagar este comentário?', bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 18), pady = 25)
            lbl_warning1.pack(anchor = NW, side = LEFT, expand = False)
                
            fechar_popup = Button(question_window, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = not_or_cancel)
            fechar_popup.pack(anchor = NE, side = RIGHT, before = lbl_warning1)
            
            fechar_popup.bind('<Enter>', x_pop_enter)
            fechar_popup.bind('<Leave>', x_pop_leave)
            n.bind('<Enter>', n_enter)
            n.bind('<Leave>', n_leave)
            s.bind('<Enter>', s_enter)
            s.bind('<Leave>', s_leave)

            question_window.mainloop()

        def write_comment(*args):
            if str(comment_entry.get()).strip() == '':
                add_comment.config(state = DISABLED)
            else:
                add_comment.config(state = ACTIVE)

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
        lbl4.place(x = 60, y = 340)

        comment_entry_verify = StringVar()
        comment_entry_verify.trace('w', write_comment)

        comment_entry = Entry(top, bg = palet[0]['fg'], bd = 0, width = 24, font = ('Antipasto'), fg = palet[0]['bg'], selectbackground = palet[0]['df_bg'], textvariable = comment_entry_verify)
        comment_entry.place(x = 60, y = 375)

        add_comment = Button(top, text = 'Adicionar', width = 9, bg = palet[0]['bg'], bd = 0, font = ('Antipasto'), fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], command = adicionar_coment, state = DISABLED)
        add_comment.place(x = 350, y = 370)

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

        remove_coment = Button(c_list_f, text = 'Remover', width = 9, bg = palet[0]['bg'], bd = 0, font = ('Antipasto'), fg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['fg'], command = r_comment, state = DISABLED)
        remove_coment.pack(side = BOTTOM, fill = X, before = sb)

        remove_coment.bind('<Enter>', remove_coment_enter)
        remove_coment.bind('<Leave>', remove_coment_leave)

    def quant_coment():
        global limit2;global s2;global s1;global quant_comments_spinbox;global quant_comentarios;global r3;global r4
        s1, s2 = '', ''
        quant_comentarios = True
        r3.config(state = DISABLED)
        r4.config(state = ACTIVE)
        def write2(*args):
            global s2;global s1;global quant_comments_spinbox

            if len(s2) > 0:
                if not s2[-1].isdigit():
                    limit2.set(s2[:-1])
                else:
                    limit2.set(s2[:9])
            # try:
            #     s2 = list(s2)
            #     if s2 != []:
            #         if len(s2) > 1 and int(s2[0]) > 5:
            #             s2.pop(0)
            #             s2.insert(0, '5')
            #         if int(s2[0]) >= 5:
            #             if len(s2) >= 2 and int(s2[1]) > 9:
            #                 s2.pop(1)
            #                 s2.insert(1, '9')
            #         if len(s2) == 1:
            #             s2.insert(0, '0')
            #     else:
            #         s2 = ['0', '0']

            # except:
            #     pass

            

        limit2 = StringVar()

        quant_comments_spinbox = Spinbox(top, from_ = 1, to_ = 100000000, width = 6, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], textvariable = limit2, font = ('Antipasto', 25), selectbackground = palet[0]['bg'], selectforeground = palet[0]['df_bg'], bd = 0, buttonbackground = palet[0]['bg'])
        quant_comments_spinbox.place(x = 60, y = 480)

        limit2.trace('w', write2)


    def sel_comment():
        # global comment_radio_var
        if comment_radio_var.get() == 1:
            c_unico()
        elif comment_radio_var.get() == 2:
            varios_c()

    def sel_ncom():
        global quant_comentarios;global r3;global r4
        if ncom_radio_var.get() == 1:
            quant_coment()
        elif ncom_radio_var.get() == 2:
            try:
                quant_comments_spinbox.destroy()
            except:
                pass
            quant_comentarios = False
            r4.config(state = DISABLED)
            r3.config(state = ACTIVE)

    r1 = Radiobutton(top, text = 'Comentário único', font = ('Antipasto', 16), variable = comment_radio_var, value = 1, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_comment)
    r1.place(x = 60, y = 300)
    
    r2 = Radiobutton(top, text = 'Vários comentários', font = ('Antipasto', 16), variable = comment_radio_var, value = 2, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_comment)
    r2.place(x = 240, y = 300)

    # c_unico()

    r3 = Radiobutton(top, text = 'Escolher quantidade \nde comentários', font = ('Antipasto', 16), variable = ncom_radio_var, value = 1, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_ncom)
    r3.place(x = 60, y = 410)
    
    r4 = Radiobutton(top, text = 'Infinito (Até você parar)', font = ('Antipasto', 16), variable = ncom_radio_var, value = 2, bg = palet[0]['bg'], fg = palet[0]['fg'], activebackground = palet[0]['bg'], activeforeground = palet[0]['fg'], command = sel_ncom)
    r4.place(x = 260, y = 420)

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
        
        lbl_warning1 = Label(question_window, text = msg, bg = palet[0]['bg'], fg = palet[0]['fg'], font = ('Antipasto', 17), pady = 25, padx = 16)
        lbl_warning1.pack(anchor = NW, side = LEFT, expand = False)
        
        fechar_popup = Button(question_window, text = 'X', bd = 0, bg = palet[0]['bg'], fg = palet[0]['fg'], width = 3, font = ('Antipasto', 15), activebackground = palet[0]['exit_bg'], activeforeground = palet[0]['fg'], highlightcolor = palet[0]['exit_bg'], command = question_window.destroy)
        fechar_popup.pack(anchor = NE, side = RIGHT, before = lbl_warning1)
        
        fechar_popup.bind('<Enter>', x_pop_enter)
        fechar_popup.bind('<Leave>', x_pop_leave)
        n.bind('<Enter>', n_enter)
        n.bind('<Leave>', n_leave)

        question_window.mainloop()

    def iniciar_bot():
        global lbl;global user_entry;global passw_entry;global view;global link_entry;global r1;global r2;global comment_entry;global add_comment;global sb;global lbl_list;global comments_list;global remove_coment;global quant_comments_spinbox;global r3;global r4;global bt_iniciar_bot;global comentarios;global c_list_f
        # 
            # print(f'Nome de usuário: {user_entry.get()}')
            # print(f'Senha: {passw_entry.get()}')
            # print(f'Link: {link_entry.get()}')
            # print(f'Vários comentários?: {v_comment}')
            # print(f'Comentários limitados?: {quant_comentarios}')
            # if v_comment == True:
            #     print(f'Comentários: {comentarios}')
            # elif v_comment == False:
            #     print(f'Comentário: {comment_entry.get()}')

            # if quant_comentarios == True:
            #     print(f'Quantidade de comentários: {quant_comments_spinbox.get()}')

        if user_entry.get() == '' or passw_entry.get() == '' or link_entry.get() == '' or v_comment == None or quant_comentarios == None or v_comment == True and comentarios == [] or v_comment == False and comment_entry.get() == '':
            error('Houve algum erro, insira os dados \nCORRETAMENTE e tente de novo   ')
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
            start()

    def iniciar_bot_enter(e):
        bt_iniciar_bot.config(bg = palet[0]['df_bg'])

    def iniciar_bot_leave(e):
        bt_iniciar_bot.config(bg = palet[0]['fg'])

    bt_iniciar_bot = Button(top, text = 'Iniciar Bot', bd = 0, fg = palet[0]['bg'], bg = palet[0]['fg'], activebackground = palet[0]['df_bg'], activeforeground = palet[0]['bg'], font = ('Antipasto', 20), command = iniciar_bot)
    # bt_iniciar_bot.pack(anchor = SE, side = RIGHT)
    bt_iniciar_bot.place(x = width - 150, y = height - 80)

    bt_iniciar_bot.bind('<Enter>', iniciar_bot_enter)
    bt_iniciar_bot.bind('<Leave>', iniciar_bot_leave)

def welcome_interface():
    global ig_wallp
    global welcome;global avançar;global ig_wallp_lbl;global a
    welcome = Frame(top, bg = palet[0]['bg'])
    welcome.pack(anchor = CENTER, side = RIGHT)

    ig_wallp = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\title.png')
    ig_wallp = ig_wallp.subsample(6, 6)

    bt_start_1 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_start_1.png')
    bt_start_1 = bt_start_1.subsample(3, 3)

    bt_start_2 = PhotoImage(file = 'C:\\Users\\Paulo Thiago\\Documents\\MeusProjetos\\InstagramBot\\python-files_pt\\media\\bt_start_2.png')
    bt_start_2 = bt_start_2.subsample(3, 3)

    ig_wallp_lbl = Label(welcome, image = ig_wallp, bg = palet[0]['bg'])
    ig_wallp_lbl.pack()

    def com_enter(e):
        avançar.config(image = bt_start_2)

    def com_leave(e):
        avançar.config(image = bt_start_1)

    def nxt():
        welcome.destroy()
        ig_wallp_lbl.destroy()
        avançar.destroy()
        a.destroy()
        program()

    avançar = Button(top, image = bt_start_1, compound = CENTER, bd = 0, bg = palet[0]['bg'], activebackground = palet[0]['bg'], command = nxt)
    avançar.pack(anchor = CENTER, side = BOTTOM, before = ig_wallp_lbl)

    a = welcome = Frame(welcome, bg = palet[0]['bg'], height = 80)
    a.pack(anchor = S, side = BOTTOM, before = ig_wallp_lbl)

    avançar.bind('<Enter>', com_enter)
    avançar.bind('<Leave>', com_leave)

welcome_interface()
program()
# start()

top.mainloop()
