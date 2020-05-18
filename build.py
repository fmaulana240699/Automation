import os
import subprocess
import sys

sshProcess = subprocess.Popen(['ssh',"ec2-user@master"],stdin=subprocess.PIPE,stdout = subprocess.PIPE,universal_newlines=True,bufsize=0)
sshProcess.stdin.write("git clone https://github.com/fmaulana240699/Automation.git \n")
sshProcess.stdin.close()

sshProcess = subprocess.Popen(['ssh',"ec2-user@master"],stdin=subprocess.PIPE,stdout = subprocess.PIPE,universal_newlines=True,bufsize=0)
sshProcess.stdin.write("kubectl get deployment | grep -i python \n")
sshProcess.stdin.close()

output=sshProcess.stdout
deployment=output.read()
print(deployment)

sshProcess = subprocess.Popen(['ssh',"ec2-user@master"],stdin=subprocess.PIPE,stdout = subprocess.PIPE,universal_newlines=True,bufsize=0)
sshProcess.stdin.write("kubectl get svc | grep -i python")
sshProcess.stdin.close()

output2=sshProcess.stdout
service=output2.read()
print(service)



if deployment == None:
    sshProcess = subprocess.Popen(['ssh',"ec2-user@master"],stdin=subprocess.PIPE,stdout = subprocess.PIPE,universal_newlines=True,bufsize=0) 
    sshProcess.stdin.write("cd Automation \n ansible-playbook build.yaml \n")
    sshProcess.stdin.close()

    output3=sshProcess.stdout
    hasil=output3.read()
    print(hasil)

else:
    sshProcess = subprocess.Popen(['ssh',"ec2-user@master"],stdin=subprocess.PIPE,stdout = subprocess.PIPE,universal_newlines=True,bufsize=0) 
    sshProcess.stdin.write("cd Automation \n ansible-playbook update.yaml \n")
    sshProcess.stdin.close()

    output4=sshProcess.stdout
    hasil2=output4.read()
    print(hasil2)
   





