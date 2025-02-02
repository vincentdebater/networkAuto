from napalm import get_network_driver
import json
driver = get_network_driver('huawei_vrp')
device = driver(hostname='siteM.vd.com', username='admin', password='Cisco@12345')
device.open()

# Send Any CLI command
send_command = device.cli(['dis health'])
print (send_command)
#  Return general device information
# get_facts = device.get_facts()
# print(get_facts)
get_facts = device.get_interfaces()
print (json.dumps(get_facts, indent=2))

# other API
# device.get_config()
# device.get_arp_table()
# device.get_mac_address_table()
# device.get_interfaces()
# device.get_interfaces_ip()
# device.get_interfaces_counters()
# device.get_lldp_neighbors()