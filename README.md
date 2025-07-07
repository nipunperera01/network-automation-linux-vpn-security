# 🔐 Network Automation for VPN and Server Security (Paramiko)

This project uses Python's Paramiko library to:
- Automate SSH login to a remote Ubuntu server
- Run key security system checks (firewall, Fail2Ban, uptime, RAM, etc.)
- Download and back up configuration files (UFW, Fail2Ban, OpenVPN)
- Log all outputs into timestamped `.log` files

---

## 🧰 Tools & Technologies
- Python 3
- Paramiko
- OpenVPN
- Fail2Ban
- UFW Firewall
- Ubuntu Server on VMware

---

## 📁 Included Files
- `system_check_log.py`: Runs and logs system checks
- `backup_config_files.py`: Downloads `/etc/` config files
- `ssh_test.py`: First test - show server details
- `multi_command_automation.py`: Runs multi commands in one file
- `backups/`: Sample output folder
- `screenshots/`: Screenshots of output and config files

---

## 🧠 What I Learned
- Automating SSH-based Linux tasks
- Using Paramiko for both SSH and SFTP
- Security practices with VPN-only access
- Backing up real firewall and intrusion protection configs

---

## 📸 Screenshots
- Paramiko install 
- test-output
- multi command output
- backup config output and folder
- system check output and log

---

## 🛡️ Use Case

A junior network or system admin could use this script to routinely audit VPN/firewall security and back up config files in production or lab networks.

---

## 📎 Author

Nipun Perera
