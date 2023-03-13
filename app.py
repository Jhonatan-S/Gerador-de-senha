import string as st
import random
from tkinter import *
from tkinter import messagebox

# TELA INICIAL

janela_1 = Tk()
janela_1.title('Gerador de senha')
janela_1.geometry('500x400+550+220')
janela_1.resizable(False, False)

# VARIÁVES 

letras = st.ascii_letters
numeros = st.digits
simbolos = st.punctuation
var_concatenadas = letras + numeros + simbolos
pic = PhotoImage(file= 'img/cadeadoimg.png')

# DIVIDINDO A TELA EM DUAS PARTES 

Frame_1 = Frame(janela_1, width= 500, height= 50) # IDENTIFICAÇÃO DE QUEM CRIOU O PROGRAMA
Frame_2 = Frame(janela_1, width= 500, height= 450) # TODA FUNCIONALIDADE DO PROGRAMA
Frame_1.grid(row= 0, column= 0)
Frame_2.grid(row= 1, column= 0)

# CRIAR LABELS

criado_por = Label(Frame_1, text= 'CREATED by Jhonatan', font= 'Times 18 bold', bg= 'black', fg= 'white', width= 35, height= 2)
foto_1 = Label(Frame_2, image= pic, height= 450, width= 500)
passo_1 = Label(Frame_2, text= 'Digite o tamanho da senha. Ex: 10', font= 'Arial 12', fg= 'red')
criado_por.pack()
passo_1.pack()
foto_1.pack()

# DEFININDO FUNÇÃO

def gerar_senha():

    tamanho = entrada_2.get()
    tamanho = int(tamanho)

    if tamanho < 8:
        messagebox.showerror('Sua senha deve ter 8 ou mais dígitos                 ') 

        
    else:
        senha = ''.join(random.sample(var_concatenadas, tamanho))
        entrada_1.delete(0, END)
        entrada_1.insert(0, senha)

        
# CRIANDO DISPLAY


entrada_1 = Entry(Frame_2, relief= RIDGE, bd= 5, justify= RIGHT, font= '5')
entrada_2 = Entry(Frame_2, relief= RIDGE, bd= 5, justify= RIGHT, font= '2')
entrada_1.place(x= 60, y= 200, width= 350, height= 35)
entrada_2.place(x= 365, y= 150, width= 45)
entrada_2.focus()
# CRIANDO BOTÃO

btn_gerar = Button(Frame_2, text= 'Gerar senha', width= 12, height= 2, font= 'Arial 12 bold', relief= RAISED, bd= 5, command= gerar_senha)
btn_gerar.place(x= 170, y= 250)


janela_1.mainloop()