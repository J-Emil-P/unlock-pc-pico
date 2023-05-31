# SPDX-FileCopyrightText: 2022 Liz Clark for Adafruit Industries
# SPDX-License-Identifier: MIT
# Modified by Emil P 2023

import os
import time
import ipaddress
import wifi
import socketpool
import board
import microcontroller
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.methods import HTTPMethod
from adafruit_httpserver.mime_type import MIMEType
from website import website_html

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_sw import KeyboardLayout
from adafruit_hid.keycode import Keycode

print(os.getenv("settings_found_message")) # a simple varible with "Settings found..." as the text to make sure it can find settings
#  connect to network
print("Connecting to WiFi")

#  set static IP address
ipv4 =  ipaddress.IPv4Address("192.168.68.96")
netmask =  ipaddress.IPv4Address("255.255.255.0")
gateway =  ipaddress.IPv4Address("192.168.68.1")
wifi.radio.set_ipv4_address(ipv4=ipv4,netmask=netmask,gateway=gateway)
#  connect to your SSID
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)

#  route default static IP
@server.route("/")
def base(request: HTTPRequest):  # pylint: disable=unused-argument
    #  serve the HTML string
    #  with content type text/html
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(website_html)

#  if a button is pressed on the site
@server.route("/", method=HTTPMethod.POST)
def buttonpress(request: HTTPRequest):
    raw_text = request.raw_request.decode("utf8") # get the raw text
    #print(raw_text) #debug
    
    form_data = raw_text.splitlines()[14] #get line 15
    print("LINE 15:", form_data)
    
    global old_form_data 
    
    if "old_form_data" in locals():
        if old_form_data == form_data:
            print("Old data")
        else:
            if "Power_PC_button" in form_data and os.getenv("WEB_PIN_CODE") in form_data:
                print("User powered pc")

            if "Sign_in_button" in form_data and os.getenv("WEB_PIN_CODE") in form_data:
                print("User signed in")
                
                key_pin_array = []
                control_key = Keycode.SHIFT
                time.sleep(1)
                keyboard = Keyboard(usb_hid.devices)
                time.sleep(1)
                keyboard_layout = KeyboardLayout(keyboard)
                
                time.sleep(5)
                keyboard_layout.write("E")
                time.sleep(5)
                keyboard_layout.write(os.getenv("COMPUTER_PIN_CODE"))
                
                time.sleep(1) #this part is for when text box was not selected
                ENTER_KEY = 0x28 
                keyboard.press(ENTER_KEY)
                time.sleep(0.5)
                keyboard.release_all()
                time.sleep(3)
                keyboard_layout.write(os.getenv("COMPUTER_PIN_CODE"))
                
            if "Lock_button" in form_data and os.getenv("WEB_PIN_CODE") in form_data:
                print("User locked PC")
                
                key_pin_array = []
                control_key = Keycode.SHIFT
                time.sleep(1)
                keyboard = Keyboard(usb_hid.devices)
                time.sleep(1)
                keyboard_layout = KeyboardLayout(keyboard)
                
                WINDOWS = 0xe3
                L_Button = 0x0f
                keyboard.press(WINDOWS)
                time.sleep(0.3)
                keyboard.press(L_Button)
                time.sleep(0.3)
                keyboard.release_all()
                
            old_form_data = form_data
    else:
        old_form_data = form_data
        print("No old_form_data found")
    
    print()
        
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(website_html)

print("starting server..")
# startup the server
try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s:80 \n" % wifi.radio.ipv4_address)
except OSError as error:
    print(error)
    time.sleep(5)
    print("restarting..")
    microcontroller.reset()
#  if the server fails to begin, restart the pico w


while True:
    try:
        # Can do something useful here, this is just a loop

        server.poll() # Process any waiting requests
    except OSError as error:
        print(error)
        time.sleep(5)
        print("restarting..")
        microcontroller.reset()