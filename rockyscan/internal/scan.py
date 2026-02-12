import os
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from core.port_scanner import scan_ports

console = Console(width=120)

# -------------------------------
# Helper: parse port range
# -------------------------------
def parse_ports(port_range):
    start, end = port_range.split("-")
    return range(int(start), int(end) + 1)

# -------------------------------
# Core scan runner (logic same)
# -------------------------------
def run(target, ports="1-10000"):
    console.print(f"[bold cyan]Target:[/] {target}")
    console.print(f"[bold cyan]Ports:[/] {ports}\n")

    port_range = parse_ports(ports)
    results = scan_ports(target, port_range)

    table = Table(title="RockyScan Scan Results")
    table.add_column("Port", justify="center", style="green")
    table.add_column("Status", justify="center", style="yellow")
    table.add_column("Service", justify="center", style="cyan")

    if results:
        for r in results:
            table.add_row(str(r["port"]), "OPEN", r["service"])
    else:
        table.add_row("-", "No open ports", "-")

    console.print(table)

    report = {
        "tool": "RockyScan",
        "version": "1.0",
        "author": "Rocky Patel",
        "target": target,
        "ports_scanned": ports,
        "open_ports": results,
        "scan_time": str(datetime.now())
    }

    os.makedirs("output", exist_ok=True)
    with open("output/scan_result.json", "w") as f:
        json.dump(report, f, indent=4)

    console.print(
        "[bold green]✔ Scan completed. Report saved to output/scan_result.json[/]\n"
    )

# -------------------------------
# INTERACTIVE MODE (FIXED UX)
# -------------------------------
def interactive():
    console.print(
        "\n[bold magenta]ROCKYSCAN INTERNAL ENGINE[/bold magenta]\n"
        "[green]Usage:[/] <target> [port-range]\n"
        "[yellow]Commands:[/yellow]\n"
        "  back  / menu  → Return to main menu\n"
        "  exit          → Quit RockyScan\n"
        "  help          → Show help\n"
    )

    while True:
        user_input = console.input(
            "[bold magenta]rockyscan[/bold magenta]> "
        ).strip()

        # ---------------------------
        # Navigation commands
        # ---------------------------
        if not user_input:
            continue

        cmd = user_input.lower()

        if cmd in ("back", "menu"):
            return  # ⬅ back to main menu

        if cmd in ("exit", "quit"):
            raise SystemExit

        if cmd == "help":
            console.print(
                "[green]Example:[/green] 192.168.1.10 1-1000\n"
                "[yellow]Commands:[/yellow] back | menu | exit\n"
            )
            continue

        # ---------------------------
        # Scan command validation
        # ---------------------------
        parts = user_input.split()
        target = parts[0]

        # prevent accidental numeric-only input like "0"
        if target.isdigit():
            console.print(
                "[red]Invalid target.[/] Use IP address or hostname.\n"
            )
            continue

        ports = parts[1] if len(parts) > 1 else "1-10000"

        try:
            run(target, ports)
        except Exception as e:
            console.print(f"[red]Error:[/] {e}\n")
