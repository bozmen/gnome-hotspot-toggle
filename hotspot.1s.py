#!/usr/bin/env python3

import subprocess
network = 'nmcli connection show Hotspot'
grep = 'grep GENERAL.STATE'
p1 = subprocess.Popen(network.split(), stdout=subprocess.PIPE)
p2 = subprocess.Popen(grep.split(), stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close() 
output, error = p2.communicate()

if len(output) > 0:
	state = output.split()[1]
else:
	state = ''

if state == b'activated':
	print ("on | iconName=network-wireless-symbolic")
	print("---")
	print("Turn hotspot off | bash='nmcli connection down Hotspot' terminal='false'")
elif state == b'activating':
	print ("activating | iconName=network-wireless-acquiring-symbolic")
	print("---")
	print("Activating...")
else:
	print ("off | iconName=network-wireless-offline-symbolic")
	print("---")
	print("Turn hotspot on | bash='nmcli connection up Hotspot' terminal='false'")




