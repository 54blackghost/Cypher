#importation des modules  
from tkinter import  *
from tkinter import messagebox
import base64
import os

#function permettant de faire le decryptage
def decrypt():
    password=code.get()
    
    
    #teste du mot de passe
    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        
         #logique de decryption
        message=text1.get(1.0,END)
        decode_message=message.encode("utf-8")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("utf-8")
        
        
        #formulaire  d'affichage du data  decrypter
        Label(screen2,text="DECRYPT",font="arail",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="arial",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        
        text2.insert(END, decrypt)
    #messages retour si le mode passe est incorrect    
    elif password=="":
        messagebox.showerror("decrytion", "input password")
         
    elif password!="1234":
        messagebox.showerror("decrytion", "input password")
    
   
#function d'encryption            
def encrypt():
    password=code.get()
    
    
    #teste du mot de passe
    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        #logique dencryption
        message=text1.get(1.0,END) 
        encode_message=message.encode("utf-8")
        base64_bytes =base64.b64encode(encode_message)
        base64_string = base64_bytes.decode('utf-8')
       
        
        
        
        #formulaire  d'affichage du data  ecrypter
        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="arial",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        
        text2.insert(END, base64_bytes)
        
        
    #messages retour si le mode passe est incorrect      
    elif password=="":
        messagebox.showerror("encrytion", "input password")
         
    elif password!="1234":
        messagebox.showerror("encrytion", "input password")
            
 #function d'affichage des interfaces 
def main_screen():
    global screen
    global code
    global text1

    
    screen=Tk()
    screen.geometry("375x398")
    
    
    #icon
    #image_icon=PhotoImage(file="")
    #screen.iconphoto(False,image_icon)
    
    
    screen.title("ULBApp")
    
    #function reset
    def reset():
        code.set("")
        text1.delete(1.0,END)
    
    
    #formulaire dappel du data original 
    Label(text="enter text for encryption and decryption", fg="black",font=("calibri",13)).place(x=10,y=10)
    text1=Text(font="arial",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)
    
    #formulaire dappel du mot de passe
    Label(text="enter secret key for encryption and decryption", fg="black", font=("calibri",13)).place(x=10,y=170)
    
    code=StringVar()
    Entry(textvariable=code, width=19,bd=0,font=("arial",25), show="*").place(x=10,y=200)
    
    #affichage de nos button
    Button(text="ENCRYPT", height="2",width=23,bg="#ed3833", fg="white",bd=0, command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2",width=23,bg="#00bd56", fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET", height="2",width=50,bg="#1089ff", fg="white",bd=0,command=reset).place(x=10,y=300)
    
    
    
    screen.mainloop()
    
main_screen()    