import os
# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
host = "mysql-test.cifxtwfwpb84.us-east-2.rds.amazonaws.com"
port = 3306
dbname = "mysql-test"
user = "admin"
password = "mysql-test"
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://" + user + ":" + password + "@" + host + ":" + port + "/" + dbname

# Uncomment the line below if you want to work with a local DB
# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
print(SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'

# Fix for the track modification error
SQLALCHEMY_TRACK_MODIFICATIONS = False
