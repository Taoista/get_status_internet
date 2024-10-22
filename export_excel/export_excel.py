import openpyxl
import os
from openpyxl import Workbook


class ExportExcel:
    def __init__(self, fecha, ip, subida, bajada, ping):
        # Nombre del archivo Excel
        self.nombre_archivo = "datos.xlsx"
        self.fecha = fecha
        self.ip = ip
        self.subida = subida
        self.bajada = bajada
        self.ping = ping
        # Insertar nuevos datos al ejecutar la función
        self.nuevos_datos = [self.fecha, self.ip, self.subida, self.bajada, self.ping]


    def insertar_datos(self):
        datos = self.nuevos_datos
        nombre_archivo = self.nombre_archivo
        # Verificar si el archivo existe
        if os.path.exists(nombre_archivo):
            # Cargar el archivo existente
            wb = openpyxl.load_workbook(nombre_archivo)
            ws = wb.active
        else:
            # Crear un nuevo archivo si no existe
            wb = Workbook()
            ws = wb.active
            # Agregar encabezados si el archivo es nuevo
            ws.append(["fecha", "ip" ,"subida", "bajada", "ping"])

        # Agregar los nuevos datos en la última fila
        ws.append(datos)
        # Guardar los cambios
        wb.save(nombre_archivo)
        print(f"Datos {datos} insertados en la última fila del archivo {nombre_archivo}.")
