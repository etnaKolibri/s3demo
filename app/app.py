from flask import Flask, render_template, request, redirect
from werkzeug.security import secure_filename

app = Flask(__name__)
app.config.from_object("flask_s3_upload.config")

if __name__=="__main__":
    app.run(debug=True)

