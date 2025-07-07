import paramiko

# Replace with your Ubuntu VM details
hostname = "10.8.0.1" 
port = 22
username = "nipun"    
password = "1234"    

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {hostname}...")
    client.connect(hostname, port, username, password)

    stdin, stdout, stderr = client.exec_command("uname -a")
    print("Output:\n", stdout.read().decode())

except Exception as e:
    print("Error:", e)

finally:
    client.close()
