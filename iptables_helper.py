import subprocess

def apply_block_rule(ip, port, protocol="tcp"):
    cmd = f"sudo iptables -A INPUT -s {ip} -p {protocol} --sport {port} -j DROP"
    subprocess.run(cmd, shell=True)

def remove_block_rule(ip, port, protocol="tcp"):
    cmd = f"sudo iptables -D INPUT -s {ip} -p {protocol} --sport {port} -j DROP"
    subprocess.run(cmd, shell=True)
