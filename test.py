import commands
import os, sys

name = commands.getoutput('cat /proc/sys/kernel/hostname')
list_apt = commands.getoutput('rpm -qa')
list_exe = commands.getoutput('find / -executable')
list_opt = commands.getoutput('find /opt/')
list_opt_usr = commands.getoutput('find /user/opt') ###
tempe = os.path.dirname(os.path.abspath(sys.argv[0])) + '/' + name
list_opt_ls = commands.getoutput('ls -lR /opt ')
list_opt_usr_ls_full = ''

if str(commands.getoutput("find */opt/")).find('find') == False:
  list_opt_usr_folder = commands.getoutput("find */opt/").split('\n')
  for i in range(list_opt_usr_folder):
    list_opt_usr_ls = commands.getoutput('ls' + '-lR' + list_opt_usr_folder[i])
    list_opt_usr_ls_full = list_opt_usr_ls_full + list_opt_usr_ls

if str(commands.getoutput("find /usr/local")).find('find') == False:
  list_usr_local = commands.getoutput('ls -lR /usr/local/')
  list_opt_usr_ls_full = list_opt_usr_ls_full + list_usr_local

  
try:
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
  
  file_opt_usr = open(str(tempe) + '/' + str(name) + ' opt_usr.txt', 'w')
  file_opt_usr.write(list_opt_usr)
  
  file_opt_ls = open(str(tempe) + '/' + str(name) + ' opt_ls.txt', 'w')
  file_opt_ls.write(list_opt_ls)
  
  file_opt_ls_full = open(str(tempe) + '/' + str(name) + ' opt_ls_full.txt', 'w')
  file_opt_ls_full.write(list_opt_usr_ls_full)
  
  file_apt.close
  file_exe.close
  file_opt.close
  file_opt_usr.close
  file_opt_ls.close
  file_opt_ls_full.close
  print('success')
    

