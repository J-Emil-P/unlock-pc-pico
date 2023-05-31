website_html = """<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-type" content="text/html;charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script>
            document.getElementById("Power_PC_time").value = Date.now()
            document.getElementById("Sign_in_time").value = Date.now()
    </script>
  </head>
  <body>
    <title>Pico PC control</title>
    <h1>Pico PC control</h1>
    <p>Powered by CircuitPython</p>
    <p>Made by <a href="https://example.com" target="_blank">Me :)</a> </p>
    <h1>Control the power of pc</h1>
    <p>The computer is currently:
    <span style="color: rgb(255, 67, 20);">Something</span></p>
    
    <br>
    
    <form accept-charset="utf-8" method="POST">
    <input type="password" id="Power_PC_input" name="Power_PC_input" placeholder="Password required">
    <input type="hidden" id="Power_PC_time" name="Power_PC_time">
    <button class="button" id="Power_PC_button" name="Power_PC_button" type="submit" value="on">Turn on PC</button></a></p></form>

    <br>

    <form accept-charset="utf-8" method="POST">
    <input type="password" id="Sign_in_input" name="Sign_in_input" placeholder="Password required">
    <input type="hidden" id="Sign_in_time" name="Sign_in_time">
    <button class="button" id="Sign_in_button" name="Sign_in_button" type="submit" value="on">Sign in</button></a></p></form>
    
    <br>
    
    <form accept-charset="utf-8" method="POST">
    <input type="password" id="Lock_input" name="Lock_input" placeholder="Password required">
    <input type="hidden" id="Lock_time" name="Lock_time">
    <button class="button" id="Lock_button" name="Lock_button" type="submit" value="on">Lock</button></a></p></form>
    
    <script>
        document.getElementById("Power_PC_time").value = Date.now()
        document.getElementById("Sign_in_time").value = Date.now()
        document.getElementById("Lock_time").value = Date.now()
    </script>
  </body>
</html>
"""
