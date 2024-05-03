# ble-morsecode-neokey
Bluetooth One Hand Morse Code Keyboard

![Screenshot](ble-mc-neo-1.jpeg)

This wireless four key keyboard allows for typing on laptops, phones and tablets. This subtle interface is CircuitPython based. It uses morse code '.' and '-' with a lookup table to translate characters.

<pre>
Features:
* Key1: '.'    # dot
* Key2: '-'    # dash
* Key3: ' '    # will do a space between words or show the morse code buffer contents
* Key4: *SEND* # translates morse code sequence to ascii sends ascii over BLE
</pre>

![Screenshot](ble-mc-neo-7.jpeg)


The morse code to ascii character is from Crysknife's excellent [morsePico project](https://github.com/Crysknife007/morsePico/blob/main/code.py). 

![Screenshot](ble-mc-neo-3.jpeg)

Bill of Materials (main components):
* [Adafruit LED Glasses Driver - nRF52840](https://www.adafruit.com/product/5217)
* [NeoKey 1x4 QT I2C](https://www.adafruit.com/product/4980)
* [Lithium Ion Polymer Battery 420mAh](https://www.adafruit.com/product/4236)

Tested with Circuitpython 9. Design files are from FreeCAD with STL and STEP available. 

![Screenshot](ble-mc-neo-4.png)

![Screenshot](ble-mc-neo-2.jpeg)

![Screenshot](ble-mc-neo-5.png)
