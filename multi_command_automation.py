import paramiko

# Server login details
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
    f"echo {password} | sudo -S ufw status",
    f"echo {password} | sudo -S fail2ban-client status"
]

# SSH client setup
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port, username, password)

    for cmd in commands:
        print(f"\n Running: {cmd}")
        stdin, stdout, stderr = client.exec_command(cmd)
        output = stdout.read().decode()
        errors = stderr.read().decode()

        print("Output:")
        print(output if output else "(No output)")
        
        if errors:
            print("Error:")
            print(errors)

except Exception as e:
    print("Connection error:", e)

finally:
    client.close()
