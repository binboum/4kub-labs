from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def lab():
    return """<html>
   <head>
      <title>4KUB</title>
      <link rel="shortcut icon" href="https://www.supinfo.com/favicon.png">
   </head>
   <body align="center">
      <img src="https://www.supinfo.com/images/fr/supinfologo.png"> 
      <p>Version : 1.0.0</p>
      <p>Hostname : {hostname}</p>
   </body>
</html>""".format(hostname=os.getenv('HOSTNAME'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)