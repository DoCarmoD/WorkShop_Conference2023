from pyzabbix import ZabbixAPI
from pprint import pprint
import csv

itens_para_cadastro = []

with open('hosts.CSV', 'r' ) as file:
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        linha_identifica = row
        itens_para_cadastro.append(linha_identifica)


zapi = ZabbixAPI("http://172.23.38.192/zabbix")
zapi.login("Admin", "zabbix")
print("Connected to Zabbix API Version %s" % zapi.api_version())

for i in range(1, len(itens_para_cadastro)):
    host_dados = itens_para_cadastro[i]
    hostname = host_dados[0]
    ip = host_dados[1]
    if hostname == "":
        pprint("Sem hostname")
    else:
        pprint("Iniciando verificação de cadastro")
        hosts_valid = zapi.host.get(filter={'host':[hostname]})
        if hosts_valid != []:
            pprint('Item cadastrado')
        else:
            pprint("item não cadastrado")
            pprint("Iniciando Cadastro")
            new_host = zapi.host.create(
                            host=hostname,
                            interfaces= {  
                                "type": 1,
                                "main": 1,
                                "useip": 1,
                                "ip": ip,
                                "dns": "",
                                "port": "10050"
                            },
                            groups = [{ "groupid": "5"}],

            )


