import os
print("testing")
deploy=os.popen("echo $fmaulana")
deployment= deploy.read()

print(deployment)
