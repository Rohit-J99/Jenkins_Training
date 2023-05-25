import subprocess

subprocess.run("opa test  --policy ./policies/policy1 -v",shell=True)
subprocess.run("conftest verify --policy ./policies/policy1 --output=table",shell=True)