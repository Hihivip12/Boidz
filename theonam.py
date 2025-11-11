import re
import time
import threading
import requests
import gc
import os
from datetime import datetime

def banner():
    os.system('clear')
    print(r""" """)

def get_uptime(start_time):
    elapsed = (datetime.now() - start_time).total_seconds()
    hours, rem = divmod(int(elapsed), 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

class KenjiToShiMessenger:
    def __init__(self, cookie):
        self.cookie = cookie
        self.user_id = self.extract_user_id()
        self.fb_dtsg = self.get_fb_dtsg()
        self.valid = self.user_id is not None and self.fb_dtsg is not None

    def extract_user_id(self):
        match = re.search(r"c_user=(\d+)", self.cookie)
        if not match:
            print("[!] Cookie không hợp lệ (không có c_user)")
            return None
        return match.group(1)

    def get_fb_dtsg(self):
        try:
            headers = {'Cookie': self.cookie, 'User-Agent': 'Mozilla/5.0'}
            res = requests.get('https://mbasic.facebook.com/profile.php', headers=headers)
            if 'checkpoint' in res.url or 'login' in res.url:
                print(f"[!] Cookie checkpoint hoặc hết hạn: {self.user_id}")
                return None
            token = re.search(r'name="fb_dtsg" value="(.*?)"', res.text)
            if not token:
                print(f"[!] Không tìm thấy fb_dtsg: {self.user_id}")
                return None
            return token.group(1)
        except Exception as e:
            print(f"[!] Lỗi khi lấy fb_dtsg: {e}")
            return None

    def send_message(self, recipient_id, message):
        if not self.valid:
            print(f"[!] Bỏ qua vì tài khoản không hợp lệ: {self.user_id}")
            return False
        try:
            ts = int(time.time() * 1000)
            data = {
                'thread_fbid': recipient_id,
                'action_type': 'ma-type:user-generated-message',
                'body': message,
                'client': 'mercury',
                'author': f'fbid:{self.user_id}',
                'timestamp': ts,
                'source': 'source:chat:web',
                'offline_threading_id': str(ts),
                'message_id': str(ts),
                '__user': self.user_id,
                '__a': '1',
                'fb_dtsg': self.fb_dtsg
            }
            headers = {
                'Cookie': self.cookie,
                'User-Agent': 'python-http',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            res = requests.post('https://www.facebook.com/messaging/send/', data=data, headers=headers)
            if res.status_code != 200 or 'error' in res.text:
                print(f"[!] Lỗi gửi tới {recipient_id} bởi {self.user_id}, thử refresh fb_dtsg...")
                # refresh fb_dtsg khi lỗi
                self.fb_dtsg = self.get_fb_dtsg()
                return False
            return True
        except Exception as e:
            print(f"[!] Exception gửi tới {recipient_id} bởi {self.user_id}: {e}")
            # thử refresh lại fb_dtsg
            self.fb_dtsg = self.get_fb_dtsg()
            return False

    def clear_memory(self):
        # reset biến nhưng vẫn giữ cookie để dùng lại
        self.fb_dtsg = None
        gc.collect()
        self.fb_dtsg = self.get_fb_dtsg()
        print(f"[+] Đã dọn RAM & refresh fb_dtsg cho {self.user_id}")

lock_ngon = threading.Lock()
messengers_ngon = []
ids_ngon = []
messages_per_id = {}
threads_info = {}
current_delay = 1.0
default_message = ""

def spam_worker(messenger: KenjiToShiMessenger):
    success = 0
    fail = 0
    idx = 0
    last_clear = time.time()
    while True:
        with lock_ngon:
            if not ids_ngon:
                time.sleep(1)
                continue
            box_id = ids_ngon[idx % len(ids_ngon)]
            idx += 1
            msg = messages_per_id.get(box_id, default_message)
            delay = current_delay

        try:
            ok = messenger.send_message(box_id, msg)
            if ok:
                success += 1
                status = "OK"
            else:
                fail += 1
                status = "FAIL (retry)"
        except Exception as e:
            fail += 1
            status = f"Lỗi: {e}"

        uptime = get_uptime(threads_info.get(messenger.user_id, {}).get('start', datetime.now()))
        print(f"[{messenger.user_id}] → {box_id} {status} | Uptime: {uptime} | OK: {success} | FAIL: {fail}".ljust(120), end='\r')

        # tự động dọn RAM sau 5 phút
        if time.time() - last_clear > 300:
            messenger.clear_memory()
            last_clear = time.time()

        time.sleep(delay)
        gc.collect()

def input_loop():
    global current_delay, default_message
    while True:
        cmd = input("\n> ").strip()
        if cmd == "exit":
            print("[*] Thoát...")
            break
        elif cmd == "tab":
            with lock_ngon:
                print("\n--- DANH SÁCH ĐANG CHẠY ---")
                print(f"ID Box: {', '.join(ids_ngon) if ids_ngon else 'Không có'}")
                if messengers_ngon:
                    print("Cookie:")
                    for ms in messengers_ngon:
                        uptime = get_uptime(threads_info[ms.user_id]['start'])
                        print(f" - {ms.user_id} | Uptime: {uptime}")
                else:
                    print("Không có cookie nào.")
        elif cmd == "ram":
            with lock_ngon:
                for ms in messengers_ngon:
                    ms.clear_memory()
            print("[*] Đã dọn RAM thủ công cho tất cả account.")

def main():
    banner()
    print(r"""
[🌸]=====================================[🌸]
|     🚀 TOOL TREO MESS 🚀   |
|        Admin:Nguyễn Đức Anh  
         Số zalo:0965116136
         facebook:https://www.facebook.com/profile.php?id=100001925681712   |
[🌸]=====================================[🌸]
""")

    # Đọc cookie từ file
    cookie_file = input("[!] Nhập Tên File Chứa Cookies\n> ")
    try:
        with open(cookie_file, 'r', encoding='utf-8') as f:
            cookies = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[×] Lỗi đọc file cookie: {e}")
        return

    ids = input("[!] Nhập ID box (phân cách bằng dấu phẩy):\n> ").split(',')
    delay = float(input("[!] Delay Giữa Mỗi Tin Nhắn (Giây):\n> "))
    file_name = input("[!] File Nội Dung Tin Nhắn:\n> ")

    with open(file_name, 'r', encoding='utf-8') as f:
        global default_message
        default_message = f.read().strip()

    global current_delay
    current_delay = delay

    with lock_ngon:
        for c in cookies:
            try:
                ms = KenjiToShiMessenger(c)
                messengers_ngon.append(ms)
                threads_info[ms.user_id] = {'start': datetime.now()}
                print(f"[✓] Cookie OK: {ms.user_id}")
                threading.Thread(target=spam_worker, args=(ms,), daemon=True).start()
            except Exception as e:
                print(f"[×] Cookie lỗi: {e}")

        for box_id in ids:
            box_id = box_id.strip()
            if box_id:
                ids_ngon.append(box_id)

    threading.Thread(target=input_loop, daemon=True).start()
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()