import subprocess
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--Arg1")
parser.add_argument("--Arg2")
Args=parser.parse_args()

pythonV='the current version is 3.11'
os.environ['pythonV'] = PYTHONV
print(os.environ["NEW_VERSION"])

sub1=subprocess.run("opa test ./policies/policy1 -v",shell=True,capture_output=True,text=True)
sub2=subprocess.run("conftest verify --policy ./policies/policy1 --output=table",shell=True,capture_output=True,text=True)

if(sub1.returncode==0 and sub2.returncode==0):
    print(sub1.stdout,sub2.stdout)
    print('Success!')
else:
    print('Failure!')

print(Args)

