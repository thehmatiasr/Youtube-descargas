from pytube import YouTube
import os

def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Descargando... {percentage:.2f}% completado", end='\r')

def descargar_video(url, ruta_guardado):
    try:
        # Crear objeto YouTube con la URL proporcionada
        video = YouTube(url, on_progress_callback=progress_callback)

        # Descargar el video en la mejor calidad disponible
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=ruta_guardado)

        print("\nDescarga completada.")
    except Exception as e:
        print("Error al descargar el video:", str(e))

# Pedir al usuario que ingrese el enlace de YouTube
url = input("Ingresa el enlace de YouTube: ")

# Pedir al usuario que ingrese la ruta de guardado o usar la ruta predeterminada
ruta_guardado = input("Ingresa la ruta de guardado o presiona Enter para usar la ruta predeterminada (/storage/emulated/0/DCIM/): ")
if not ruta_guardado:
    ruta_guardado = "/storage/emulated/0/DCIM/"

# Verificar si la ruta de guardado es válida y si existe, de lo contrario, usar la predeterminada
if not os.path.exists(ruta_guardado):
    print("La ruta de guardado no es válida o no existe. Usando la ruta predeterminada.")
    ruta_guardado = "/storage/emulated/0/DCIM/"

descargar_video(url, ruta_guardado)