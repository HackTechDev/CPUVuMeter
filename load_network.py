#!/usr/bin/python3

import psutil
import time

def get_network_load(interval=1):
    """Calculate network load in Kb/s."""
    # Get initial network I/O stats
    net_io_start = psutil.net_io_counters()

    # Sleep for the interval
    time.sleep(interval)

    # Get network I/O stats after the interval
    net_io_end = psutil.net_io_counters()

    # Calculate the difference and convert bytes to kilobytes
    bytes_sent = net_io_end.bytes_sent - net_io_start.bytes_sent
    bytes_recv = net_io_end.bytes_recv - net_io_start.bytes_recv

    kb_sent = bytes_sent / 1024
    kb_recv = bytes_recv / 1024

    return kb_sent, kb_recv

def main():
    while True:
        kb_sent, kb_recv = get_network_load()
        print(f"Kb sent: {kb_sent:.2f} Kb/s | Kb received: {kb_recv:.2f} Kb/s")
        time.sleep(1)  # Adjust the sleep time if needed

if __name__ == "__main__":
    main()
