<h1>Hackpad<h1/>

A simple 5-key macropad built with a Seeed XIAO RP2040 and a 0.91" OLED display.

Designed as a small, programmable USB keyboard.

<h1>Features<h1/>

5 mechanical keys (direct GPIO wiring)

0.91" I²C OLED

USB HID keyboard

Programmable macros

Custom PCB (KiCad)

<h1>Hardware<h1/>

Seeed XIAO RP2040

5× MX-style switches

0.91" OLED display (GND–VCC–SCL–SDA pin order)

<h1>Firmware<h1/>

Written in CircuitPython

Acts as a USB keyboard

Displays simple text/status on the OLED

Main file:

firmware/main.py

<h1>Install<h1/>

Flash CircuitPython to the Seeed XIAO RP2040

Copy required libraries to CIRCUITPY/lib

Copy main.py to the board

<h1>PCB<h1/>

Designed in KiCad

Keys wired directly to GPIO pins

OLED connected over I²C (SDA/SCL)


<h1>My PCB<h1/>
  
<img width="497" height="348" alt="Screenshot 2025-12-26 at 7 05 10 PM" src="https://github.com/user-attachments/assets/9d77fdde-b738-4634-8539-361a54ec4eef" />

<img width="585" height="371" alt="Screenshot 2025-12-26 at 6 59 59 PM" src="https://github.com/user-attachments/assets/b73d2abc-2d96-4391-bb70-4f8afdcdb1e1" />


<h1>My Schematic<h1/>

<img width="531" height="473" alt="Screenshot 2025-12-26 at 6 34 37 PM" src="https://github.com/user-attachments/assets/2b0a1cdb-703e-4c30-adf5-f7f018193259" />
