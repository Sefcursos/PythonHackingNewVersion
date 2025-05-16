## SCRIPT DE USO EDUCATIVO ##
# DESARROLLO DE UN ESCÁNER DE PUERTOS CON INTERFAZ GRÁFICA Y ESCANEO MULTIHILO PARA CURSO DE HACKING ÉTICO. TODA ESTA INFORMACIÓN ES DE MANERA EDUCATIVA.

import socket # Permite crear conexiones de red y escanear puertos.
import platform # Detecta el sistema operativo (Windows, Linux...).
import subprocess # Ejecuta comandos del sistema para obtener la IP local.
import time # Usado para pausas y barra de progreso
import threading # Permite hacer el escaneo en varios hilos simultáneamente (más rápido
import tkinter as tk # Para crear interfaz gráfica
from tkinter import ttk, messagebox # Para crear interfaz gráfica
import queue # Para comunicación segura entre hilos (usamos una cola de resultados)
import re # Expresiones regulares para validar la IP.
import locale # Para obtener IP local según el sistema operativo.

from PythonUtils.Ej2_VerificadorDeFuerzaDeContraseña import resultado

# Diccionario con puertos comunes asociados a vulnerabilidades o malas prácticas de seguridad
puertos_vulnerables = {
    21: "FTP (sin cifrado, susceptible a sniffing y brute force)",
    23: "Telnet (inseguro, sin cifrado)",
    25: "SMTP (posible open relay)",
    110: "POP3 (sin cifrado)",
    139: "NetBIOS (puede exponer archivos en red)",
    143: "IMAP (sin cifrado)",
    445: "SMB (explotable por EternalBlue)",
    3306: "MySQL (brute force, acceso remoto)",
    3389: "RDP (ataques RCE, brute force)",
    5900: "VNC (sin autenticación en muchos casos)",
    8080: "HTTP Alternativo (admin panels expuestos)"
}
# Función que detecta la IP local del equipo para escanearla.
def obtener_ip_local():
    sistema = platform.system() # Detecta si estás en windows, linux, etc.
    if sistema == "Windows":
        resultado = subprocess.check_output("ipconfig", encoding='850')
        for linea in resultado.splitlines():
            if "IPv4" in linea:
                return  linea.split(":")[-1].strip()
    else:
        resultado = subprocess.check_output("hostname -I", shell=True)
        return resultado.decode().split()[0]

def validar_ip(ip):
    patron = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if patron.match(ip):
        partes = ip.split(".")
        return all(0 <= int(parte) <= 255 for parte in partes)
    return False

class EscanerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Escáner de Puertos GUI Multihilo")
        self.root.geometry("600x450")
        self.queue_resultados = queue.Queue()
        self.crear_interfaz()

    def crear_interfaz(self):
        # IP
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=10)

        tk.Label(frame_top, text="IP a escanear:").grid(row=0, column=0)
        self.entry_ip = tk.Entry(frame_top, width=20)
        self.entry_ip.grid(row=0, column=1,  padx=5)

        tk.Button(frame_top, text="Usar IP local", command=self.usar_ip_local).grid(row=0, column=2, padx=5)

        # Rango de puertos
        frame_rango = tk.Frame(self.root)
        frame_rango.pack(pady=10)

        tk.Label(frame_rango, text="Puerto inicio: ").grid(row=0, column=0)
        self.entry_inicio = tk.Entry(frame_rango, width=6)
        self.entry_inicio.insert(0, "1")
        self.entry_inicio.grid(row=0, column=1, padx=5)

        tk.Label(frame_rango, text="Puerto fin:").grid(row=0, column=2)
        self.entry_fin = tk.Entry(frame_rango, width=6)
        self.entry_fin.insert(0, "1024")
        self.entry_fin.grid(row=0, column=3, padx=5)

        # Botón escanear
        self.boton_escanear = tk.Button(self.root, text="Iniciar escaneo", command=self.iniciar_escaneo)
        self.boton_escanear.pack(pady=10)

        # Barra de progreso
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=10)

        # Resultados
        self.texto_resultado = tk.Text(self.root, height=15)
        self.texto_resultado.pack(pady=10, padx=10)

        def usar_ip_local(self):
            ip = obtener_ip_local()
            self.entry_ip.delete(0, tk.END)
            self.entry_ip.insert(0, ip)

        def iniciar_escaneo(self):
            ip = self.entry_ip.get().strip()
            if not validar_ip(ip):
                messagebox.showerror("Error", "IP inválida")
                return

            try:
                puerto_inicio = int(self.entry_inicio.get())
                puerto_fin = int(self.entry_fin.get())
                if not (0 < puerto_inicio <= puerto_fin <= 65535):
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Rango de puertos inválido.")
                return

            self.texto_resultado.delete("1.0", tk.END)
            self.progress["maximum"] = puerto_fin - puerto_inicio + 1
            self.progress["value"] = 0

            threading.Thread(target=self.escanear_puertos, args=(ip, puerto_inicio, puerto_fin), daemon=True).start()
            self.root.after(100, self.actualizar_resultados)


# Función imprime una barra de progreso tipo [####------] 40%
# def mostrar_barra(progreso, total, largo=30):
#     porcentaje = progreso / total
#     completado = int(porcentaje * largo)
#     barra = "#" * completado + "-" * (largo - completado)
#     print(f"\r[ {barra} ] {porcentaje *100:.1f}% ", end="")

# Función encargada de ejecutar el escaneo de puertos
    def escanear_puertos(self, ip, inicio, fin):
        threads = []
        for puerto in range(inicio, fin +1):
            t = threading.Thread(target=self.escanear_puerto, args=(ip, puerto))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        self.queue_resultados.puit(None) # Señal de fin


    def escanear_puertos(self, ip, puerto):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # socket.socket(): te crea un nuevo objeto de socket, socke.AF_INET: Indica que se esta utilizando la familia de direcciones IPv4 (192.168.0.1), socket.SOCK_STREAM: Esto especifica que el socket sera de tipo STREAMM,osea que utilizara el protocolo tCP (Transmission Control Protocol), el cual proporciona una conexión confiable.
                 sock.settimeout(0.3)
                 resultado = sock.connect_ex((ip, puerto))
                 if resultado == 0:
                    vulnerabilidad = puertos_vulnerables.get(puerto, "")
                    mensaje = f"Puerto {puerto} abierto"
                    if vulnerabilidad:
                        mensaje += f" --> VULNERABILIDAD: {vulnerabilidad}"
                    self.queue_resultados.put(mensaje)

        except:
            pass
        self.queue_resultados.put("PROGRESO")

    def actualizar_resultado(self):
        while not self.queue_resultados.empty():
            resultado = self.queue_resultados.get()
            if resultado == "PROGRESO":
                self.progress["value"] += 1
            elif resultado is None:
                self.texto_resultado.insert(tk.END, "\n--- Escaneo completado ----\n")
                return
            else:
                self.texto_resultado.insert(tk.END, resultado + "\n")

        self.root.after(100, self.actualizar_resultado)


# Ejecutar escaneo (Lamamos a la función). Lanzar Aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = EscanerGUI(root)
    root.mainloop()




