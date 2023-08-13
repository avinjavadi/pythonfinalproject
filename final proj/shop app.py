import tkinter
import sqlite3
from user_actions import *
from product_actions import *

def login():
    global session
    global login_cnt
    user=txt_user.get()
    pas=txt_pass.get()
    result=user_login(user,pas)
    if result:
        lbl_msg.configure(text="welcome to your account !",fg="green")
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        btn_login.configure(state="disabled")
        btn_logout.configure(state="active")
        login_cnt=3
        session=result

        access=access_check(session)
        if not access:
            btn_submit.configure(state="disabled")
            btn_shop.configure(state="disabled")
            btn_admin_panel.configure(state="disabled")

        elif int(access[1])==1 :
            btn_shop.configure(state="disabled")
            btn_admin_panel.configure(state="disabled")

        elif int(access[1])==2 :
            btn_shop.configure(state="active")
            btn_admin_panel.configure(state="disabled")

        elif int(access[1])==3 :
            btn_shop.configure(state="active")
            btn_admin_panel.configure(state="active")

    else:
        lbl_msg.configure(text="wrong username or password !!!",fg="red")
        login_cnt-=1
        if login_cnt == 0 :
            btn_login.configure(state="disabled")
            lbl_msg.configure(text="3 times error occurred !! login disabled !!",fg="red")

def submit():
    user=txt_user.get()
    pas=txt_pass.get()
    result,errormsg=validation(user,pas)
    if not result:
        lbl_msg.configure(text=errormsg,fg="red")
    else:
        user_submit(user,pas)
        lbl_msg.configure(text="submit done!",fg="green")
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")

def logout():
    btn_login.configure(state="active")
    btn_logout.configure(state="disabled")
    lbl_msg.configure(text="you are logged out now",fg="blue")
    btn_shop.configure(state="disabled")
    btn_admin_panel.configure(state="disabled")

def shop():

    def buy():
        pid=pidtxt.get()
        qnt=pqnttxt.get()

        if pid=="" or qnt=="" :
            lbl_msg2.configure(text="fill the inputs",fg="red")
            return
        
        if not pid.isdigit() or not qnt.isdigit():
            lbl_msg2.configure(text="you must enter a number in inputs !!!",fg="red")
            return
        
        result=get_single_product(pid)
        if not result:
            lbl_msg2.configure(text="wrong product id",fg="red")
            return
        
        if int(qnt) > result[3]:
            lbl_msg2.configure(text="not enough products",fg="red")
            return
        
        if int(qnt) <= 0:
            lbl_msg2.configure(text="quantity should be at least 1",fg="red")
            return
        
        save_to_cart(pid,session,qnt)
        lbl_msg2.configure(text="add to cart successfully",fg="green")
        pidtxt.delete(0,"end")
        pqnttxt.delete(0,"end")

        update_quantity_of_products(qnt,pid)
        lst.delete(0,"end")
        products=get_product()
        for product in products:
            text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
            lst.insert("end",text)

    win_shop=tkinter.Toplevel(win)
    win_shop.geometry("400x400")
    win_shop.title("shopping panel")

    lst=tkinter.Listbox(win_shop,width=50)
    lst.pack()

    products=get_product()
    for product in products:
        text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
        lst.insert("end",text)

    pidlbl=tkinter.Label(win_shop,text="ID: ")
    pidlbl.pack()
    pidtxt=tkinter.Entry(win_shop)
    pidtxt.pack()
    
    pqntlbl=tkinter.Label(win_shop,text="QUANTITY: ")
    pqntlbl.pack()
    pqnttxt=tkinter.Entry(win_shop)
    pqnttxt.pack()
    
    lbl_msg2=tkinter.Label(win_shop,text="")
    lbl_msg2.pack()

    btn_buy=tkinter.Button(win_shop,text="buy",command=buy)
    btn_buy.pack()

    win_shop.mainloop()

