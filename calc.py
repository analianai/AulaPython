# ==============================
# Calculadora Simples em Tkinter
# Comentada passo a passo
# ==============================

# Importa o Tkinter (interface gráfica) e as caixas de diálogo (messagebox)
import tkinter as tk
from tkinter import messagebox

# ---------- Função principal de cálculo ----------
def calcular():
    """
    Lê os valores digitados, converte para float e calcula
    soma, subtração, multiplicação e divisão (com proteção
    contra divisão por zero). Exibe tudo num messagebox.
    """
    try:
        # .get() pega o texto que o usuário digitou nas caixas de entrada
        n1 = float(entrada1.get())   # converte o primeiro número para float
        n2 = float(entrada2.get())   # converte o segundo número para float

        # Operações básicas
        soma = n1 + n2
        subtracao = n1 - n2
        multiplicacao = n1 * n2

        # Evita erro quando o segundo número é 0
        divisao = n1 / n2 if n2 != 0 else "Não existe (divisão por zero)"

        # Monta um texto bonitinho com os resultados
        resultado = (
            f"Soma: {soma}\n"
            f"Subtração: {subtracao}\n"
            f"Multiplicação: {multiplicacao}\n"
            f"Divisão: {divisao}"
        )

        # Exibe os resultados em uma janelinha
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        # Cai aqui se o usuário digitou algo que não é número (ex.: letras)
        messagebox.showerror("Erro", "Digite apenas números (use ponto como separador decimal).")

# ---------- Construção da Janela ----------
janela = tk.Tk()                     # Cria a janela principal
janela.title("Calculadora Simples")  # Define o título da janela
janela.geometry("320x220")           # Largura x Altura (em pixels)
janela.resizable(False, False)       # Impede redimensionamento (opcional)

# ---------- Widgets (componentes da interface) ----------
# Rótulo (texto explicativo) do primeiro número
lbl1 = tk.Label(janela, text="Digite o primeiro número:")
lbl1.pack(pady=(12, 2))              # Coloca na tela com espaçamento vertical (topo,baixo)

# Caixa de entrada do primeiro número
entrada1 = tk.Entry(janela, justify="center")
entrada1.pack(pady=2)
entrada1.focus_set()                 # Já deixa o cursor aqui quando abrir o app

# Rótulo do segundo número
lbl2 = tk.Label(janela, text="Digite o segundo número:")
lbl2.pack(pady=(10, 2))

# Caixa de entrada do segundo número
entrada2 = tk.Entry(janela, justify="center")
entrada2.pack(pady=2)

# Botão que, ao ser clicado, chama a função calcular()
botao = tk.Button(janela, text="Calcular", command=calcular)
botao.pack(pady=12)

# Dica rápida para o usuário (opcional)
dica = tk.Label(
    janela,
    text="Dica: use ponto para decimais (ex.: 3.5).",
    font=("Arial", 9),
    fg="#555"
)
dica.pack()

# ---------- Loop principal ----------
# Mantém a janela aberta e escuta eventos (cliques, digitação, etc.)
janela.mainloop()
