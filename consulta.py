import psutil
import time
from os import getenv
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS



token = "token"
org = "org"
bucket = "Medicoes"


client = InfluxDBClient(url="https://us-central1-1.gcp.cloud2.influxdata.com", token=token)

query = f'from(bucket: \"{bucket}\") |> range(start: -1h)'
tables = client.query_api().query(query,org=org)
leituras_cpu = []
for table in tables:
    for row in table:
        leituras_cpu.append(row.values["_value"])
media = sum(leituras_cpu)/len(leituras_cpu)
print(f'Dados coletado do banco: {leituras_cpu}')
print("Média: {:.2f}%".format(media))
