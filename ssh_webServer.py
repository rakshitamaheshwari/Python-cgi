import subprocess as sp
import os

os.system("ssh 192.168.43.62 yum install httpd -y")
os.system("ssh 192.168.43.62 cat > /var/www/html/abc.html")
os.system("ssh 192.168.43.62 iptables -F")
os.system("ssh 192.168.43.62 systemctl restart httpd")
