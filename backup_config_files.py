import paramiko
import os

# Connection info
hostname = "10.8.0.1"
port = 22
username = "nipun"
password = "1234"

# Local directory to save files
backup_dir = "backups"
os.makedirs(backup_dir, exist_ok=True)

# Files to download: source -> destination
config_files = {
    "/etc/fail2ban/jail.local": os.path.join(backup_dir, "jail.local"),
    "/etc/ufw/ufw.conf": os.path.join(backup_dir, "ufw.conf"),
    "/etc/openvpn/server.conf": os.path.join(backup_dir, "openvpn_server.conf"),
}

# Connect and fetch files
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {hostname}...")
    ssh.connect(hostname, port, username, password)

    sftp = ssh.open_sftp()

    for remote_file, local_file in config_files.items():
        try:
            print(f"Downloading {remote_file}...")
            sftp.get(remote_file, local_file)
            print(f"Saved to {local_file}")
        except FileNotFoundError:
            print(f"File not found: {remote_file} (skipped)")

    sftp.close()
    ssh.close()

except Exception as e:
    print(f"Connection or SFTP error: {e}")
