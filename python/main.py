import os
import time
from datetime import datetime, timedelta, timezone
from serial_arduino.arduino import arduino
from sqlitemod.migrate import Migration
from sqlitemod.base_engine import BaseSession
from sqlitemod.models import Result


class Resultcls(BaseSession):
    def __init__(self, datapath) -> None:
        super().__init__(datapath)

    def create(self, msg: str) -> None:
        """insert database

        Args:
            msg (str): db:message
        """
        JST: timezone = timezone(timedelta(hours=+9), 'JST')
        temp: Result = Result(message=msg, created=datetime.now(JST))
        print(f"message:{temp.message}, created={temp.created}")
        self.session.add(temp)
        self.session.commit()


if __name__ == '__main__':
    # const value
    dbpath_relative: str = './results.sqlite3'
    devicefilepath: str = "/dev/ttyACM0"
    num: int = -1  # default: -1
    second: int = -1  # default: -1
    start = time.time()

    base = os.path.dirname(os.path.abspath(__file__))
    datapath = os.path.normpath(
        os.path.join(base, dbpath_relative))

    Migration(datapath).result()

    cli: Resultcls = Resultcls(datapath)

    cur_device: arduino = arduino(devicefilepath)

    while True:
        try:
            message: str = cur_device.get_serial()
            cli.create(message)
        except KeyboardInterrupt:
            break
        except:
            cli.create("connection err")
            pass
        finally:
            if num != -1:
                num: int = num - 1
                if num <= 0:
                    print("num completed")
                    break
            if second != -1:
                if time.time() - start >= second:
                    print("time completed")
                    break
    del cli
    del cur_device
    print("finished")
