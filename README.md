Hackpad

A simple 5-key macropad built with a Seeed XIAO RP2040 and a 0.91" OLED display.

Designed as a small, programmable USB keyboard.

Features

5 mechanical keys (direct GPIO wiring)

0.91" I²C OLED

USB HID keyboard

Programmable macros

Custom PCB (KiCad)

Hardware

Seeed XIAO RP2040

5× MX-style switches

0.91" OLED display (GND–VCC–SCL–SDA pin order)

Firmware

Written in CircuitPython

Acts as a USB keyboard

Displays simple text/status on the OLED

Main file:

firmware/main.py

Install

Flash CircuitPython to the Seeed XIAO RP2040

Copy required libraries to CIRCUITPY/lib

Copy main.py to the board

PCB

Designed in KiCad

Keys wired directly to GPIO pins

OLED connected over I²C (SDA/SCL)
My PCB
<img width="492" height="338" alt="Screenshot 2025-12-26 at 4 35 13 PM" src="https://github.com/user-attachments/assets/775f11c6-411a-41cf-bd79-a34932bc01eb" />
My Schematic

<img width="531" height="473" alt="Screenshot 2025-12-26 at 6 34 37 PM" src="https://github.com/user-attachments/assets/2b0a1cdb-703e-4c30-adf5-f7f018193259" />
