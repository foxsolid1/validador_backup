import os
import unicodedata
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

def normalizar_ruta(ruta):
    return unicodedata.normalize('NFC', ruta.replace('\\', '/').lower())

def listar_archivos_directorio(directorio):
    lista_archivos = []
    total_peso = 0
    carpetas = set()

    for carpeta_raiz, _, archivos in os.walk(directorio):
        carpetas.add(normalizar_ruta(os.path.relpath(carpeta_raiz, directorio)))
        for nombre_archivo in archivos:
            if (nombre_archivo.startswith('~$') or nombre_archivo.startswith('.~') or
                nombre_archivo.lower().endswith('.ini') or nombre_archivo.lower().endswith('.tmp')):
                continue
            ruta_completa = os.path.join(carpeta_raiz, nombre_archivo)
            ruta_relativa = os.path.relpath(ruta_completa, directorio)
            ruta_normalizada = normalizar_ruta(ruta_relativa)
            lista_archivos.append(ruta_normalizada)
            total_peso += os.path.getsize(ruta_completa)

    return set(lista_archivos), len(carpetas), total_peso

def bytes_a_megabytes(bytes):
    return round(bytes / (1024 * 1024), 2)

def comparar_y_generar_reporte(original, respaldo):
    archivos_original, carpetas_original, peso_original = listar_archivos_directorio(original)
    archivos_respaldo, carpetas_respaldo, peso_respaldo = listar_archivos_directorio(respaldo)
    faltantes = archivos_original - archivos_respaldo

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_reporte = f"reporte_backup_{timestamp}.txt"

    with open(nombre_reporte, "w", encoding="utf-8") as reporte:
        reporte.write("Resumen de comparación de respaldo\n")
        reporte.write("="*40 + "\n")
        reporte.write(f"Ruta carpeta origen: {original}\n")
        reporte.write(f"Ruta carpeta respaldo: {respaldo}\n")
        reporte.write(f"Carpetas en origen: {carpetas_original}\n")
        reporte.write(f"Carpetas en respaldo: {carpetas_respaldo}\n")
        reporte.write(f"Peso total en origen: {bytes_a_megabytes(peso_original)} MB\n")
        reporte.write(f"Peso total en respaldo: {bytes_a_megabytes(peso_respaldo)} MB\n\n")

        if faltantes:
            reporte.write("Archivos/carpetas faltantes en el respaldo:\n\n")
            for item in sorted(faltantes):
                reporte.write(f"- {item}\n")
        else:
            reporte.write("Todos los archivos están respaldados correctamente.\n")

    return nombre_reporte, faltantes

class BackupValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Backups")

        self.label_original = tk.Label(root, text="Carpeta Original:")
        self.label_original.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.entry_original = tk.Entry(root, width=60)
        self.entry_original.grid(row=0, column=1, padx=5, pady=5)

        self.btn_explorar_original = tk.Button(root, text="Examinar", command=self.seleccionar_original)
        self.btn_explorar_original.grid(row=0, column=2, padx=5, pady=5)

        self.label_respaldo = tk.Label(root, text="Carpeta de Respaldo:")
        self.label_respaldo.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.entry_respaldo = tk.Entry(root, width=60)
        self.entry_respaldo.grid(row=1, column=1, padx=5, pady=5)

        self.btn_explorar_respaldo = tk.Button(root, text="Examinar", command=self.seleccionar_respaldo)
        self.btn_explorar_respaldo.grid(row=1, column=2, padx=5, pady=5)

        self.btn_validar = tk.Button(root, text="Validar Backup", command=self.validar_backup)
        self.btn_validar.grid(row=2, column=1, pady=10)

    def seleccionar_original(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.entry_original.delete(0, tk.END)
            self.entry_original.insert(0, carpeta)

    def seleccionar_respaldo(self):
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.entry_respaldo.delete(0, tk.END)
            self.entry_respaldo.insert(0, carpeta)

    def validar_backup(self):
        carpeta_original = self.entry_original.get()
        carpeta_respaldo = self.entry_respaldo.get()

        if not carpeta_original or not carpeta_respaldo:
            messagebox.showerror("Error", "Selecciona ambas carpetas antes de validar.")
            return

        reporte, faltantes = comparar_y_generar_reporte(carpeta_original, carpeta_respaldo)

        if faltantes:
            messagebox.showwarning("Backup Incompleto", f"Faltan archivos. Revisa el reporte: {reporte}")
        else:
            messagebox.showinfo("Backup Correcto", "Todos los archivos están correctamente respaldados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackupValidatorApp(root)
    root.mainloop()
