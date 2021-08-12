import sys
import paramiko
import getpass

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

while(True):
    comm = raw_input("Enter Command to Execute or Q to Quit:\n")
    if 'Q' in comm:
        print("GoodBye")
        sys.exit()
    with open("hosts") as hosts:
        for host in hosts:
            host=host.strip()
            username=getpass.getuser()
            port=22
            try:
                ssh.connect(host, port, usernamee)
            except :
                print("Host: "+host+" SSH Failed")
                continue

            stdin, stdout, stderr = ssh.exec_command(comm)
            if stdout.channel.recv_exit_status() == 0:
                print("Host: "+host+" Command Success")
            else:
                print("Host: "+host+" Command Failed")
