INTERNSHIP DETAILS

COMPANY NAME: CODTECH IT SOLUTIONS PVT. LTD

INTERN NAME: Sanil Samir Mhatre

INTERN ID: CT08JTP

DOMAIN: Cyber Security & Ethical Hacking

BATCH DURATION: January 20th, 2025 to February 20th, 2025

MENTOR NAME: Neela Santosh Kumar


# Penetration-Testing-Toolkit
A penetration testing toolkit with a port scanner and a simple brute-forcer, allowing users to scan open ports and test passwords against a target file.

# Penetration Testing Toolkit

## Overview
This toolkit provides two essential penetration testing utilities:
1. **Port Scanner** - Scans a target host for open ports within a specified range.
2. **Simple Brute-Forcer** - Attempts to match passwords from a list against a target file to find valid credentials.

## Features
- Scans ports efficiently using socket connections.
- Performs brute-force attacks on files to identify valid credentials.
- Simple command-line interface for ease of use.

## Requirements
- Python 3.x

## Installation
1. Clone the repository or download the script:
   ```sh
   git clone https://github.com/your-repo/penetration-testing-toolkit.git
   cd penetration-testing-toolkit
   ```
2. Ensure Python 3 is installed on your system.

## Usage
Run the script using:
```sh
python main.py
```

### Port Scanner
1. Select option `1` in the menu.
2. Enter the target host (IP or domain).
3. Specify the port range (e.g., `1-1000`).

### Simple Brute-Forcer
1. Select option `2` in the menu.
2. Enter the path to the target file.
3. Enter the username to test.
4. Provide the path to the password list.

## Example Output
```
=== Penetration Testing Toolkit ===
1. Run Port Scanner
2. Run Simple Brute-Forcer
3. Exit
Select an option (1/2/3): 1
Enter the target host (IP or domain): 192.168.1.1
Enter the port range to scan (e.g., 1-1000): 1-100
Scanning 192.168.1.1 from port 1 to 100...
[+] Port 22 is open
[+] Port 80 is open
```

## Disclaimer
This tool is intended for educational and ethical penetration testing purposes only. Unauthorized use against systems you do not own or have explicit permission to test is illegal.

## License
This project is licensed under the MIT License.

## Output

