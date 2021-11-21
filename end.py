import commands

# scp -i key inc@10.10.10.16:/tmp/audit/
dir_main = '/tmp/audit/'
dir_host = '/tmp/audit/'

key_rsa = '/home/user/.ssh/audit'
user = 'inc'


ip_address_file = open('./ip_address.txt', 'r')
ip_address_list = ip_address_file.read().split('\n')
for i in ip_address_list:
  a = commands.getoutput('scp -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i ' + key_rsa + ' -r ' + user + '@' + i +':' + dir_host + ' ' + dir_main)
  b = commands.getoutput('ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i ' + key_rsa + ' ' + user + '@' + i + ' ' + "'rm -rf /tmp/audit ; rm -rf /tmp/audit.py'")