import os 

with open('/pswd') as f:
	first_line=f.readline()
first=first_line.split(':')
pswd=first[1]


with open('/etc/shadow') as f:
	first_line_new=f.readline()
first_new=first_line_new.split(':')
pswd_new=first_new[1]

if pswd!=pswd_new:
	print("Your root password has been changed")

else:
	print("nothing happened")

os.system("cp /etc/shadow /pswd")
