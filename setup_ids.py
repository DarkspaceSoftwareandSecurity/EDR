import os
import sys
import platform
import subprocess

# Define the base directory based on the provided path
BASE_DIR = r"C:\Users\micky\OneDrive\Desktop\IDS" if platform.system() == "Windows" else os.path.expanduser("~/Desktop/IDS")

# Define the folder structure for IDS
FOLDERS = [
    "logs",           # To store network traffic and system logs
    "reports",        # To store XLS and DOCX reports
    "config",         # Configuration files for IDS settings
    "scripts",        # To store scripts for analysis and automation
    "pcap_data",      # To store packet capture files
]

# Requirements for the project
REQUIREMENTS = [
    "pandas",        # To generate XLS reports
    "matplotlib",    # For generating graphs and charts
    "python-docx",   # For generating DOCX reports (correct library name)
    "scapy",         # To analyze network traffic (if needed)
    "numpy",         # Numerical computations
    "requests",      # For threat intelligence API integration
]

def create_folder_structure():
    print("[+] Creating folder structure...")
    for folder in FOLDERS:
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"    [Created] {folder_path}")
        else:
            print(f"    [Exists] {folder_path}")
    print("[+] Folder structure created successfully.\n")

def install_dependencies():
    print("[+] Installing dependencies...")
    python_cmd = "python" if platform.system() == "Windows" else "python3"
    
    try:
        # Install each requirement separately
        subprocess.check_call([python_cmd, "-m", "pip", "install"] + REQUIREMENTS)
        print("[+] Dependencies installed successfully.\n")
    except subprocess.CalledProcessError as e:
        print("[-] Error during dependency installation:", e)
        sys.exit(1)

def main():
    # Step 1: Detect Operating System
    current_os = platform.system()
    print(f"[+] Detected OS: {current_os}\n")

    # Step 2: Create Folder Structure
    create_folder_structure()

    # Step 3: Install Dependencies
    install_dependencies()

    # Step 4: Print Completion Message
    print("[+] IDS Setup Complete! The environment is ready for monitoring and analysis.\n")

if __name__ == "__main__":
    main()
