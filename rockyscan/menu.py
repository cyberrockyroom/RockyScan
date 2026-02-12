from rich.console import Console
from rich.table import Table

console = Console()

def show_menu():
    table = Table(title="Select Scanning Engine", header_style="bold cyan")
    table.add_column("ID", justify="center")
    table.add_column("Tool")
    table.add_column("Description")

    table.add_row("1", "[bold magenta]ROCKYSCAN[/bold magenta]", "Built-in scanner")
    table.add_row("2", "Nmap", "Industry standard")
    table.add_row("3", "Masscan", "Fast scanner")
    table.add_row("4", "RustScan", "Modern scanner")
    table.add_row("5", "Naabu", "Bug bounty tool")
    table.add_row("6", "Netcat", "Manual scan")
    table.add_row("7", "Hping3", "Packet crafting")
    table.add_row("8", "Unicornscan", "Async scan")
    table.add_row("9", "Angry IP Scanner", "IP scanner")
    table.add_row("10", "Fscan", "Internal network scan")
    table.add_row("0", "Exit", "Quit")

    console.print(table)
    return console.input("➜ Enter choice: ")
