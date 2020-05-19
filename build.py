import os

deploy=os.popen("kubectl get deployment | grep -i python")
deployment= deploy.read()

serv=os.popen("kubectl get svc | grep -i python ")
services= serv.read()

if deployment == None:
    os.system("kubectl create -f deployment.yaml && kubectl create -f services.yaml")
    os.system("cd .. && rm -rf Automation")

    s=os.popen("kubectl get deployment | grep -i python")
    success= s.read()

    if success == None:
        print("Build App Gagal")
        terminate()
    else:
        print("Build App Berhasil")

else:
    os.system("kubectl set image deployment/socket-fajar-python socket-python-fajar=fmaulana24/socket:v$BUILD_NUMBER --record")
    os.system("cd .. && rm -rf Automation")
    print("Update Aplikasi Berhasil")