
import psutil
import time
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.layout import Layout

console = Console()

def get_cpu_info():
    return {
        "usage": psutil.cpu_percent(percpu=True),
        "total": psutil.cpu_percent(),
        "freq": psutil.cpu_freq().current,
        "cores": psutil.cpu_count(logical=True)
    }

def create_ui():
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3)
    )

    layout["main"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )

    return layout

def render(cpu_data):
    layout = create_ui()

    # Header
    layout["header"].update(
        Panel("🚀 FUTURISTIC CPU MONITOR", style="bold cyan")
    )

    # CPU Overview
    overview = Table.grid(expand=True)
    overview.add_column(justify="center")

    overview.add_row(f"[bold green]Total Usage:[/bold green] {cpu_data['total']}%")
    overview.add_row(f"[bold yellow]Frequency:[/bold yellow] {cpu_data['freq']:.2f} MHz")
    overview.add_row(f"[bold magenta]Cores:[/bold magenta] {cpu_data['cores']}")

    layout["left"].update(
        Panel(overview, title="🧠 CPU Overview", border_style="green")
    )

    # Per-core usage bars
    progress = Progress(
        TextColumn("[bold blue]Core {task.fields[core]}"),
        BarColumn(bar_width=None),
        TextColumn("[bold white]{task.percentage:>3.0f}%"),
    )

    for i, usage in enumerate(cpu_data["usage"]):
        progress.add_task("", total=100, completed=usage, core=i)

    layout["right"].update(
        Panel(progress, title="⚡ Per-Core Usage", border_style="cyan")
    )

    # Footer
    layout["footer"].update(
        Panel("Press CTRL+C to exit", style="bold red")
    )

    return layout

def main():
    with Live(console=console, refresh_per_second=2) as live:
        while True:
            cpu_data = get_cpu_info()
            live.update(render(cpu_data))
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting Futuristic Monitor...[/bold red]")
