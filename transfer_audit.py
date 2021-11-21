import commands

# cd /tmp/audit/
dir_main = '/tmp/audit/audit.py'
dir_host = '/tmp/audit.py'

key_rsa = '/home/user/.ssh/audit'
user = 'inc'

ip_address_file = open('./ip_address.txt', 'r')
ip_address_list = ip_address_file.read().split('\n')
for i in ip_address_list:
  # a = commands.getoutput('ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i ' + key_rsa + ' ' + user + '@' + i + ' ' + "'mkdir /tmp/audit/'")
  b = commands.getoutput('scp -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i ' + key_rsa + ' -r ' + dir_main + ' ' + user + '@' + i +':' + dir_host)
  c = commands.getoutput('ssh -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i ' + key_rsa + ' ' + user + '@' + i + ' ' + "'python /tmp/audit.py'")
