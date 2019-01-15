import boto3, botocore
from config import S3_BUCKET, S3_KEY, S3_SECRET

s3 = boto3.client(

    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET

)

"""

    Upload file

"""
def upload_file_to_s3(file, bucket_name, acl="publick-read"):
    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )
    
    except Exception as e:
        print("S3 Upload Failed: ", e)
        return e


    return "{}{}".format(app.config["S3_LOCATION"], file.filename)  