import subprocess as sp
a=sp.getoutput("ansible localhost -m command -a cal")
print(a[30:])


