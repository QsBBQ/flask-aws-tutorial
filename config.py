# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
import os
db_name = os.environ['RDS_DB_NAME']
db_user = os.environ['RDS_USERNAME']
db_password = os.environ['RDS_PASSWORD']
db_host = os.environ['RDS_HOSTNAME']
db_port = os.environ['RDS_PORT']

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@flask-demo.co1s6zhqgeco.us-west-2.rds.amazonaws.com:3306/demodb'.format(db_user, db_password)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(db_user, db_password, db_host, db_port, db_name)
# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
