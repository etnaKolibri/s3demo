from app import app
from flask import Flask, render_template, request, redirect
from werkzeug.security import secure_filename


@app.route("/", methods=["POST"])
def upload_file():

	# A
    if "user_file" not in request.files:
        return "No user_file key in request.files"

	# B
    file_to_upload = request.files["user_file"]

    """
        These attributes are also available

        file_to_upload.filename               # The actual name of the file
        file_to_upload.content_type
        file_to_upload.content_length
        file_to_upload.mimetype

    """

	# C.
    if file_to_upload.filename == "":
        return "Please select a file"

	# D.
    if file_to_upload and allowed_file(file_to_upload.filename):
        file_to_upload.filename = secure_filename(file_to_upload.filename)
        output = upload_file_to_s3(file_to_upload, app.config["S3_BUCKET"])
        return str(output)

    else:
        return redirect("/")