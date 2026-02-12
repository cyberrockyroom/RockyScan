#!/usr/bin/env python3

import os
import sys
import argparse
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from core.port_scanner import scan_ports

console = Console(width=120)

BANNER = r"""
██████╗  ██████╗  ██████╗██╗  ██╗██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝██║   ██║██║     █████╔╝  ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
██╔══██╗██║   ██║██║     ██╔═██╗   ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

def parse_ports(port_range):
    start, end = port_range.split("-")
    return range(int(start), int(end) + 1)

def main():
    console.print(BANNER, style="bold cyan")
    console.print("[bold yellow]RockyScan – CLI Network Security Scanner[/]")
    console.print("[green]Author:[/] Rocky Patel")
    console.print("[green]Version:[/] 1.0\n")

    parser = argparse.ArgumentParser(
        description="RockyScan - Personal CLI Based Network Security Scanner"
    )

    parser.add_argument(
        "target",
        help="Target IP address or domain"
    )

    parser.add_argument(
        "-p", "--ports",
        default="1-10000",
        help="Port range (default: 1-10000)"
    )

    args = parser.parse_args()

    console.print(f"[bold cyan]Target:[/] {args.target}")
    console.print(f"[bold cyan]Ports:[/] {args.ports}\n")

    ports = parse_ports(args.ports)
    results = scan_ports(args.target, ports)

    table = Table(title="RockyScan Scan Results")
    table.add_column("Port", style="green", justify="center")
    table.add_column("Status", style="yellow", justify="center")
    table.add_column("Service", style="cyan", justify="center")

    if results:
        for item in results:
            table.add_row(
                str(item["port"]),
                "OPEN",
                item["service"]
            )
    else:
        table.add_row("-", "No open ports found", "-")

    console.print(table)

    report = {
        "tool": "RockyScan",
        "version": "1.0",
        "author": "Rocky Patel",
        "target": args.target,
        "ports_scanned": args.ports,
        "open_ports": results,
        "scan_time": str(datetime.now())
    }

    os.makedirs("output", exist_ok=True)
    with open("output/scan_result.json", "w") as f:
        json.dump(report, f, indent=4)

    console.print("\n[bold green]Scan completed. Report saved to output/scan_result.json[/]")

if __name__ == "__main__":
    main()

