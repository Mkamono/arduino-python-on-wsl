from sqlalchemy import create_engine

class BaseEngine(object):
    def __init__(self, datapath) -> None:
        # username = 'username'
        # password = 'password'
        # hostname = 'localhost'
        # dbname = 'db_server'
        self.engine = create_engine(f'sqlite:///{datapath}')
