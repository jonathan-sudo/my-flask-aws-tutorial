import os
# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ec2-user:26AwsDR5e3Y9hkLOgYrr@flask-aws-db.cifxtwfwpb84.us-east-2.rds.amazonaws.com:3306/flask-aws-db'

# Uncomment the line below if you want to work with a local DB
# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'

# Fiw for the track modification error
SQLALCHEMY_TRACK_MODIFICATIONS = False
