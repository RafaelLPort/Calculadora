import tkinter as tk
from tkinter import ttk

COR_FUNDO = '#232032'
COR_BOTAO = '#2d2b3a'
COR_BOTAO_OP = '#7c3aed'
COR_BOTAO_OP_CLARO = '#a78bfa'
COR_TEXTO = '#fff'
COR_TEXTO_OP = '#fff'
COR_EXP = '#a1a1aa'

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("320x500")
        self.root.configure(bg=COR_FUNDO)
        self.root.resizable(False, False)
        self.expressao = ""
        self.resultado = ""

        # Frame do display
        display_frame = tk.Frame(root, bg=COR_FUNDO)
        display_frame.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(20,0))

        # Label da expressão
        self.label_exp = tk.Label(display_frame, text="", anchor='e', bg=COR_FUNDO, fg=COR_EXP, font=("Arial", 14))
        self.label_exp.pack(fill='x', padx=10)
        # Label do resultado
        self.label_res = tk.Label(display_frame, text="0", anchor='e', bg=COR_FUNDO, fg=COR_TEXTO, font=("Arial", 28, "bold"))
        self.label_res.pack(fill='x', padx=10)

        # Botões e layout
        botoes = [
            ["CE", "C", "%", "÷"],
            ["7", "8", "9", "x"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["±", "0", ".", "="],
            ["", "", "", ""]
        ]

        for i, linha in enumerate(botoes):
            for j, texto in enumerate(linha):
                if texto == "":
                    continue
                if texto in ["÷", "x", "-", "+", "=", "%"]:
                    cor = COR_BOTAO_OP
                elif texto in ["CE", "C"]:
                    cor = COR_BOTAO_OP_CLARO
                else:
                    cor = COR_BOTAO
                self.criar_botao(texto, i+1, j, cor)

        # Configurar grid
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def criar_botao(self, texto, linha, coluna, cor):
        btn = tk.Button(self.root, text=texto, bg=cor, fg=COR_TEXTO, font=("Arial", 16, "bold"),
                        bd=0, relief='flat', activebackground=cor, activeforeground=COR_TEXTO,
                        command=lambda t=texto: self.clicar(t))
        btn.grid(row=linha, column=coluna, sticky="nsew", padx=8, pady=8, ipadx=0, ipady=18)
        btn.configure(highlightthickness=0, borderwidth=0)

    def clicar(self, tecla):
        if tecla == "C":
            self.expressao = ""
            self.resultado = ""
            self.atualizar_display()
        elif tecla == "CE":
            self.expressao = self.expressao[:-1]
            self.atualizar_display()
        elif tecla == "=":
            if not self.expressao:
                return  # Não faz nada se a expressão estiver vazia
            try:
                expressao_eval = self.expressao.replace('÷', '/').replace('x', '*').replace('-', '-')
                self.resultado = str(eval(expressao_eval))
            except:
                self.resultado = "Erro"
            self.atualizar_display()
        elif tecla == "%":
            try:
                expressao_eval = self.expressao.replace('÷', '/').replace('x', '*').replace('-', '-')
                self.resultado = str(eval(expressao_eval)/100)
            except:
                self.resultado = "Erro"
            self.atualizar_display()
        elif tecla == "±":
            if self.expressao and self.expressao[0] == "-":
                self.expressao = self.expressao[1:]
            else:
                self.expressao = "-" + self.expressao
            self.atualizar_display()
        else:
            self.expressao += tecla
            self.atualizar_display()

    def atualizar_display(self):
        self.label_exp.config(text=self.expressao)
        self.label_res.config(text=self.resultado if self.resultado else (self.expressao if self.expressao else "0"))

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
