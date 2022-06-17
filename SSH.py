import paramiko

client = paramiko.SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="raspberrypi", username="dave", password="dave")

print(client)

ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command('ss -ltn')

results = []

for line in ssh_stdout:
    results.append(line.strip('\n'))

for i in results:
    print(i.strip())
