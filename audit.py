import commands
import os


dir_main = '/tmp/'


name = commands.getoutput('cat /proc/sys/kernel/hostname')
ip = commands.getoutput("ip a | grep 'inet'")
OS_version = commands.getoutput("hostnamectl | grep 'Operating System'")

if OS_version.find('ALT') == -1:
  print('no ALT')
  list_apt = commands.getoutput('dpkg-query -l')
else:
  print('ALT')
  list_apt = commands.getoutput('rpm -qa')
  
list_exe = commands.getoutput('find / -executable')
list_opt = commands.getoutput('find /opt/ ; find /usr/opt/ ; find /usr/local/')
list_opt_ls = commands.getoutput('ls -lR /opt/ ; ls -lR /usr/opt/ ; ls -lR /usr/local/')

tmp = dir_main + 'audit/'
tempe = dir_main + 'audit/' + name
print(tempe)

try:
  os.mkdir(tmp)
  os.mkdir(tempe)
except OSError:
  print('error')
else:
  file_apt = open(str(tempe) + '/' + str(name) + ' apt.txt', 'w')
  file_apt.write(list_apt)
  
  file_exe = open(str(tempe) + '/' + str(name) + ' exe.txt', 'w')
  file_exe.write(list_exe)
  
  file_opt = open(str(tempe) + '/' + str(name) + ' opt.txt', 'w')
  file_opt.write(list_opt)

  file_opt_ls = open(str(tempe) + '/' + str(name) + ' opt_ls.txt', 'w')
  file_opt_ls.write(list_opt_ls)
  
  file_host_ip = open(str(tempe) + '/' + str(name) + ' host_ip.txt', 'w')
  file_host_ip.write(ip + '\n' + OS_version)
  
  file_apt.close
  file_exe.close
  file_opt.close
  file_opt_ls.close

  print('success')
