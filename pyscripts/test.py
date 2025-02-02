from napalm import get_network_driver
import json

driver = get_network_driver('huawei_vrp')
device_list = [ {'hostname':'siteM.vd.com','username':'admin','password':'Cisco@321'},
                {'hostname':'siteC.vd.com','username':'admin','password':'Cisco@123'},
                {'hostname':'siteN.vd.com','username':'admin','password':'Cisco@123'}
]

def device_operate ():
  for i in range(0,len(device_list)):

    device = driver(hostname=device_list[i]['hostname'],username=device_list[i]['username'],password=device_list[i]['password'])
    device.open()


# # Send Any CLI command
    send_command = device.cli(['dis health'])
    print (send_command)
# #  Return general device information
# # get_facts = device.get_facts()
# # print(get_facts)
    get_facts = device.get_interfaces_ip()
    print (json.dumps(get_facts, indent=2))
    device.close()
# other API
# device.get_config()
# device.get_arp_table()
# device.get_mac_address_table()
# device.get_interfaces()
# device.get_interfaces_ip()
# device.get_interfaces_counters()

# device.get_lldp_neighbors()
device_operate()

