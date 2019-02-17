# Su dung cac thu vien can thiet
# Su dung PushBullet de phat thong bao ve may tinh hoac dien thoai thong minh
import requests


def ThongBao(title, msg):
    headers = {
        'Access-Token': 'o.J1figRj0Y1ZLaJVd6eDyi6Nfr0gt3pbM',
        'Content-Type': 'application/json',
    }
    response = requests.post(
        'https://api.pushbullet.com/v2/pushes',
        headers=headers, data=(
            '{"type":"note","title":"' + (title) + '","body":" ' + (msg) + ' "}').encode("utf-8")
    )
