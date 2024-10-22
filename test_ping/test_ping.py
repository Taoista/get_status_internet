import speedtest
from datetime import datetime

class TestPing:
    def __init__(self):
        # Crear un objeto Speedtest
        st = speedtest.Speedtest()

        # Obtener los servidores cercanos
        st.get_best_server()

        # Medir la velocidad de descarga
        self.download_speed = st.download() / 1_000_000  # Convertir a Mbps

        # Medir la velocidad de subida
        self.upload_speed = st.upload() / 1_000_000  # Convertir a Mbps

        # Medir el ping
        self.ping = st.results.ping

        # Obtener la IP pública
        self.ip_publica = st.results.client['ip']

        # Obtener la fecha y hora actual
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Mostrar los resultados

    def get_fecha(self):
        return str(self.fecha_hora)

    def get_download_speed(self):
        return str(self.download_speed)

    def get_upload_speed(self):
        return str(self.upload_speed)

    def get_ping(self):
        return str(self.ping)

    def get_ip_public(self):
        return str(self.ip_publica)

   