## 📸 Tool Demo (Live Scan Output)

Below is a real execution output of **RockyScan** running on a local network target:

```text
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

🛠️ Step-by-Step Installation
1️⃣ Clone the Repository

git clone https://github.com/cyberrockyroom/RockyScan.git
cd RockyScan

2️⃣ Create a Python Virtual Environment (Recommended)

python3 -m venv venv


Activate the virtual environment:

source venv/bin/activate

3️⃣ Install Required Dependencies

pip install -r requirements.txt

4️⃣ Make the Script Executable

chmod +x main.py

5️⃣ Install RockyScan as a System-Wide Command (Optional but Recommended)

This allows you to run RockyScan like nmap from anywhere in the terminal.

sudo ln -s $(pwd)/main.py /usr/local/bin/rockyscan


Verify installation:

rockyscan --help

▶️ Usage
🔹 Basic Scan

rockyscan <target-ip>


Example:

rockyscan 192.168.1.10

🔹 Scan with Custom Port Range

rockyscan <target-ip> -p 1-10000


Example:

rockyscan 192.168.1.10 -p 1-10000
