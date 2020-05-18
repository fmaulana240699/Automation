import os

#os.system("kubectl get pods")

deploy=os.popen("kubectl get deployment | grep -i python")
deployment= deploy.read()

serv=os.popen("kubectl get svc | grep -i python ")
services= serv.read()

if deployment == None:
    os.system("ansible-playbook build.yaml && rm -rf Automation")
else:
    os.system("ansible-playbook update.yaml && rm -rf Automation")

