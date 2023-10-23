# unlock-pc-pico
Uses raspberry pi pico w with circuitpython to unlock/lock your pc with another device (over wifi)

Only **tested** with Swedish keyboard, circuit python 8.0.3 and pin code as log in

**SECURITY IS NOT GUARANTEED, USE AT YOUR OWN RISK!**

# Using it!
## warnings and disclaimers
* Only use on your own wifi
* Do NOT use on wifi networks without a password
* Bad actors can control your computer if they get physical or digital (via wifi) access
* Do NOT port forward the pico to the internet
## requires:
Circuit python pico w: https://circuitpython.org/board/raspberry_pi_pico_w/
Thonny Python: https://thonny.org/ 
## Config
1. Install circuit python (link in requires section)
2. Download repository zip file
3. Unzip files
4. Drag files from the code to your pico w files
5. Edit settings.toml with password etc
6. Run the code by opening web-code.py in Thonny **(tested and recomended for first run)** or rename it to main.py to automaticly start code when inserted in pc (untested).
7. Open ip adress in chrome (on your phone on same wifi) sent in shell (Inside thonny)
