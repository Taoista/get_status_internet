import openpyxl
import os
from openpyxl import Workbook

from export_excel.export_excel import *
from test_ping.test_ping import *


def main():
    speed_test = TestPing()
    fecha = speed_test.get_fecha()
    download = speed_test.get_download_speed()
    upload = speed_test.get_upload_speed()
    ping = speed_test.get_ping()
    ip_public = speed_test.get_ip_public()

    data = [fecha, download, upload, ping, ip_public]

    export_excel = ExportExcel(fecha, ip_public, upload, download, ping)

    export_excel.insertar_datos()
    
    print(data)



if __name__ == "__main__":
    main()