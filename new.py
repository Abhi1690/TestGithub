import subprocess
import getpass
import os
#p = subprocess.Popen('cd', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#for line in p.stdout.readlines():
  #  print line,
#retval = p.wait()
#os.system('dir')os.system
amd = raw_input("Enter file location : ")
os.chdir(amd)
os.system("dir")
print("done")
raw_input()
raw_input()
