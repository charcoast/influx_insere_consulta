import psutil
import time
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS



token = "token"
org = "org"
bucket = "Medicoes"


client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    cpu = psutil.cpu_percent()
    print(cpu)
    
    data = [f'cpu,computador=computador-1 porcentagem={cpu}']
    print(data)
    
    write_api.write(bucket, org, data)
    time.sleep(5)
