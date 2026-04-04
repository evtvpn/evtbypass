#!/usr/bin/env python3
# Launcher for EVT Bypass .so file

import sys

try:
    # Import the compiled module
    from evtbypass import start_process
    print("[+] Module loaded successfully!")
    start_process()
except ImportError as e:
    print(f"[-] Cannot import evtbypass.so: {e}")
    print("[!] Make sure evtbypass.so is in the same directory")
except Exception as e:
    print(f"[-] Error: {e}")
