# validador_backup
Este proyecto proporciona una herramienta en Python para comparar dos directorios (origen y respaldo), verificando que todos los archivos y carpetas hayan sido respaldados correctamente. Incluye una interfaz gráfica intuitiva usando Tkinter y genera un reporte detallado en formato de texto.
🚀 Características

Comparación Recursiva: Incluye subcarpetas y archivos.

Normalización Unicode: Evita falsos positivos por caracteres especiales.

Filtros Inteligentes: Omite archivos temporales (~$*, *.ini, *.tmp).

Reporte Detallado:

Ruta completa de origen y respaldo.

Número total de carpetas en cada directorio.

Peso total (MB) de cada carpeta.

Lista de archivos/carpetas faltantes.

Interfaz Gráfica (GUI): Uso sencillo con botones de "Examinar" y reportes emergentes.

📋 Requisitos

Python 3.8 o superior

Bibliotecas estándar: os, unicodedata, tkinter

🔧 Instalación y Uso

Clona el repositorio:



git clone https://github.com/foxsolid1/backup-validator.git
cd backup-validator

2. Ejecuta la aplicación:
   ```bash
python validador_backup.py

En la ventana:

Selecciona la carpeta Origen.

Selecciona la carpeta Respaldo.

Haz clic en Validar Backup.

Revisa el reporte generado (reporte_backup_YYYY-MM-DD_HH-MM-SS.txt).

🛠️ Ejemplo de Salida de Reporte

Resumen de comparación de respaldo
========================================
Ruta carpeta origen: C:/Datos/Proyecto/Origen
Ruta carpeta respaldo: D:/Backups/Proyecto
Carpetas en origen: 25
Carpetas en respaldo: 25
Peso total en origen: 1024.75 MB
Peso total en respaldo: 1024.12 MB

Archivos/carpetas faltantes en el respaldo:

- documentos/informe_final.pdf
- imagenes/logo_nuevo.png

  🤝 Contribuciones

¡Todas las contribuciones son bienvenidas! Por favor abre un issue o realiza un pull request.

© 2025 Gabino Trejo Andrade
