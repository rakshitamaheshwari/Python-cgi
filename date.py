import subprocess  as sp
a=sp.getoutput("ansible localhost -m command  -a date")
b=a.split('\n')
print(b[1])
