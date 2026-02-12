import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

# ----------------------------------
# Tool mapping
# ----------------------------------
TOOLS = {
    "1": ("ROCKYSCAN", "internal"),
    "2": ("Nmap", "nmap"),
    "3": ("Masscan", "masscan"),
    "4": ("RustScan", "rustscan"),
    "5": ("Naabu", "naabu"),
    "6": ("Netcat", "nc"),
    "7": ("Hping3", "hping3"),
    "8": ("Unicornscan", "unicornscan"),
    "9": ("Angry IP Scanner", "ipscan"),
    "10": ("Fscan", "fscan"),
}

# ----------------------------------
# Examples for each tool (🔥 UX MAGIC)
# ----------------------------------
EXAMPLES = {
    "nmap": [
        "-sS -p 22 192.168.1.10",
        "-sV -p 1-1000 scanme.nmap.org"
    ],
    "masscan": [
        "192.168.1.0/24 -p80,443 --rate 1000"
    ],
    "rustscan": [
        "-a 192.168.1.10 --ulimit 5000"
    ],
    "naabu": [
        "-host 192.168.1.10"
    ],
    "nc": [
        "-zv 192.168.1.10 22"
    ],
    "hping3": [
        "-S -p 80 192.168.1.10"
    ],
    "unicornscan": [
        "192.168.1.10:1-1000"
    ],
    "ipscan": [
        "192.168.1.0/24"
    ],
    "fscan": [
        "-h 192.168.1.10"
    ],
}

# ----------------------------------
# Launcher
# ----------------------------------
def launch(choice):
    tool_info = TOOLS.get(choice)

    if not tool_info:
        console.print("[red]Invalid option[/red]")
        return

    tool_name, binary = tool_info

    # -------------------------------
    # Internal RockyScan
    # -------------------------------
    if binary == "internal":
        from rockyscan.internal.scan import interactive
        interactive()
        return

    # -------------------------------
    # External tools
    # -------------------------------
    example_text = ""
    if binary in EXAMPLES:
        example_text = "\n".join(
            f"  {ex}" for ex in EXAMPLES[binary]
        )

    panel = Panel(
        f"[bold green]{tool_name} MODE[/bold green]\n\n"
        "[bold cyan]Examples:[/bold cyan]\n"
        f"{example_text}\n\n"
        "[yellow]Type commands exactly like original tool[/yellow]\n"
        "[dim]Type 'back' to return to menu[/dim]",
        border_style="cyan"
    )

    console.print(panel)

    while True:
        cmd = console.input(f"[bold cyan]{binary}[/bold cyan]> ").strip()

        if not cmd:
            continue

        if cmd.lower() == "back":
            return

        try:
            subprocess.run([binary] + cmd.split())
        except FileNotFoundError:
            console.print(
                f"[red]Error:[/] {binary} not installed on this system\n"
            )
            return
