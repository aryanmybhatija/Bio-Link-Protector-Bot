import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="author" content="Team Sonu" />
    <meta name="keywords" content="Bio Restrictor, Bio protector,  Bio Link Protector" />
    <meta name="description" content="Botzone Save Restricted Bot Service." />
    <meta property="og:description" content="TeamSonu1 Bio Link Protector.">	  
    <title> Save Restricted Bot - By ꧁•⊹٭𝚂𝚘𝚗𝚞٭⊹•꧂</title>
    <link rel="icon" type="image/x-icon" href="https://myappme.shop/img/file_224.jpg" type="image/x-icon" />
  </head>

   <body>
   <center>
       <img src="https://myappme.shop/img/file_224.jpg" alt="Bio Link Restrictor" style="width:50px;height:50px;border-radius: 100px;">
       <h1 class="font-bold" id="Bio Link Restrictor">Bio Link Protector </h1>
       <p class="font-bold" id="Bot successfully">Bot successfully Running...</p>
   </center>
   </body>
<center> 
    <img src="https://myappme.shop/img/file_225.jpg" height="200" width="200" style="border-radius: 12px;"/>
    <br>
    <a href="https://t.me/Team_Sonu1" target="_blank"><img align="center" src="https://myappme.shop/img/file_227.jpg" alt="Star" height="200" width="200" /></a>
</p>
</center>
<br>
<footer class="bg-blue-500 font-bold text-white text-center py-3 mt-5">
<center>
        Powered By <a href="https://t.me/Sonuporsa" target="_blank"> ꧁•⊹٭𝚂𝚘𝚗𝚞٭⊹•꧂</a>
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2025 Bio Link Protector. All rights reserved.
            </p></center>
        </div>
    </footer>
<style>
    body { 
        background: antiquewhite;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