def admin_panel():

    def update_quantity():
        def increase():
            pid=pidtxt.get()
            qnt=pqnt1txt.get()

            if pid=="" or qnt=="" :
                lbl_msg.configure(text="fill the inputs",fg="red")
                return
            if not pid.isdigit() or not qnt.isdigit():
                lbl_msg.configure(text="you must enter a number in inputs !!!",fg="red")
                return
            result=get_single_product(pid)
            if not result:
                lbl_msg.configure(text="wrong product id",fg="red")
                return
            
            result=get_single_product(pid)
            lst=list(result)
            x=lst[3] + int(qnt)

            sql=''' UPDATE products SET qnt=? WHERE id=? '''
            cnt.execute(sql,(x,pid))
            cnt.commit()

            lst1.delete(0,"end")
            products=get_product()
            for product in products:
                text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
                lst1.insert("end",text)
            
            lbl_msg.configure(text="increase done",fg="green")
            pidtxt.delete(0,"end")
            pqnt1txt.delete(0,"end")

        def decrease():
            pid=pidtxt.get()
            qnt=pqnt1txt.get()

            if pid=="" or qnt=="" :
                lbl_msg.configure(text="fill the inputs",fg="red")
                return
            if not pid.isdigit() or not qnt.isdigit():
                lbl_msg.configure(text="you must enter a number in inputs !!!",fg="red")
                return
            
            result=get_single_product(pid)
            if not result:
                lbl_msg.configure(text="wrong product id",fg="red")
                return
            result=get_single_product(pid)
            lst=list(result)
            x=lst[3] - int(qnt)

            sql=''' UPDATE products SET qnt=? WHERE id=? '''
            cnt.execute(sql,(x,pid))
            cnt.commit()

            lst1.delete(0,"end")
            products=get_product()
            for product in products:
                text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
                lst1.insert("end",text)

            lbl_msg.configure(text="decrease done",fg="green")
            pidtxt.delete(0,"end")
            pqnt1txt.delete(0,"end")

        win_update=tkinter.Toplevel(win_admin)
        win_update.geometry("500x500")
        win_update.title("update quantity panel")

        lst1=tkinter.Listbox(win_update,width=50)
        lst1.pack()

        products=get_product()
        for product in products:
            text=f"ID={product[0]} , NAME={product[1]} , PRICE={product[2]} , QUANTITY={product[3]}"
            lst1.insert("end",text)

        pidlbl=tkinter.Label(win_update,text="product id: ")
        pidlbl.pack()
        pidtxt=tkinter.Entry(win_update)
        pidtxt.pack()

        pqnt1lbl=tkinter.Label(win_update,text="product quantity: ")
        pqnt1lbl.pack()
        pqnt1txt=tkinter.Entry(win_update)
        pqnt1txt.pack()

        btn_in=tkinter.Button(win_update,text="increase",command=increase)
        btn_in.pack()

        btn_de=tkinter.Button(win_update,text="decrease",command=decrease)
        btn_de.pack()

        lbl_msg=tkinter.Label(win_update,text="")
        lbl_msg.pack()

    def update_products():
        pname=pntxt.get()
        price=pprtxt.get()
        qnt=pqnt1txt.get()

        if pname=="" or price=="" or qnt=="" :
            lbl_msg2.configure(text="fill the inputs",fg="red")
            return
        
        if not pname.isalnum():
            lbl_msg2.configure(text="the product name must be a combination of letters and numbers !!!",fg="red")
            return
        
        products=get_product()
        for product in products:
            if product[1] == pname :
                lbl_msg2.configure(text="product already exist !!!",fg="red")
                return
        
        if not price.isdigit() or not qnt.isdigit():
            lbl_msg2.configure(text="you must enter a number in price and quantity inputs !!!",fg="red")
            return
        
        if int(price)<=0 or int(qnt)<=0 :
            lbl_msg2.configure(text="the price and quantity of the product cannot be 0 or less",fg="red")
            return
        
        insert_product(pname,price,qnt)
        lbl_msg2.configure(text="product successfully added",fg="green")
        pntxt.delete(0,"end")
        pprtxt.delete(0,"end")
        pqnt1txt.delete(0,"end")

    def users_access():

        def confirm_access():
            uid=idtxt.get()
            acc=acctxt.get()

            if uid=="" or acc=="" :
                lbl_msg2.configure(text="fill the inputs",fg="red")
                return
            
            if not uid.isdigit() or not acc.isdigit():
                lbl_msg2.configure(text="you must enter a number in inputs !!!",fg="red")
                return
            
            result=get_single_user(uid)
            if not result:
                lbl_msg2.configure(text="wrong user id",fg="red")
                return
            
            check=access_check(uid)
            if check:
                lbl_msg2.configure(text="access level has been already set for this id !!!",fg="red")
                return
            
            if not (int(acc)==1 or int(acc)==2 or int(acc)==3) :
                lbl_msg2.configure(text="access level must be between 1 and 3 !!!",fg="red")
                return
            
            user_access(uid,acc)
            lbl_msg2.configure(text="access level registered successfully",fg="green")
            idtxt.delete(0,"end")
            acctxt.delete(0,"end")


        win_access=tkinter.Toplevel(win_admin)
        win_access.geometry("500x500")
        win_access.title("users access panel")

        lbl_msg=tkinter.Label(win_access,text="determine the access level of users",fg="blue")
        lbl_msg.pack()

        lst_user=tkinter.Listbox(win_access,width=50,height=9)
        lst_user.pack()
        users=get_user()
        for user in users:
            text=f"ID={user[0]}  ,  NAME={user[1]}  ,  SCORE={user[4]}"
            lst_user.insert("end",text)

        lst_access=tkinter.Listbox(win_access,width=50,height=3)
        lst_access.pack()
        level_lst=["level 1 : The login, submit and logout buttons are active",
                    "level 2 : The login, submit, logout and shop buttons are active",
                    "level 3 : All buttons are active [admin level]"]
        for level in level_lst:
            lst_access.insert("end",level)

        idlbl=tkinter.Label(win_access,text="user id: ")
        idlbl.pack()
        idtxt=tkinter.Entry(win_access)
        idtxt.pack()

        acclbl=tkinter.Label(win_access,text="user access: ")
        acclbl.pack()
        acctxt=tkinter.Entry(win_access)
        acctxt.pack()

        lbl_msg2=tkinter.Label(win_access,text="")
        lbl_msg2.pack()

        btn_confirm=tkinter.Button(win_access,text="confirm access",command=confirm_access)
        btn_confirm.pack()

    win_admin=tkinter.Toplevel(win)
    win_admin.geometry("500x300")
    win_admin.title("admin panel")

    lbl_msg=tkinter.Label(win_admin,text="what product do you want to register ?",fg="blue")
    lbl_msg.pack()

    pnlbl=tkinter.Label(win_admin,text="product name: ")
    pnlbl.pack()
    pntxt=tkinter.Entry(win_admin)
    pntxt.pack()
    
    pprlbl=tkinter.Label(win_admin,text="product price: ")
    pprlbl.pack()
    pprtxt=tkinter.Entry(win_admin)
    pprtxt.pack()

    pqnt1lbl=tkinter.Label(win_admin,text="product quantity: ")
    pqnt1lbl.pack()
    pqnt1txt=tkinter.Entry(win_admin)
    pqnt1txt.pack()

    lbl_msg2=tkinter.Label(win_admin,text="")
    lbl_msg2.pack()

    btn_buy=tkinter.Button(win_admin,text="add product",command=update_products)
    btn_buy.pack()

    btn_access=tkinter.Button(win_admin,text="users access",command=users_access)
    btn_access.pack()

    btn_qnt=tkinter.Button(win_admin,text="update quantity",command=update_quantity)
    btn_qnt.pack()

    win_admin.mainloop()

#------------------------------------------------------------------------------------------

session=""
login_cnt=3

win=tkinter.Tk()
win.geometry("350x350")

lbl_user=tkinter.Label(win,text="username : ")
lbl_user.pack()
txt_user=tkinter.Entry(win)
txt_user.pack()

lbl_pass=tkinter.Label(win,text="password : ")
lbl_pass.pack()
txt_pass=tkinter.Entry(win)
txt_pass.pack()

lbl_msg=tkinter.Label(win,text="")
lbl_msg.pack()

btn_login=tkinter.Button(win,text="login",command=login)
btn_login.pack()

btn_submit=tkinter.Button(win,text="submit",command=submit)
btn_submit.pack()

btn_logout=tkinter.Button(win,text="logout",state="disabled",command=logout)
btn_logout.pack()

btn_shop=tkinter.Button(win,text="shop",state="disabled",command=shop)
btn_shop.pack()

btn_admin_panel=tkinter.Button(win,text="admin panel",state="disabled",command=admin_panel)
btn_admin_panel.pack()

win.mainloop()