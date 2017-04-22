# *-* coding:utf-8 *-*
from Tkinter import *




def hide_me(event):
    event.widget.pack_forget()
def girisYap():

    try:
        def new_window():

            def projeler(event):



                value = str((liste.selection_get()))
                import git
                import os
                adres = "http://github.com/" + isim2+ "/"+value

                git.Git().clone(adres)

            pncr = Tk()
            pncr.geometry("600x600+200+200")
            pncr.title("")
            isim2 = Entry.get(isim)
            pencere.destroy()
            lbl = Label(pncr, text="klonlamak istediğiniz projeyi seçiniz").pack()

            liste = Listbox(pncr, width=40, height=20, font=('times', 13))
            liste.bind('<<ListboxSelect>>', projeler)
            liste.place()
            liste.pack()

            for repo in user_repos:
                baslangic = str(repo).find("(")
                bitis = str(repo).find(")")
                a = str(repo)[baslangic + 1:bitis]
                # a = str(repo)[7:len(str(user_repos))-4]  Buda çalışır hangisini tercih ederseniz artık.
                liste.insert(END, a)
            pncr.mainloop()
        # liste.place(x=80, y=180)
        from pygithub3 import Github
        username = isim.get()
        password = sifre.get()
        gh = Github(login=username, password=password)
        get_user = gh.users.get()
        Label1 = Label(pencere, text="Giriş başarılı").pack()
        user_repos = gh.repos.list().all()
        button1.bind('<Button-1>', hide_me)
        new_window()
    except :
        lbl1=Label(pencere,text="hatalı giriş yaptınız !").pack()
        lbl2=Label(pencere,text="tekrar deneyin").pack()
pencere = Tk()
pencere.tk_setPalette("#D0A9F5")
pencere.title(u"Giriş Ekrani")
pencere.geometry("500x500+100+100")

karsilama = Label(pencere)
karsilama.config(text = u"HOŞGELDİNİZ, giris yapiniz ")
karsilama.pack()

isimSor= Label(pencere)
isimSor.config(text = u"Kullanici Adi : ",fg="black" )
isimSor.pack(fill=X)
isim= Entry(pencere,bg="#FFFFFF")
isim.pack()

sifreSor= Label(pencere)
sifreSor.config(text = u"sifre : ")
sifreSor.pack()
sifre = Entry(pencere, bd = 3, show="*",bg="#FFFFFF")
sifre.pack()

button1=Button(pencere)
button1.config(text = u"Giris yap!" , command = girisYap)
button1.pack()

pencere.mainloop()
