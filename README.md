<h1>Hackpad</h1>

<p>
A simple <strong>5-key macropad</strong> built with a <strong>Seeed XIAO RP2040</strong> and a <strong>0.91&quot; OLED display</strong>.
</p>

<p>
Designed as a small, programmable USB keyboard.
</p>

<hr>

<h2>Features</h2>

<ul>
  <li>5 mechanical keys (direct GPIO wiring)</li>
  <li>0.91&quot; I²C OLED display</li>
  <li>USB HID keyboard</li>
  <li>Programmable macros</li>
  <li>Custom PCB (KiCad)</li>
</ul>

<hr>

<h2>Hardware</h2>

<ul>
  <li>Seeed XIAO RP2040</li>
  <li>5× MX-style switches</li>
  <li>0.91&quot; OLED display (GND–VCC–SCL–SDA pin order)</li>
</ul>

<hr>

<h2>Firmware</h2>

<ul>
  <li>Written in CircuitPython</li>
  <li>Acts as a USB keyboard</li>
  <li>Displays simple text/status on the OLED</li>
</ul>

<p>
Main firmware file:
</p>

<pre><code>firmware/main.py</code></pre>

<hr>

<h2>Installation</h2>

<ol>
  <li>Flash CircuitPython to the Seeed XIAO RP2040</li>
  <li>Copy required libraries to <code>CIRCUITPY/lib</code></li>
  <li>Copy <code>main.py</code> to the board</li>
</ol>

<hr>

<h2>PCB</h2>

<ul>
  <li>Designed in KiCad</li>
  <li>Keys wired directly to GPIO pins</li>
  <li>OLED connected over I²C (SDA/SCL)</li>
</ul>

<hr>

<h2>Case</h2>

<p>
The PCB is intentionally left exposed to improve accessibility, reduce complexity, and showcase the hardware design.
</p>

<p>
Leaving out a top enclosure simplifies assembly, allows easy debugging and modification, and keeps the focus on the PCB itself rather than a case.
</p>

<p>
The PCB fits inside a simple case and is secured using hot glue.
</p>

<img
  width="666"
  height="361"
  alt="Case preview"
  src="https://github.com/user-attachments/assets/9729e6d2-3e71-46c2-a7fe-441d8435d741"
/>

<hr>

<h2>My PCB</h2>

<img
  width="497"
  height="348"
  alt="PCB top view"
  src="https://github.com/user-attachments/assets/9d77fdde-b738-4634-8539-361a54ec4eef"
/>

<img
  width="585"
  height="371"
  alt="PCB 3D view"
  src="https://github.com/user-attachments/assets/b73d2abc-2d96-4391-bb70-4f8afdcdb1e1"
/>

<hr>

<h2>My Schematic</h2>

<img
  width="531"
  height="473"
  alt="Schematic"
  src="https://github.com/user-attachments/assets/2b0a1cdb-703e-4c30-adf5-f7f018193259"
/>
