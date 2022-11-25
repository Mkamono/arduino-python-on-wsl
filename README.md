# このリポジトリは
windows機でローカル環境を極力汚さずにマイコン開発をするテンプレートです。
# 使い方
```powershell:powershell:administrator
#wsl起動済み
usbipd wsl attach --busid 2-1
```
```bash:WSL
sudo chmod 777 /dev/ttyACM0 #権限付与
sudo apt install nptdate
sudo ntpdate ntp.nict.jp # 時刻合わせ

sudo pip install -r requirement.txt
sudo python3 python/main.py
```