import subprocess as sp
x = sp.getoutput("ansible all -m command -a lsblk | grep disk")
#a = x.split("disk")	
#for i in x:
#	if i
#while i in a !=' ':
print(x)
	

