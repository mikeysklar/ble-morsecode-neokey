import board                                                                                                   
import time
import digitalio                                                                                               
from adafruit_hid.keyboard import Keyboard                                                                     
from adafruit_hid.keycode import Keycode                                                                       
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS                                                   
import adafruit_ble                                                                                            
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement                                     
from adafruit_ble.services.standard.hid import HIDService                                                      
from micropython import const
from adafruit_neokey.neokey1x4 import NeoKey1x4

# Enable the ble radio                                                                                         
ble = adafruit_ble.BLERadio()                                                                                  
                                                                                                               
# create HID Service                                                                                           
hid = HIDService()                                                                                             
# Create Advertisement                                                                                         
advertisement = ProvideServicesAdvertisement(hid)                                                              
                                                                                                               
# Create Keyboard Object                                                                                       
k = Keyboard(hid.devices)                                                                                      
kl = KeyboardLayoutUS(k)                                                                                       

# use default I2C bus
i2c_bus = board.I2C()

# Create a NeoKey object
neokey = NeoKey1x4(i2c_bus, addr=0x30)

#  states for key presses
key_0_state = False
key_1_state = False
key_2_state = False
key_3_state = False

morsecode = ""

MorseCodes = {
    'a'  : '.-',
    'b'  : '-...',
    'c'  : '-.-.',
    'd'  : '-..',
    'e'  : '.',
    'f'  : '..-.',
    'g'  : '--.',
    'h'  : '....',
    'i'  : '..',
    'j'  : '.---',
    'k'  : '-.-',
    'l'  : '.-..',
    'm'  : '--',
    'n'  : '-.',
    'o'  : '---',
    'p'  : '.--.',
    'q'  : '--.-',
    'r'  : '.-.',
    's'  : '...',
    't'  : '-',
    'u'  : '..-',
    'v'  : '...-',
    'w'  : '.--',
    'x'  : '-..-',
    'y'  : '-.--',
    'z'  : '--..',
    '0'  : '-----',
    '1'  : '.----',
    '2'  : '..---',
    '3'  : '...--',
    '4'  : '....-',
    '5'  : '.....',
    '6'  : '-....',
    '7'  : '--...',
    '8'  : '---..',
    '9'  : '----.',
    '.'  : '.-.-.-',
    ','  : '--..--',
    '?'  : '..--..', 
    '\'' : '.----.', 
    '!'  : '-.-.--',
    '/'  : '-..-.',
    '('  : '-.--.',
    ')'  : '-.--.-',
    '&'  : '.-...',
    ':'  : '---...',
    ';'  : '-.-.-.',
    '='  : '-...-',
    '+'  : '.-.-.',
    '-'  : '-....-',
    '_'  : '..--.-',
    '@'  : '.--.-.',
    '"'  : '.-..-.',
    '*'  : '...-.',
    '\\' : '-.-.-',
    '%'  : '---.-',
    '#'  : '--.-.',
    '|'  : '--.-.-',
    '^'  : '......',
    '~'  : '.---..',
    '`'  : '-..-.-',
    '$'  : '...-..',
    '['  : '.--..',
    ']'  : '.--..-',
    '{'  : '.--.-',
    '}'  : '.--.--',
    '<'  : '-.---',
    '>'  : '-.----',
    ' '  : '..--',
    '\n' : '.-.-',
    '\b' : '----'
}

# Lookup the right character in the dictionary
def keycodeLookup(keystring):

  # For every item in the dictionary
  for c in MorseCodes:

    # If this is the keycode we are looking for
    if MorseCodes[c] == keystring:

      # Return the matching keycode
      return c

  # If we don't find anything return an empty string
  return ''

c = ''

while True:                                                                                                    
  ble.start_advertising(advertisement)  # Start advertising                                                  
  while not ble.connected:  # Wait for connection                                                            
    pass                                                                                                   
                                                                                                               
  while ble.connected:                                                                                       
    #  switch debouncing
    #  also turns off NeoPixel on release
    if not neokey[0] and key_0_state:
      key_0_state = False
      neokey.pixels[0] = 0x0
    if not neokey[1] and key_1_state:
      key_1_state = False
      neokey.pixels[1] = 0x0
    if not neokey[2] and key_2_state:
      key_2_state = False
      neokey.pixels[2] = 0x0
    if not neokey[3] and key_3_state:
      key_3_state = False
      neokey.pixels[3] = 0x0

    if neokey[0] and not key_0_state:
      neokey.pixels[0] = 0xFF0000
      c = keycodeLookup(morsecode)
      kl.write(c)
      morsecode = ''
      c = ''
      print("\n", end="")
      key_0_state = True

    if neokey[1] and not key_1_state:
      neokey.pixels[1] = 0xFFFF00
      key_1_state = True
      morsecode += ' '
      print(" ", end="")
      kl.write(morsecode)
      morsecode = ''

    if neokey[2] and not key_2_state:
      neokey.pixels[2] = 0x00FF00
      morsecode += '-'
      print("-", end="")
      key_2_state = True

    if neokey[3] and not key_3_state:
      neokey.pixels[3] = 0x00FFFF
      morsecode += '.'
      print(".", end="")
      key_3_state = True

    time.sleep(0.03)
