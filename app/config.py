import os

S3_BUCKET= os.environ.get("S3_BUCKET_NAME")
S3_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION  = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY  = os.urandom(32)
DEBUG  = True
PORT = 5000


export S3_BUCKET=" baket nameE"
export S3_KEY="aws key"
export S3_SECRET_ACCESS_KEY="tanja"

