import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Hello World")

# Configurar o tamanho da janela
janela.geometry("300x200")

# Criar um rótulo com a mensagem
mensagem = tk.Label(janela, text="Hello World!!!", font=("Arial", 24))
mensagem.pack(expand=True)

# Iniciar o loop principal da janela
janela.mainloop()
