#Melvin Josue Perez Garcia 
#Jaime Arnoldo Rodriguez Meza
from tkinter import Button,Tk,messagebox
import tkinter
import smtplib
ventana = Tk()
ventana.title("Gestion de correos")
ventana.geometry('500x500')
ventana.resizable(0,0)
#se configura el boton con las cajas para que se envie
def enviarcorr():
    fromaddr = usuario.get() 
    toaddrs = receptor.get()
    msg = correo.get("1.0","end")
        
        # Datos 
    username = usuario.get()
    password = contra.get()

    if fromaddr =="" and toaddrs=="" and password =="" and msg =="":
        messagebox.showerror("Error","Llene todo los campos requeridos. Por favor")
    else:
        # Enviando el correo 
        server = smtplib.SMTP('smtp.gmail.com:587') 
        server.starttls() 
        server.login(username,password) 
        server.sendmail(fromaddr, toaddrs, msg) 
        server.quit() 

#Ventana estructura
label1= tkinter.Label ( ventana , text = "Enviar a:",bg="black",fg="white" )
label1.place (x=80,y=40,width=60,height=40)
label2= tkinter.Label ( ventana , text = "Usuario:",bg="black",fg="white" )
label2.place (x=80,y=90,width=60,height=40)
label3= tkinter.Label ( ventana , text = "Contraseña:",bg="black",fg="white" )
label3.place (x=80,y=150,width=80,height=40)
label4= tkinter.Label ( ventana , text = "Escriba el mensaje para la persona." )
label4.place (x=80,y=210,width=200,height=40)
receptor=tkinter.Entry(ventana)
receptor.place(x=250,y=40,width=200,height=40)
usuario=tkinter.Entry(ventana)
usuario.place(x=250,y=90,width=200,height=40)
contra=tkinter.Entry(ventana)
contra.place(x=250,y=150,width=200,height=40)
correo=tkinter.Text(ventana)
correo.place(x=70,y=250,width=350,height=150)

boton = Button(ventana,text="Enviar: ",command=enviarcorr,bg="black",fg="white")
boton.place(x=70,y=410,width=60,height=40)
ventana.mainloop()