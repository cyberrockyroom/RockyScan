# RockyScan 🔍

RockyScan is a Python-based CLI network security scanner inspired by Nmap.

## 📸 Tool Demo (Live Scan Output)

Below is a real execution output of **RockyScan** running on a local network target:

██████╗  ██████╗  ██████╗██╗  ██╗██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██║     █████╔╝  ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██║   ██║██║     ██╔═██╗   ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

RockyScan – CLI Network Security Scanner
Author: Rocky Patel
Version: 1.0

Target: 192.168.252.137
Ports: 1-10000

┏━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Port ┃ Status ┃ Service ┃
┡━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│  22  │  OPEN  │   SSH   │
│ 1716 │  OPEN  │ UNKNOWN │
│ 9090 │  OPEN  │ UNKNOWN │
└──────┴────────┴─────────┘

Scan completed. Report saved to output/scan_result.json


## Features
- TCP Port Scanning
- Automatic Service Name Detection
- Pretty CLI Output
- JSON Report Generation
- Nmap-style command usage

## ⚙️ Installation & Setup Guide

This section explains how anyone can install and use **RockyScan** on their system.

---

### 📌 Prerequisites
Make sure the following are installed on your system:

- Linux OS (Kali Linux / Ubuntu recommended)
- Python 3.8 or higher
- Git
- Internet connection

Check versions:

python3 --version
git --version

🛠️ Step-by-Step Installation
## 1️⃣ Clone the Repository
git clone https://github.com/cyberrockyroom/RockyScan.git
cd RockyScan

## 2️⃣ Create a Python Virtual Environment (Recommended)
python3 -m venv venv


Activate the virtual environment:

source venv/bin/activate

## 3️⃣ Install Required Dependencies
pip install -r requirements.txt

## 4️⃣ Make the Script Executable
chmod +x main.py

## 5️⃣ Install RockyScan as a System-Wide Command (Optional but Recommended)

This allows you to run RockyScan like nmap from anywhere in the terminal.

sudo ln -s $(pwd)/main.py /usr/local/bin/rockyscan


## Verify installation:

rockyscan --help


## Usage

rockyscan <target>
rockyscan <target> -p 1-10000

## Example
rockyscan 127.0.0.1 -p 1-10000

## Disclaimer
This tool is developed strictly for educational and authorized testing purposes only.
