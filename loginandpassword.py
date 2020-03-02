import tkinter as tk
import tkinter.messagebox as mb
import pymysql

window = tk.Tk()
window.geometry('500x500')
window.title('Login&Password')

back_button = tk.Button()
ok_button = tk.Button()

def main():
    login_button = tk.Button(text='Login', command=lambda : start_login())
    register_button = tk.Button(text='Register', command=lambda : start_register())

    login_button.pack()
    register_button.pack()

    def start_login():
        login_button.pack_forget()
        register_button.pack_forget()

        login()

    def start_register():
        login_button.pack_forget()
        register_button.pack_forget()

        register()


def register():
    login_label = tk.Label(text='Login')
    login_entry = tk.Entry()

    password_label = tk.Label(text='Password')
    password_entry = tk.Entry(show='#')

    email_label = tk.Label(text='Email')
    email_entry = tk.Entry()

    ok_button = tk.Button(text='OK', command=lambda: sing_up())

    back_button = tk.Button(text='Back', command=lambda: back())

    login_label.pack()
    login_entry.pack()

    password_label.pack()
    password_entry.pack()

    email_label.pack()
    email_entry.pack()

    ok_button.pack()

    back_button.place(x = 0, y = 0)

    def back():
        back_button.destroy()

        login_label.pack_forget()
        login_entry.pack_forget()

        password_label.pack_forget()
        password_entry.pack_forget()

        email_label.pack_forget()
        email_entry.pack_forget()

        ok_button.pack_forget()

        main()

    def sing_up():
        #INSERT INTO users (login, password, email ) VALUES('testname', 'testpassword', 'test@email.com');
        conn = pymysql.connect('localhost', 'root', 'realPassword', 'test')

        in_database = False

        try:
            cur = conn.cursor()
            cur.execute('SELECT login FROM users;')

            rows = cur.fetchall()

            lenrows = int(len(rows) / 2)

            print(rows)

            for i in range(32):
                if rows[lenrows][0] == login_entry.get():
                    in_database = True
                    break

                lenrows = int(lenrows / 2)

        except:
            if in_database == False:
                mb.showerror(title='Database', message='it\'s login has already')
            
            print('(0_0)')

        if not login_entry.get() == '' or password_entry.get() == '' or email_entry.get() == '':
            with conn:
                cur = conn.cursor()
                cur.execute(f'INSERT INTO users (login, password, email ) VALUES("{login_entry.get()}", "{password_entry.get()}", "{email_entry.get()}");')

                mb.showinfo(title='Register', message='You Registered')

                back()
        
        else:
            mb.showerror(title='Enter', message='You not enter all data')


def login():
    login_label = tk.Label(text='Login')
    login_entry = tk.Entry()

    password_label = tk.Label(text='Password')
    password_entry = tk.Entry(show='#')

    ok_button = tk.Button(text='OK', command=lambda: sing_in())

    back_button = tk.Button(text='Back', command=lambda: back())

    login_label.pack()
    login_entry.pack()

    password_label.pack()
    password_entry.pack()

    ok_button.pack()
    
    back_button.place(x = 0, y = 0)

    def back():
        back_button.destroy()

        login_label.pack_forget()
        login_entry.pack_forget()

        password_label.pack_forget()
        password_entry.pack_forget()

        ok_button.pack_forget()

        main()
        

    def sing_in():
        conn = pymysql.connect('localhost', 'root', 'realPassword', 'test')

        with conn:
            cur = conn.cursor()
            cur.execute('SELECT login, password FROM users;')

            rows = cur.fetchall()

            lenrows = int(len(rows) / 2)

            print(rows)

            # hashpassword = hash(password_entry.get())

            # print(hashpassword)

            for i in range(len(rows)):
                if rows[i][0] == login_entry.get() and rows[i][1] == password_entry.get():
                    print(f'Database version: \n Login {rows[i][0]}, {login_entry.get()} \n Password {rows[i][1]}, {password_entry.get()}, {i}')

                    mb.showinfo(title='Login', message='You enter')
                    break

                # lenrows = int(lenrows / 2)


if __name__ == '__main__':
    main()
    window.mainloop()
