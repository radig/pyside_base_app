import os
from elixir import *

# dbdir=os.path.join(os.path.expanduser("~"),".pyrestaurant")
dbdir=os.path.join(os.getcwd(),"db")
dbfile=os.path.join(dbdir,"database.sqlite")

def initDB():
    # Make sure ~/.pyqtodo exists
    if not os.path.isdir(dbdir):
        os.mkdir(dbdir)
    # Set up the Elixir internal thingamajigs
    metadata.bind = "sqlite:///%s"%dbfile
    metadata.bind.echo = True
    setup_all()
    # And if the database doesn't exist: create it.
    if not os.path.exists(dbfile):
        create_all()
    # session.commit()