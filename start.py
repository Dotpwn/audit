import commands

user = 'inc'
dir_main_sshkey  = '/home/user/.ssh/audit.pub'
# dir_main = '/tmp/audit/'

'''
Create folder mkdir /tmp/audit/
cd /tmp/audit/
ssh-keygen (/home/user/.ssh/audit)
ssh-copy-id -f -i /home/user/.ssh/audit.pub user@10.10.10.10
'''

pwd = commands.getoutput('pwd')
ip_address_file = open(pwd + '/ip_address.txt', 'r')
ip_address_list = ip_address_file.read().split('\n')
for i in ip_address_list:
  a = commands.getoutput('ssh-copy-id -f -oStrictHostKeyChecking=no -oUserKnownHostsFile=/dev/null -i ' + dir_main_sshkey + ' ' + user + '@' + i)
  # dopisat' parol'