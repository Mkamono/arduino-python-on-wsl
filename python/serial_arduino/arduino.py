import serial
import time


class arduino:
    def __init__(self, device: str, timeoutsec: float = 0.1) -> None:
        self.err: str = ""
        try:
            self.ser: serial.Serial = serial.Serial(
                device, timeout=timeoutsec)
        except Exception as e:
            self.err: str = f"connection failed: {e}"
            raise e

    def get_serial(self) -> str:
        while True:
            try:
                result_byte: bytes = self.ser.readline()
                result: str = result_byte.decode(encoding='utf-8')[:-2]  # 改行コード削除
            except Exception as e:
                self.err: str = f"read failed: {e}"
                raise e
            if result == "":
                time.sleep(0.1)
                continue
            else:
                return result

    def __del__(self) -> None:
        try:
            self.ser.close()
        except AttributeError:
            print("device not found")
            pass


if __name__ == "__main__":
    print("Enter = /dev/ttyACM0")
    device = input("devicefile = ")
    if device == "":
        device = "/dev/ttyACM0"
    cur_device = arduino(device)
    print("wait...")
    print(cur_device.get_serial())
