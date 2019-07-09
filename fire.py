import subprocess as sp
#y="systemctl status firewalld"
x=sp.getoutput("ansible localhost -m command -a 'systemctl status firewalld' ")
if "inactive" in  x:
	print("noactive")
else:
	print("yes") 
#print(x)
#<?xml version="1.0"?>
#<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
