System Hardening Script

Overview

This Python script performs a set of system hardening tasks, aimed at increasing the security posture of a Windows operating system. It automates several key actions such as enforcing strong password policies, disabling unnecessary services, configuring the firewall, managing file permissions, enabling logging, and applying system updates.

The script is currently tailored for Windows systems, but it can be extended to support other operating systems with minimal modifications.

Features

The script performs the following tasks:
1. Enforces Strong Password Policy:
   - Sets the minimum password length to 12 characters and the maximum password age to 30 days.

2. Disables Unnecessary Services:
   - Disables services that are not critical to system operation, such as the Print Spooler (`Spooler`) and Windows Search (`WSearch`), which may introduce vulnerabilities if not required.

3. Configures the Firewall:
   - Enables the Windows firewall for all profiles (Domain, Private, and Public).
   - Sets the firewall policy to block all inbound traffic and allow outbound traffic.

4. Manages File Permissions:
   - Restricts file and directory permissions on critical system directories (e.g., `C:\Windows`, `C:\Program Files`, and `C:\Users`) by removing inherited permissions.

5. Configures Logging:
   - Placeholder for configuring logging and ensuring that appropriate logs are enabled and managed. This can be expanded to configure Event Viewer or other logging mechanisms.

6. Applies System Updates:
   - Installs any pending Windows updates using PowerShell’s `Install-WindowsUpdate` command and automatically reboots the system if necessary.

Prerequisites

- The script is designed to run on Windows systems.
- Requires Python 3.x installed.
- Some functions utilize **PowerShell** and Windows command-line tools (e.g., `net`, `netsh`, `sc`, `icacls`), so administrative privileges are required to execute the script.

How to Use

1. Clone the repository:
```bash
git clone <repository_url>
```

2. Run the Script:
To run the script, simply execute the following command from the command line with administrative privileges:
```bash
python system_hardening.py
```

3. Output:
The script will detect the operating system and execute the corresponding hardening tasks. If any task fails, an error message will be displayed in the terminal.

Functions Description

1. detect_os():
   - Detects the current operating system using the `platform` module.
   - Returns the OS name (e.g., "Windows").

2. enforce_strong_password_policy():
   - Uses the `net accounts` command to enforce a minimum password length of 12 characters and a maximum password age of 30 days.

3. disable_unnecessary_services():
   - Disables unnecessary services like the Print Spooler (`Spooler`) and Windows Search (`WSearch`) to minimize attack surfaces.

4. configure_firewall():
   - Configures the Windows firewall to ensure it is enabled and set to block all inbound traffic while allowing outbound traffic.

5. manage_file_permissions():
   - Manages permissions for critical system directories by removing inherited permissions using the `icacls` command.

6. configure_logging():
   - Placeholder function for configuring system logging. This can be expanded to set up Event Viewer logs or other logging solutions.

7. apply_system_updates():
   - Installs Windows updates using PowerShell’s `Install-WindowsUpdate` command to ensure the system is up to date with the latest security patches.

Customization

- Add or Modify Services to Disable:
   You can add more services to disable or remove ones you need by modifying the `services_to_disable` list inside the `disable_unnecessary_services()` function.

- Logging Configuration:
   Expand the `configure_logging()` function to configure specific logging settings based on your organization’s requirements.

Limitations

- The script is currently only designed to work on **Windows** systems.
- Requires **administrative privileges** to run successfully.
- Logging functionality needs to be fully implemented.


