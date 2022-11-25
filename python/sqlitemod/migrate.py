from sqlitemod.base import BaseEngine
from sqlitemod.models import Base


class Migration(object):
    def __init__(self, datapath) -> None:
        self.e = BaseEngine(datapath).engine

    def result(self) -> None:
        Base.metadata.create_all(self.e)
