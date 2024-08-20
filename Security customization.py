
import os
import platform
import subprocess

def detect_os():
    """Detect the operating system."""
    return platform.system()

def enforce_strong_password_policy():
    """Enforce strong password policies."""
    os_type = detect_os()
    if os_type == "Windows":
        try:
            subprocess.run(["net", "accounts", "/minpwlen:12", "/maxpwage:30"], check=True)
            print("Password policy enforced on Windows.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to enforce password policy: {e}")

def disable_unnecessary_services():
    """Disable unnecessary services."""
    os_type = detect_os()
    if os_type == "Windows":
        services_to_disable = ["Spooler", "WSearch"]
        for service in services_to_disable:
            try:
                subprocess.run(["sc", "config", service, "start=", "disabled"], check=True)
                subprocess.run(["sc", "stop", service], check=True)
                print(f"Disabled service: {service}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to disable service {service}: {e}")

def configure_firewall():
    """Enable and configure the firewall."""
    os_type = detect_os()
    if os_type == "Windows":
        try:
            subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "state", "on"], check=True)
            subprocess.run(["netsh", "advfirewall", "set", "allprofiles", "firewallpolicy", "blockinbound,allowoutbound"], check=True)
            print("Firewall configured on Windows.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to configure firewall: {e}")

def manage_file_permissions():
    """Restrict file and directory permissions."""
    os_type = detect_os()
    if os_type == "Windows":
        critical_dirs = ["C:\\Windows", "C:\\Program Files", "C:\\Users"]
        for directory in critical_dirs:
            try:
                subprocess.run(["icacls", directory, "/inheritance:r"], check=True)
                print(f"Configured permissions for: {directory}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to configure permissions for {directory}: {e}")

def configure_logging():
    """Ensure logging is enabled and configure log rotation."""
    os_type = detect_os()
    if os_type == "Windows":
        print("Logging configuration for Windows.")
        # Logging configuration implementation here

def apply_system_updates():
    """Check for and install system updates."""
    os_type = detect_os()
    if os_type == "Windows":
        try:
            subprocess.run(["powershell", "-Command", "Install-WindowsUpdate -AcceptAll -AutoReboot"], check=True)
            print("System updates applied on Windows.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to apply system updates: {e}")

def main():
    """Main function to run all hardening tasks."""
    os_type = detect_os()
    print(f"Operating System detected: {os_type}")

    enforce_strong_password_policy()
    disable_unnecessary_services()
    configure_firewall()
    manage_file_permissions()
    configure_logging()
    apply_system_updates()

if __name__ == "__main__":
    main()
