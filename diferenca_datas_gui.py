import tkinter as tk
from datetime import datetime

def calcular_diferenca():
    data1_str = entrada_data1.get()
    data2_str = entrada_data2.get()
    try:
        data1 = datetime.strptime(data1_str, "%d/%m/%Y")
        data2 = datetime.strptime(data2_str, "%d/%m/%Y")
        diferenca = abs((data2 - data1).days)
        resultado.config(text=f"A diferença é de {diferenca} dias.")
    except ValueError:
        resultado.config(text="Formato inválido! Use dd/mm/aaaa.")

# Criar a janela
janela = tk.Tk()
janela.title("Diferença entre Datas")
janela.geometry("300x200")

# Widgets
tk.Label(janela, text="Data 1 (dd/mm/aaaa):").pack(pady=5)
entrada_data1 = tk.Entry(janela)
entrada_data1.pack()

tk.Label(janela, text="Data 2 (dd/mm/aaaa):").pack(pady=5)
entrada_data2 = tk.Entry(janela)
entrada_data2.pack()

tk.Button(janela, text="Calcular", command=calcular_diferenca).pack(pady=10)

resultado = tk.Label(janela, text="")
resultado.pack()

# Executar
janela.mainloop()
