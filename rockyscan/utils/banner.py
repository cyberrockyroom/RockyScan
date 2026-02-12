import random
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# -----------------------------
# Metadata
# -----------------------------
VERSION = "2.0.0"
AUTHOR = "Rocky Patel"

# Smooth gradient palettes (NO chaos)
GRADIENTS = [
    ["#ff004c", "#ff7a00", "#ffe600", "#3cff00", "#00ffe1", "#007bff"],
    ["#00f5ff", "#008cff", "#6a00ff", "#d000ff"],
    ["#00ff9c", "#00cfff", "#007bff"],
    ["#ff6a00", "#ff004c", "#b300ff"],
]

def gradient_text(ascii_text: str) -> Text:
    colors = random.choice(GRADIENTS)
    text = Text()
    step = len(colors)
    i = random.randint(0, step - 1)

    for char in ascii_text:
        if char == "\n":
            text.append(char)
        else:
            text.append(char, style=f"bold {colors[i % step]}")
            i += 1
    return text


def show_banner():
    ascii_logo = pyfiglet.figlet_format(
        "ROCKYSCAN",
        font="slant"
    )

    banner = gradient_text(ascii_logo)

    # 🔹 Panel ONLY for logo
    panel = Panel(
        banner,
        border_style="bright_cyan",
        subtitle="[bold cyan]Unified Network Scanning Framework[/bold cyan]",
        subtitle_align="center"
    )

    console.print(panel)

    # 🔹 Version & Author BELOW the banner (as you want)
    console.print(
        f"[cyan]Version:[/] {VERSION}    "
        f"[cyan]Author:[/] {AUTHOR}",
        justify="center"
    )

    console.print(
        "\n[bold red]⚠ WARNING:[/bold red] "
        "Use only on systems you own or have permission\n"
    )
