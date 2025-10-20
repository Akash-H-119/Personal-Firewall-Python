import subprocess

def apply_block_rule(ip, port, protocol="TCP"):
    cmd = f'netsh advfirewall firewall add rule name="Block {ip}:{port}" dir=in action=block remoteip={ip}'
    subprocess.run(cmd, shell=True)

def remove_block_rule(ip, port, protocol="TCP"):
    cmd = f'netsh advfirewall firewall delete rule name="Block {ip}:{port}"'
    subprocess.run(cmd, shell=True)
