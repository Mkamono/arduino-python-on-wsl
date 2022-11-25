# このリポジトリは
windows機でローカル環境を極力汚さずにマイコン開発をするテンプレートです。
[Qiitaの記事](https://qiita.com/KMNMKT/items/952a7de4d2541c2570a2)を投稿していますので参照してください。
# 使い方
```powershell
#wsl起動済みpowershell
usbipd wsl attach --busid <devicepid>
```
```bash
#wsl
sudo chmod 777 /dev/<devicepath> #権限付与
sudo apt install nptdate
sudo ntpdate ntp.nict.jp # 時刻合わせ

sudo pip install -r requirement.txt
sudo python3 python/main.py
```