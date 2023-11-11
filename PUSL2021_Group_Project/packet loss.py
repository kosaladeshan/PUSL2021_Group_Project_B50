import subprocess
import re

def ping_google():
    # Execute ping command and get the output
    command = ['ping', '-c', '4', 'google.com']
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Extract packet loss from output
    packet_loss_line = [line for line in stdout.decode('utf-8').split('\n') if 'packet loss' in line]
    if packet_loss_line:
        packet_loss = re.findall(r'(\d+)% packet loss', packet_loss_line[0])
        if packet_loss:
            print(f'Packet loss: {packet_loss[0]}%')
        else:
            print('Could not extract packet loss information.')
    else:
        print('Could not find packet loss information.')

ping_google()
