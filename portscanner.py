import hashlib
import socket as port
import threading
import time as t
import tkinter as tk
from tkinter import messagebox

portas_principais = [21, 22, 23, 25, 53, 80, 443, 1433, 3306, 3389, 5432]

janela = tk.Tk()
janela.configure(bg="black")
janela.title("Port Scanner Reconnaissance")
janela.geometry("550x550")

titulo = tk.Label(janela, text="RECONNAISSANCE PORT SCANNER", font=("OpenSans", 18, "bold"), fg="green", bg="black")
titulo.pack(pady=15)

frame_input = tk.Frame(janela, bg="black")
frame_input.pack(pady=10)

label_alvo = tk.Label(frame_input, text="Alvo (IP/Hostname):", font=("OpenSans", 12), fg="yellow", bg="black")
label_alvo.pack(side=tk.LEFT, padx=5)

campo_alvo = tk.Entry(frame_input, font=("OpenSans", 12), fg="white", bg="#222222", width=25)
campo_alvo.insert(0, "scanme.nmap.org")  
campo_alvo.pack(side=tk.LEFT, padx=5)

campo_resultado = tk.Text(janela, font=("Consolas", 11), fg="#00FF00", bg="#151515", width=60, height=18)
campo_resultado.pack(pady=10, padx=20)

def executarvarredura(alvo):
    try:
        port.gethostbyname(alvo)
    except port.gaierror:
        campo_resultado.delete("1.0", tk.END)
        campo_resultado.insert(tk.END, " ERRO: O endereço IP ou Hostname digitado não pôde ser encontrado.\n")
        campo_resultado.insert(tk.END, "Por favor, verifique a grafia e tente novamente.\n")
        botaoiniciar.config(state="normal", text="Iniciar Scan")
        return 
    campo_resultado.delete("1.0", tk.END)
    campo_resultado.insert(tk.END, f"Varredura iniciada em {alvo}...\n" + "-" * 50 + "\n")
    campo_resultado.see(tk.END)

    for p in portas_principais:
        t.sleep(0.5)
        client = port.socket(port.AF_INET, port.SOCK_STREAM)
        client.settimeout(1)
        resultado = client.connect_ex((alvo, p))
        client.close()
        
        if resultado == 0:
            t.sleep(0.5)
            campo_resultado.insert(tk.END, f" Porta {p} está aberta.\n")
            try:
                banner_client = port.socket(port.AF_INET, port.SOCK_STREAM)
                banner_client.settimeout(1)
                banner_client.connect((alvo, p))
                banner = banner_client.recv(1024).decode().strip()
                
                if banner:
                    t.sleep(0.5)
                    campo_resultado.insert(tk.END, f" Banner da porta {p}: {banner}\n")
                banner_client.close()   
            except:
                pass
        else:
            t.sleep(0.5)
            campo_resultado.insert(tk.END, f" Porta {p}: Fechada\n")
        campo_resultado.see(tk.END)

    campo_resultado.insert(tk.END, "-"*50 + "\n Varredura concluída!\n")
    botaoiniciar.config(state="normal", text="Iniciar Scan")

def iniciar_varredura():
    alvo_digitado = campo_alvo.get().strip()
    
    if alvo_digitado != "":
        botaoiniciar.config(state="disabled", text="Varredura em andamento...")
        threading.Thread(target=executarvarredura, args=(alvo_digitado,), daemon=True).start()
    else:
        campo_resultado.delete("1.0", tk.END)
        campo_resultado.insert(tk.END, " Campo vazio. Por favor, insira um endereço IP ou hostname válido.\n")
botaoiniciar = tk.Button(janela, text="Iniciar Scan", font=("OpenSans", 12, "bold"), command=iniciar_varredura, fg="gray", bg="#111111", activebackground="#222222")
botaoiniciar.pack(pady=15)

janela.mainloop()