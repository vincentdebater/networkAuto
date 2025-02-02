from napalm import get_network_driver
import json
driver = get_network_driver("h3c_comware")
conn_args = {
    "port": 22
}
device = driver("siteO.vd.com", "admin", "H3@132comware",optional_args=conn_args)
device.open()
ret = device.is_alive()
print(json.dumps(ret,indent=2))
ret = device.send_command("display clock", use_textfsm=True)
print(json.dumps(ret,indent=2))