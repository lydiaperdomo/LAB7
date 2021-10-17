import os
import netlike
from netlike import ConnectHandler
from get pass import get pass
from date time import date

USERNAME = input(‘Please enter your SSH username: ’)
PASSWORD = getpass(‘Please enter your SSH password: ‘)
date = date.today().strftime(‘%Y_%m_%d’)

device = {
	‘ip’ = ‘192.168.108.10’
	‘username’ : USERNAME,
	‘password’ : PASSWORD,
	‘device_type’ : ‘cisco_ios’
}

c = ConnectHandler(**device)

output = c.send_command(‘show run’)

f = open(f’back_configuration{date}’, ‘x’)

f.write(output)
f.close