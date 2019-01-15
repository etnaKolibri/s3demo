from flask import Flask

app = Flask(__name__)
app.config.from_object("flask_s3_upload.config")

if __name__=="__main__":
    app.run(debug=True)

