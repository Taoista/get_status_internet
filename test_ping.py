import speedtest
from datetime import datetime

# Crear un objeto Speedtest
st = speedtest.Speedtest()

# Obtener los servidores cercanos
st.get_best_server()

# Medir la velocidad de descarga
download_speed = st.download() / 1_000_000  # Convertir a Mbps

# Medir la velocidad de subida
upload_speed = st.upload() / 1_000_000  # Convertir a Mbps

# Medir el ping
ping = st.results.ping

# Obtener la IP pública
ip_publica = st.results.client['ip']

# Obtener la fecha y hora actual
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mostrar los resultados
print(f"Fecha y hora de la prueba: {fecha_hora}")
print(f"Velocidad de descarga: {download_speed:.2f} Mbps")
print(f"Velocidad de subida: {upload_speed:.2f} Mbps")
print(f"Ping: {ping} ms")
print(f"IP pública: {ip_publica}")
