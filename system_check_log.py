import paramiko
from datetime import datetime

hostname = "10.8.0.1"
port = 22
username = "nipun"
password = "1234"

# Commands to run
commands = [
    "hostname",
    "uptime",
    "df -h",
    "free -m",
    f"echo {password} | sudo -S -p '' ufw status",
    f"echo {password} | sudo -S -p '' fail2ban-client status"
]

# Create a timestamped log file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = f"system_audit_{timestamp}.log"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port, username, password)

    with open(log_file, "w") as log:
        for cmd in commands:
            log.write(f"\n=== Command: {cmd} ===\n")
            stdin, stdout, stderr = client.exec_command(cmd)
            output = stdout.read().decode()
            errors = stderr.read().decode()
            log.write(output or "(No output)\n")
            if errors.strip():
                log.write(f"[Error]\n{errors}\n")

    print(f"Output saved to: {log_file}")

finally:
    client.close()
