import os

#os.system("kubectl get pods")

deploy=os.popen("kubectl get deployment | grep -i python")
deployment= deploy.read()

serv=os.popen("kubectl get svc | grep -i python ")
services= serv.read()

if deployment == None:
    os.system("ansible-playbook build.yaml")
    verif=os.popen("kubectl get deployment")
    verify=verif.read()

    if verify == None:
        print("Build Aplikasi GAGAL")
    else:
       print("Build Aplikasi BERHASIL")
else:
    os.system("ansible-playbook update.yaml")
    print("Update Aplikasi BERHASIL")
