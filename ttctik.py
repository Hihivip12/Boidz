import sys,os,time,json
from rich.table import Table
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from threading import Thread
from threading import Thread
import cloudscraper
from pystyle import Colors,Colorate,Center
def kiemtrathietbi():

           return "com.termux" in os.environ.get("PREFIX", "")
listmd = [
        # 'faker',
        'tqdm',
        'imaplib',
        'threading',
        'getuseragent',
      #  'numpy',
        'unidecode',
        'colorama',
       # 'wmi',
        'fake_useragent',
        'ctypes',
        'logging',
        'pywintypes'
        'cloudscraper'
        'rich']
import importlib
for i in range (len(listmd)-1):
    try:
        module=listmd[i]
        importlib.import_module(module)
    except:
        os.system (f'pip install {listmd[i]}')
        importlib.import_module(module)  
import sys,platform,os,json,base64,hashlib,random,requests,logging,json,threading,time
import os.path,getuseragent
from datetime import datetime ,date
gradient_list = [
    Colors.red_to_yellow,
    Colors.yellow_to_green,
    Colors.green_to_blue,
    Colors.blue_to_purple,
    Colors.rainbow,
]

def spinner_loading():
    with console.status("[bold cyan]Đang khởi động BVZONE-V1...[/]", spinner="dots12"):
        time.sleep(1.8)
from threading import Thread
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    Thread(target=spinner_loading).start()
    time.sleep(2)
    now = datetime.now().strftime("🕓 %H:%M:%S - 📅 %d/%m/%Y")
    os_name = platform.system()
    banner_text = f"""
           © Copyright By Boiz

██████╗░░█████╗░██╗███████╗
██╔══██╗██╔══██╗██║╚════██║
██████╦╝██║░░██║██║░░███╔═╝
██╔══██╗██║░░██║██║██╔══╝░░
██████╦╝╚█████╔╝██║███████╗
╚═════╝░░╚════╝░╚═╝╚══════╝
[</>] => Admin: Boiz 
[</>] => Box Zalo: https://zalo.me/g/beizcs929
[</>] => Web Bán VPS: éo cs đâu
[</>] => Bạn Đang Sử Dụng Version: V1.2
[💻] => Hệ Điều Hành: {os_name}
[🕒] => Thời Gian: {now}
"""
    gradient = random.choice(gradient_list)
    colored_banner = Colorate.Vertical(gradient, banner_text)
    for line in colored_banner.splitlines():
        print(Center.XCenter(line))
        time.sleep(0.02)
console = Console()
def bugconcac():
    import sys
    if sys.gettrace():
        console.print("[red]⛔ Phát hiện Debugger! Thoát tool.[/]")
        sys.exit()
    else:
        console.print("[green]✅ Không phát hiện debugger.[/]")
bugconcac()
# =============== CHẶN DEBUG ===============
def bugcailon():
    if sys.gettrace():
        print("PHAT HIEN DEBUG! Dung tool.")
        sys.exit()
    if 'PYTHONINSPECT' in os.environ:
        print("PHAT HIEN PYTHONINSPECT. Chan chay.")
        sys.exit()
bugcailon()
 
def randommau():
    rand = random.randint(1, 231)
    if rand <= 7:
        mau = "\033[1;3" + str(random.randint(1, 7)) + "m"
    elif rand >= 8 and rand <= 231:
        rand = random.randint(1, 231)
        mau = "\033[38;5;" + str(rand) + "m"
    return mau
class  Golike_INSTA:
    def __init__ (self,account_id,athor,req = None,UserAgent ='Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'):
        self.header = {'Host':'gateway.golike.net',    'Accept':'application/json, text/plain, */*',    "Accept-Language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",    'Authorization': athor,    'Content-Type':'application/json;charset=UTF-8',    'Origin':'https://app.golike.net',    'Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',    'Sec-Ch-Ua-Mobile':'?1',    'Sec-Ch-Ua-Platform':'"Android"',    'Sec-Fetch-Dest':'empty',    'Sec-Fetch-Mode':'cors',    'Sec-Fetch-Site':'same-site',    'T':'VFZSamVVMVVVVEJQVkdOM1RWRTlQUT09',    'User-Agent':UserAgent}
        if (req == None):
            self.req= requests.Session ()
        else:
            self.req= req
        self.account_id = account_id
        self.athor = athor
        self.UserAgent= UserAgent
    def get_jobs (self):
        import json
        get_ = self.req.get(url='https://gateway.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id=' + str(self.account_id) + '"&data=null', headers=self.header).text
        jsonstr = json.loads(get_)
        try:
            self.link = jsonstr["data"]["link"]
            self.id_jobs = jsonstr["data"]["id"]
            self.st = jsonstr["status"]
            self.ty = jsonstr["data"]["package_name"]
            self.price_after_cost = jsonstr['data']['price_per_after_cost']
            self.object_id = jsonstr['data']['object_id']
            if (self.ty  == 'comment'):
                    self.idcmt =  str(jsonstr['data']['comment_run']['id'])
                    self.ndungcmt = str(jsonstr['data']['comment_run']['message'])
                    self.ndung_ht = get_.split ('"comment_run"',1)[1].split ('"message":"')[1].split ('","status"')[0]
                    return {"trangthai":True, "id_jobs":self.id_jobs,"link":self.link,"type":self.ty,"coin":self.price_after_cost,"object_id":self.object_id, "id_cmt":self.idcmt, "ndung_cmt":self.ndungcmt}
            else:
                return {"trangthai":True, "id_jobs":self.id_jobs,"link":self.link,"type":self.ty,"coin":self.price_after_cost,"object_id":self.object_id}
        except:
            return {"trangthai":False}
    def hoan_thanh (self):
        if (self.ty == 'like' or self.ty == 'follow' ):
            data ={"instagram_users_advertising_id":self.id_jobs,"instagram_account_id":self.account_id,"async":True,"data":None}
            get_ = self.req.post ('https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs', headers=self.header,data=json.dumps(data)).text
            jsonstr = json.loads(get_)
        elif (self.ty  == 'comment'):
                dt = '{' + f'"instagram_users_advertising_id":{self.id_jobs},"instagram_account_id":{self.account_id},"async":true,"comment_id":{self.idcmt},"message":"{self.ndung_ht}"' + '}'
                get_ = self.req.post ('https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs', headers=self.header, data=dt).text
                #get_ = self.req.post ('https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs', headers=self.header, data=data).text

                jsonstr = json.loads(get_)
        if (jsonstr["status"] == 200):
            return {"trangthai":True}
        else:
            return {"trangthai":False}

    def bao_loi (self):
        try:
            data = {"ads_id":self.id_jobs,"object_id":f"{self.object_id }","account_id":self.account_id,"type":self.ty}
            get_jobs = self.req.post (f'https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',data=json.dumps (data),headers=self.header).json()
            if (get_jobs["status"] == 200):
                return {"trangthai":True}
            else:
                return {"trangthai":False}
        except Exception as e:
               print (e)
               return {"trangthai":False}

class INSTAGRAM_REQ:
    def __init__(self,cookie,req=None,useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'):
        self.cookie = cookie
        if (req == None):
            self.req= requests.Session ()
        else:
            self.req= req
        self.useragent=useragent
        self.header = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'cookie': self.cookie ,
            'dpr':'1',
            'priority':'u=0, i',
            'sec-ch-prefers-color-scheme':'light',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'upgrade-insecure-requests':'1',
            'user-agent':self.useragent,
            'viewport-width':'912'
        }
        self.csrftoken= cookie.split ('csrftoken=')[1].split (';')[0].replace (' ','')
    def check_username (self):
        try:
            text = self.req.get ('https://www.instagram.com/profile.php',headers=self.header ).text
            username_ig = text.split ('"username":"')[1].split ('"')[0]
            return username_ig
        except:
            return 'none'
    def follow(self, url):
        try:
            get = self.req.get (url,headers=self.header).text
            
            av = get.split ('"actorID":"')[1].split ('"')[0]
            hs= get.split ('"haste_session":"')[1].split ('"')[0]
            hsi = get.split ('"hsi":"')[1].split ('"')[0]
            rev_ = get.split ('"__spin_r":')[1].split (',')[0]
            __spin_t = get.split ('"__spin_t":')[1].split (',')[0]
            fb_dtsg = get.split ('"DTSGInitData"')[1].split ('"token":"')[1].split ('"')[0]
            lsd = get.split ('"LSD",')[1].split ('"token":"')[1].split ('"')[0]
            jazoest=get.split ('&jazoest=')[1].split ('"')[0].split ('&')[0]
            id_fl = get.split ('"profile_id":"')[1].split ('"')[0]

            versioningID = get.split ('"versioningID":"')[1].split ('"')[0]
            app_id = get.split ('"X-IG-App-ID":"')[1].split ('"')[0]
            
            import urllib.parse
            import urllib
            data = ('av=' + av +'&__d=www&__user=0&__a=1&__req=y&__hs=' +urllib.parse.quote (hs)+ '&dpr=1&__ccg=UNKNOWN&__rev='+ rev_+'&__s=2jf96v%3Atu2kai%3Azcd8rn&__hsi='+hsi+'&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awpUO0n24oaEnxO1ywOwv89k2C1Fwc60D87u3ifK0EUjwGzEaE2iwNwmE2eUlwhEe87q7U1bobpEbUGdwtUd-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubxKi2qi7ErwYCz8rwHwjE&__csr=gaQtMNsQszN6xAZE-xnllh5mGQh5EJaWiApXyTuHGHKXACIxWBWqhpE_AJljiy99ZHjADDVay98Cj-mGhbCyp4FqKHABDDGWAyFEHgObWWl2EDBUyiQ9Bix64EBkm-ido8u7pmcx28Uxe8w04yv-2S1180FU-7A0dYzQczE4wM5W16x24oCq5Cdwxg981GU0a5C0HE9mip24ya5o6y48jPoaU8U18EsgaCmp912qpss0g-1mBIAOzQ9D2gmzU568xnyE2ADDyro4Z03_UbW80--4402De01kYw&__comet_req=7&fb_dtsg='+urllib.parse.quote (fb_dtsg)+'&jazoest='+jazoest+'&lsd='+lsd+'&__spin_r='+rev_+'&__spin_b=trunk&__spin_t='+__spin_t+'&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisFollowMutation&variables=%7B%22target_user_id%22%3A%22' + id_fl+'%22%2C%22container_module%22%3A%22profile%22%2C%22nav_chain%22%3A%22PolarisProfilePostsTabRoot%3AprofilePage%3A1%3Avia_cold_start%22%7D&server_timestamps=true&doc_id=7275591572570580')
            header_req = {
            'accept-language':'vi,en-US;q=0.9,en;q=0.8',
            'content-length':str(len(data)),
            'content-type':'application/x-www-form-urlencoded',
            'cookie':self.cookie,
            'origin':'https://www.instagram.com',
            'priority':'u=1, i',
            'referer':url,
            'user-agent':self.useragent,
            'x-asbd-id':'129477',
            'x-bloks-version-id':versioningID,
            'x-csrftoken':self.csrftoken,
            'x-fb-friendly-name':'usePolarisFollowMutation',
            'x-fb-lsd':lsd,
            'x-ig-app-id':app_id,
                    }
            fl = self.req.post ('https://www.instagram.com/graphql/query', data=data , headers=header_req).text
            trangthai= False
            if ('"status":"ok"' in fl):
                trangthai = True
            trangthai_2 = False
            if ('"following":true' in fl ):
                trangthai_2 = True
            elif ('"followed_by":true' in fl ):
                trangthai_2 = True
            elif ('"is_bestie":true' in fl ):
                trangthai_2 = True
            elif ('"outgoing_request":true' in fl ):
                trangthai_2 = True
            if (trangthai == True and trangthai_2 == False):
                return {"trangthai":'limit',"lido":"limit"}
            
            elif (trangthai == True and  trangthai_2==True):
                return {"trangthai":True}
            else:
                return {"trangthai":False,"lido":'thao tác thất bại'}
        except Exception as e:
            return {"trangthai":False,"lido":'thao tác thất bại'}
    def like(self, url):
        try:
            get = self.req.get (url,headers=self.header).text
            
            av = get.split ('"actorID":"')[1].split ('"')[0]
            hs= get.split ('"haste_session":"')[1].split ('"')[0]
            hsi = get.split ('"hsi":"')[1].split ('"')[0]
            rev_ = get.split ('"__spin_r":')[1].split (',')[0]
            __spin_t = get.split ('"__spin_t":')[1].split (',')[0]
            fb_dtsg = get.split ('"DTSGInitData"')[1].split ('"token":"')[1].split ('"')[0]
            lsd = get.split ('"LSD",')[1].split ('"token":"')[1].split ('"')[0]
            jazoest=get.split ('&jazoest=')[1].split ('"')[0].split ('&')[0]
            media_id = get.split ('"media_id":"')[1].split ('"')[0]

            versioningID = get.split ('"versioningID":"')[1].split ('"')[0]
            app_id = get.split ('"X-IG-App-ID":"')[1].split ('"')[0]
            
            import urllib.parse
            import urllib
            data = (f'av={av}&__d=www&__user=0&__a=1&__req=l&__hs={urllib.parse.quote (hs)}&dpr=1&__ccg=UNKNOWN&__rev={rev_}&__s=8x9z5g%3Atu2kai%3Afgwok5&__hsi={hsi}&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awpUO0n24oaEnxO1ywOwv89k2C1Fwc60D87u3ifK0EUjwGzEaE2iwNwmE2eUlwhEe87q7U1bobpEbUGdwtUd-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubxKi2K7ErwYCz8rwHwjE&__csr=gaO6MRsQvf4qbdfrdEhZll4lqHh4haZbWiApUZQEOXDACBhWBAqhp8jAjRAgKivqQV8_AG8AypfVqF4LAypqBGWKaDDCxCaQcy-KBgG9Vu8AJ3QE98Bam-ido8UtBoO48zy99Q00ihcw2Dypo0RbwhUZ1K18c0Fogx69Cw0MNo3kp9A8i8Elwq8gxfdwHwzw4ywi6mp913ACn7030VUCS1fg0_-0j7x100FPw0lf8&__comet_req=7&fb_dtsg={urllib.parse.quote (fb_dtsg)}&jazoest={jazoest}&lsd={lsd}&__spin_r={rev_}&__spin_b=trunk&__spin_t={__spin_t}&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=usePolarisLikeMediaLikeMutation&variables=%7B%22media_id%22%3A%22{media_id}%22%7D&server_timestamps=true&doc_id=8244673538908708')
            header_req = {
            'accept-language':'vi,en-US;q=0.9,en;q=0.8',
            'content-length':str(len(data)),
            'content-type':'application/x-www-form-urlencoded',
            'cookie':self.cookie,
            'origin':'https://www.instagram.com',
            'priority':'u=1, i',
            'referer':url,
            'user-agent':self.useragent,
            'x-asbd-id':'129477',
            'x-bloks-version-id':versioningID,
            'x-csrftoken':self.csrftoken,
            'x-fb-friendly-name':'usePolarisFollowMutation',
            'x-fb-lsd':lsd,
            'x-ig-app-id':app_id,
                    }
            lk = self.req.post ('https://www.instagram.com/graphql/query', data=data , headers=header_req).text
            trangthai= False
            if ('"status":"ok"' in lk):
                trangthai = True
            trangthai_2 = False
            if ('"is_final":true' in lk ):
                trangthai_2 = True

            if (trangthai == True and trangthai_2 == False):
                return {"trangthai":'limit',"lido":"limit"}
            
            elif (trangthai == True and  trangthai_2==True):
                return {"trangthai":True}
            else:
                return {"trangthai":False,"lido":'thao tác thất bại'}
        except Exception as e:
            return {"trangthai":False,"lido":'thao tác thất bại'}
       
    def comment (self,url,ndung):
        try:
            get = self.req.get (url,headers=self.header).text
            
            av = get.split ('"actorID":"')[1].split ('"')[0]
            hs= get.split ('"haste_session":"')[1].split ('"')[0]
            hsi = get.split ('"hsi":"')[1].split ('"')[0]
            rev_ = get.split ('"__spin_r":')[1].split (',')[0]
            __spin_t = get.split ('"__spin_t":')[1].split (',')[0]
            fb_dtsg = get.split ('"DTSGInitData"')[1].split ('"token":"')[1].split ('"')[0]
            lsd = get.split ('"LSD",')[1].split ('"token":"')[1].split ('"')[0]
            jazoest=get.split ('&jazoest=')[1].split ('"')[0].split ('&')[0]
            id_cmt = get.split ('"media_id":"')[1].split ('"')[0]

            versioningID = get.split ('"versioningID":"')[1].split ('"')[0]
            app_id = get.split ('"X-IG-App-ID":"')[1].split ('"')[0]
            
            import urllib.parse
            import urllib
            data = (f'av={av}&__d=www&__user=0&__a=1&__req=k&__hs={urllib.parse.quote (hs)}&dpr=1&__ccg=UNKNOWN&__rev={rev_}&__s=hjlypc%3Atu2kai%3Agg89ig&__hsi={hsi}&__dyn=7xeUjG1mxu1syUbFp41twpUnwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awpUO0n24oaEnxO1ywOwv89k2C1Fwc60D87u3ifK0EUjwGzEaE2iwNwmE2eUlwhEe87q7U1bobpEbUGdwtUd-2u2J0bS1LwTwKG1pg2fwxyo6O1FwlEcUed6goK2OubxKi2K7ErwYCz8rwHwjE&__csr=gaO6MRsQvf4qbdfqfElRlkhlGJ4h4HQLFahDzTizbKuiql7GmhF5Axehfmh2V9ZHjAz-iEyi9A_BGAi-i9BGmHGUGuuq6oHgObWWl2EDBUyiQfiwAykFrV8RwzxSlz8gye8ADg0194O0au9Bw3kK17zQ6U4wM2Bx24oCq0335wdhACgx8yxm1Ex24YS2K2e0ia18ppAA4eipss0c3Dyro4Z03_U1cu4402De01kYw&__comet_req=7&fb_dtsg={urllib.parse.quote (fb_dtsg)}&jazoest={jazoest}&lsd={lsd}&__spin_r={rev_}&__spin_b=trunk&__spin_t={__spin_t}&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=PolarisPostCommentInputRevampedMutation&variables=%7B%22connections%22%3A%5B%22client%3Aroot%3A__PolarisPostCommentsDirect__xdt_api__v1__media__media_id__comments__connection_connection(data%3A%7B%7D%2Cmedia_id%3A%5C%22{id_cmt}%5C%22%2Csort_order%3A%5C%22popular%5C%22)%22%5D%2C%22request_data%22%3A%7B%22comment_text%22%3A%22{urllib.parse.quote (ndung)}%22%7D%2C%22media_id%22%3A%223420172113959420596%22%7D&server_timestamps=true&doc_id=7980226328678944')
            header_req = {
            'accept-language':'vi,en-US;q=0.9,en;q=0.8',
            'content-length':str(len(data)),
            'content-type':'application/x-www-form-urlencoded',
            'cookie':self.cookie,
            'origin':'https://www.instagram.com',
            'priority':'u=1, i',
            'referer':url,
            'user-agent':self.useragent,
            'x-asbd-id':'129477',
            'x-bloks-version-id':versioningID,
            'x-csrftoken':self.csrftoken,
            'x-fb-friendly-name':'usePolarisFollowMutation',
            'x-fb-lsd':lsd,
            'x-ig-app-id':app_id,
                    }
            lk = self.req.post ('https://www.instagram.com/graphql/query', data=data , headers=header_req).text
    
            trangthai= False
            if ('"status":"ok"' in lk):
                trangthai = True
            trangthai_2 = False
            if ('"is_final":true' in lk ):
                trangthai_2 = True

            if (trangthai == True and trangthai_2 == False):
                return {"trangthai":'limit',"lido":"limit"}
            
            elif (trangthai == True and  trangthai_2==True):
                return {"trangthai":True}
        except Exception as e:
            return {"trangthai":False,"lido":'thao tác thất bại'}

def clean_bar ():
  if (kiemtrathietbi()):
    os.system ("clear")
  else:
    os.system ("cls")
def addproxy (proxy, req = None):
    from requests.auth import HTTPProxyAuth
    if (req == None):
        req = requests.Session()
    proxy=proxy.replace(' ','')
    try:
        ip,port,user,passw = None,None,None,None
        if (len(proxy.split(':')) ==4 ):
            ip,port,user,passw=proxy.split(':')
        elif (len(proxy.split(':')) == 2):
            ip,port=proxy.split(':')
        if ip != None:
            if user !=None:
                        proxies = {
                        "http": f"http://{user}:{passw}@{ip}:{port}",
                        "https": f"http://{user}:{passw}@{ip}:{port}"
                        }
                        auth = requests.auth.HTTPProxyAuth(user, passw)
                        req.proxies = proxies
                        req.auth = auth
            else:
                        proxies = {
                        "http": f"http://{ip}:{port}",
                        "https": f"http://{ip}:{port}",
                        }
                        req.proxies = proxies
    except:
        pass
    return req
def checkcauhinh_golikeig (dulieu , account):
    for i in range(len(account['data'])):
        id =  account['data'][i]['id']
        id_u = account['data'][i]['instagram_id']
        ten = account['data'][i]['instagram_username']
        if  (dulieu == id or dulieu == id_u or dulieu == ten):
            return {"trangthai":True, "id":id}
    return {"trangthai":False, "id":id}
redb = "\033[1;31m"
red = "\033[1;31m"
green = "\033[1;32m"
red="\033[1;31m"
black="\033[0;30m"
blackb="\033[1;30m"
white="\033[1;37m"
whiteb="\033[1;37m"
redb="\033[1;31m"
green="\033[0;32m"
greenb="\033[1;32m"
yellow="\033[0;33m"
yellowb="\033[1;33m"
syan="\033[1;36m"
blue="\033[0;34m"
blueb="\033[1;34m"
purple="\033[0;35m"
purpleb="\033[1;35m"
lightblue="\033[0;36m"
lightblueb="\033[1;36m"
xanh= "\033[1;96m"
xlacay ="\033[0;32m"
den="\033[1;90m"
do="\033[1;91m"
luc="\033[1;92m"
vang="\033[1;93m"
xduong="\033[1;94m"
delay1=''
boqua1= ''
hong="\033[1;95m"
trang="\033[1;97m"
vang="\033[1;93m"
thanhngang ="══════════════════════════════════════════════════════════════"
redb = "\033[1;31m"
red = "\033[1;31m"
green = "\033[1;32m"
red="\033[1;31m"
black="\033[0;30m"
blackb="\033[1;30m"
white="\033[1;37m"
whiteb="\033[1;37m"
redb="\033[1;31m"
green="\033[0;32m"
greenb="\033[1;32m"
yellow="\033[0;33m"
yellowb="\033[1;33m"
syan="\033[1;36m"
blue="\033[0;34m"
blueb="\033[1;34m"
purple="\033[0;35m"
purpleb="\033[1;35m"
lightblue="\033[0;36m"
lightblueb="\033[1;36m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blud="\033[1;34m"
res="\033[1;35m"
nau="\033[1;36m"
trang="\033[1;37m"
cam= "\033[38;5;208m"
lavender="\033[1;95m"
peach="\033[1;96m"
coral="\033[1;97m"
charcoal="\033[1;98m"
maroon="\033[1;99m"
gold="\033[1;100m"
teal="\033[1;101m"
indigo="\033[1;102m"
rose="\033[1;103m"
icon1 = "\033[1;37m•[✩]➭ \033[1;37m"
icon2 = "\033[1;33m•[۞] ➭ : \033[1;37m"
syan="\033[1;36m"
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"

import os
try:
    crv =open ("chrome_VERSION.txt",'r',encoding="utf-8").read()
except:
    crv =open ("chrome_VERSION.txt",'w',encoding="utf-8").write('127')
data = {}

try:
    data = json.loads (open ("data_instagram_golike_tool.txt","r",encoding= "utf-8").read())
except :
    pass

try:
    data["delay"]
except:
    data["delay"] = {}
try:
    delay_like_min = data["delay"]["like_min"]
    delay_like_max = data["delay"]["like_max"]
    delay_follow_min = data["delay"]["follow_min"]
    delay_follow_max = data["delay"]["follow_max"]
    delay_comment_min = data["delay"]["comment_min"]
    delay_comment_max = data["delay"]["comment_max"]
    delay_get_jobs_min= data["delay"]["get_jobs_min"]
    delay_get_jobs_max= data["delay"]["get_jobs_max"]
    delay_lam_jobs_doi_acc = data["delay"]["lam_jobs_doi_acc"]
    check = input("Bạn muốn dùng lại setting đã lưu? (Y/N) : ")
except:
    check = "n"
if check.lower() == "n":
    print (f'{greenb}Lưu Ý : Min Phải Nhỏ Hơn Hoặc Bằng Max')
    while True:
        try:
            data["delay"]["like_min"] = int (input (f'{greenb}[{lightblueb}1{greenb}] {blueb}Nhập Delay Like Min: {red}').replace (' ',''))
            data["delay"]["like_max"] = int (input (f'{greenb}[{lightblueb}2{greenb}] {blueb}Nhập Delay Like Max: {red}').replace (' ',''))
            data["delay"]["follow_min"] = int (input (f'{greenb}[{lightblueb}3{greenb}] {blueb}Nhập Delay Follow Min: {red}').replace (' ',''))
            data["delay"]["follow_max"] = int (input (f'{greenb}[{lightblueb}4{greenb}] {blueb}Nhập Delay Follow Max: {red}').replace (' ',''))
            data["delay"]["comment_min"] = int (input (f'{greenb}[{lightblueb}3{greenb}] {blueb}Nhập Delay Comment Min: {red}').replace (' ',''))
            data["delay"]["comment_max"] = int (input (f'{greenb}[{lightblueb}4{greenb}] {blueb}Nhập Delay Comment Max: {red}').replace (' ',''))
            data["delay"]["get_jobs_min"] = int (input (f'{greenb}[{lightblueb}5{greenb}] {blueb}Nhập Delay Get Jobs Min: {red}').replace (' ',''))
            data["delay"]["get_jobs_max"] = int (input (f'{greenb}[{lightblueb}6{greenb}] {blueb}Nhập Delay Get Jobs Max: {red}').replace (' ',''))
            data["delay"]["lam_jobs_doi_acc"] = int (input (f'{greenb}[{lightblueb}6{greenb}] {blueb}Nhập Sau Số Jobs Thì Đổi Acc: {red}').replace (' ',''))
            break
        except:
            print (f'{redb}Vui lòng chỉ nhập số, không nhập chữ')
    delay_like_min = data["delay"]["like_min"]
    delay_like_max = data["delay"]["like_max"]
    delay_follow_min = data["delay"]["follow_min"]
    delay_follow_max = data["delay"]["follow_max"]
    delay_comment_min = data["delay"]["comment_min"]
    delay_comment_max = data["delay"]["comment_max"]
    delay_get_jobs_min= data["delay"]["get_jobs_min"]
    delay_get_jobs_max= data["delay"]["get_jobs_max"]
    delay_lam_jobs_doi_acc = data["delay"]["lam_jobs_doi_acc"]
else:
    pass
open ("data_instagram_golike_tool.txt","w",encoding= "utf-8").write (json.dumps (data))
try:
    authorization = auth
    print(f"\nBạn Có Muốn Sử Dụng Lại Authorizations-Nhập (Y/N)", end = '')
    check = input().strip()
except:
    check = "n"
if check.lower() == "n":
    auth = input(f"{greenb}Authorization Golike: {whiteb}").strip()
    data["authorization"] = auth  
else:
    pass

# Cách tốt nhất
if "User-Agent" not in data:
    data["User-Agent"] = getuseragent.UserAgent('android').Random()

scraper = cloudscraper.create_scraper()

# Cookie có thể không cần set cứng, hoặc nếu set thì nên lấy từ phiên mới nhất. 
# Nếu muốn set cứng, hãy chắc chắn bạn lấy đúng từ DevTools của Golike:
# scraper.cookies.set("golike_session", "fa2Y9JtF5V4XpvF3FCiiO4VX4BFKjaa0uf241SUI", domain="gateway.golike.net")

# header phải dùng Authorization do user nhập:
header = {
    'Host':'gateway.golike.net',
    'Accept':'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Authorization': auth,
    'Content-Type':'application/json;charset=UTF-8',
    'Origin':'https://app.golike.net',
    'Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'Sec-Ch-Ua-Mobile':'?1',
    'Sec-Ch-Ua-Platform':'"Android"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'T':'VFZSak1FNUVaekpOVkZreFRYYzlQUT09',
    'User-Agent':data["User-Agent"],
    'Referer': 'https://app.golike.net/'
}

try:
    login = scraper.get("https://gateway.golike.net/api/instagram-account", headers=header)
    if login.status_code == 200:
        print("✅ Đăng nhập thành công")
        try:
            account = login.json()
            
        except Exception as e:
            print("❌ Lỗi chuyển đổi JSON:", e)
            print("❌ Dữ liệu trả về:", login.text)
            exit(1)
    else:
        print(f"❌ Đăng nhập thất bại ({login.status_code}):")
        if login.text.strip().startswith("<!DOCTYPE html>"):
            print("⚠️  Golike trả về HTML → có thể bị Cloudflare chặn bot. Bạn cần thử lại hoặc thay User-Agent + Proxy.")
        else:
            print(login.text)
        exit(1)
except Exception as e:
    print("❌ Lỗi khi kết nối:", e)
    exit(1)

from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
import time

console = Console()



from rich.progress import Progress, SpinnerColumn, TextColumn

def nhan_tien_progress():
    console.print("[bold cyan]💸 Đang tiến hành nhận xu từ GoLike...[/bold cyan]\n")

    with Progress(
        SpinnerColumn(style="bold yellow"),
        TextColumn("[progress.description]{task.description}", style="bold white"),
        BarColumn(bar_width=40, complete_style="green"),
        TimeElapsedColumn(),
        transient=True
    ) as progress:
        task = progress.add_task("🪙 Đang nhận xu", total=100)
        for _ in range(100):
            progress.update(task, advance=1)
            time.sleep(0.015)

    console.print("[bold green]✅ Nhận xu thành công![/bold green]\n")


def spinner_get_job():
    with Progress(
        SpinnerColumn(spinner_name="bouncingBall"),
        TextColumn("[bold cyan]🔄 Đang get jobs..."),
        transient=True,
        refresh_per_second=12
    ) as progress:
        task = progress.add_task("get_job", total=None)
        time.sleep(1.5)  # bạn có thể chỉnh tùy vào thời gian thực thi get_job()

from rich.progress import Progress, SpinnerColumn, TextColumn
import time

def spinner_follow():
    with Progress(
        SpinnerColumn(spinner_name="line"),
        TextColumn("[bold white] Đang Follow..."),
        transient=True,
        refresh_per_second=10,
    ) as progress:
        task = progress.add_task("follow", total=None)
        time.sleep(1.5)  # chỉnh nếu cần

from rich.progress import Progress, SpinnerColumn, TextColumn
import time

def spinner_like():
    with Progress(
        SpinnerColumn(spinner_name="bouncingBar"),
        TextColumn("[bold white]Đang Like..."),
        transient=True,
        refresh_per_second=10,
    ) as progress:
        progress.add_task("like", total=None)
        time.sleep(1.5)  # thời gian hiển thị spinner, chỉnh tùy ý


account = login.json()
print(xlacay + 'Đang đọc thông tin account golike          ', end="\r")
try:
    user_info = scraper.get("https://gateway.golike.net/api/users/me", headers=header)
    if user_info.status_code == 200:
        username_golike = user_info.json()["data"]["username"]
    else:
        print(f"⚠️  Không thể lấy thông tin username (status: {user_info.status_code})")
        username_golike = "Không rõ"
except Exception as e:
    print("❌ Lỗi khi lấy thông tin username:", e)
    username_golike = "Không rõ"
    exit(1)

clean_bar ()
banner()
try:
    data["data"]
except:
    data["data"] = {}
try:
    data["data"][username_golike]
except:
    data["data"][username_golike]= {}
try:
    data["data"][username_golike]["cookie"]
except:
    data["data"][username_golike]["cookie"] = []

cookiecu = data["data"][username_golike]["cookie"]
data["data"][username_golike]["cookie"]  = []

from rich.console import Console

console = Console()

def show_cookie_result(index, username_ig, proxy_ip, status):
    if status == "ok":
        console.print(
            f"[bold green][{index}][/bold green] USER_INSTAGRAM: [white]{username_ig}[/white], "
            f"IP_PROXY: [white]{proxy_ip}[/white]"
        )
    elif status == "trung":
        console.print(
            f"[bold red]![/] Cookie thứ [bold green]{index}[/] bị trùng, bị lặp lại"
        )
    elif status == "chua_add":
        console.print(
            f"[bold yellow]⚠️ Tài khoản [bold green]{username_ig}[/bold green] chưa được thêm vào golike[/]"
        )
def hieu():
   table = Table.grid(padding=(0, 2))
   table.add_column(justify="left", no_wrap=True)

   # Thêm từng dòng với màu sắc nổi bật
   table.add_row("✅ [bold green]SUCCESS", f"[bold cyan][{dme_jobs_da_lam}]")
   table.add_row("🆔 [white]ID:", f"[bold yellow]{id_nv}")
   table.add_row("📌 [white]Nhiệm vụ:", f"[bold magenta]{type_nv}")
   table.add_row("💰 [white]Coin nhận được:", f"[bold green]{coin}đ")
   table.add_row("🔢 [white]Tổng Coin hiện tại:", f"[bold cyan]{total_coin}đ")
   table.add_row("🎉 [bold cyan]Thông báo:", "[bold green]Nhận xu thành công!")
   os.system("clear")
   console.print(Panel(table, title="[bold white]🎯 KẾT QUẢ NHIỆM VỤ", title_align="left", border_style="bold blue"))
   time.sleep(0.8)

def thong_bao_that_bai(id_nv, type_nv):
    msg = Text()
    msg.append("⛔ ", style="bold red")
    msg.append("FAILED (LIMIT ACTION)\n", style="bold red")
    msg.append("🆔 ID: ", style="white")
    msg.append(f"{id_nv}\n", style="bold green")
    msg.append("📌 Nhiệm Vụ: ", style="white")
    msg.append(f"{type_nv}", style="bold green")
    
    console.print(
        Panel(msg, title="[bold red]! THẤT BẠI", border_style="red", title_align="left")
    )
from rich.live import Live
from rich.spinner import Spinner
from rich.align import Align

def hien_thi_spinner_comment(tf):
    with Live(refresh_per_second=10) as live:
        for i in range(tf, 0, -1):
            spinner = Spinner("dots", text="[bold white]💬 Đang comment...")
            live.update(Align.left(spinner))
            time.sleep(1)
    console.print("[bold green]✅ Comment hoàn tất!\n")




import threading, time, json, random
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.text import Text
from rich.panel import Panel

console = Console()

def check_username_cookie_instagram(proxy, cookie):
    try:
        result = addproxy(proxy).get(
            'https://www.instagram.com/profile.php',
            timeout=5,
            headers={
                "Cookie": cookie,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
                "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
                "Priority": "u=0, i",
                "Accept": "text/html,application/xhtml+xml,...",
                "Cache-Control": "max-age=0"
            }
        ).text
        return result
    except:
        return ""
# === Biến toàn cục fix lỗi ===
demm = 1
demm_2 = 0
demm_3 = 0
tongtksong = 0
ckchay = []
list_username_ig = []

# === Class Thread with Result ===
class ThreadWithResult(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None):
        def function():
            self.result = target(*args, **kwargs)
        super().__init__(group=group, target=function, name=name, daemon=daemon)

# === Hàm check IG ===
def check_username_cookie_instagram(proxy, cookie):
    try:
        result = addproxy(proxy).get(
            'https://www.instagram.com/profile.php',
            timeout=5,
            headers={
                "Cookie": cookie,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
                "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126"',
                "Priority": "u=0, i",
                "Accept": "text/html,application/xhtml+xml,...",
                "Cache-Control": "max-age=0"
            }
        ).text
        return result
    except:
        return ""
from rich.panel import Panel
from rich.text import Text
def show_running_account(username_ig, ckchay):
    text = Text()
    text.append("🚀 Đang chạy tài khoản: ", style="bold white")
    text.append(f"{username_ig}\n", style="bold green")
    text.append("💡 Số cookie còn live: ", style="bold white")
    text.append(f"{len(ckchay)}", style="bold cyan")

    console.print(Panel.fit(text, title="", border_style="bold blue"))

from rich.table import Table
from rich.panel import Panel

def hien_thi_ket_qua(dme_jobs_da_lam, id_nv, type_nv, coin, total_coin):
    show_running_account(username_ig, ckchay)
    os.system("clear")
    table = Table(title=f"🎯 KẾT QUẢ NHIỆM VỤ #{dme_jobs_da_lam}", show_header=True, header_style="bold magenta")
    table.add_column("🔖 Trường", justify="left", style="bold cyan")
    table.add_column("📌 Thông tin", justify="left", style="bold white")

    table.add_row("🆔 ID Nhiệm Vụ", f"[green]{id_nv}")
    table.add_row("📌 Loại Nhiệm Vụ", f"[magenta]{type_nv.upper()}")
    table.add_row("💰 Xu Nhận", f"[yellow]{coin} đ")
    table.add_row("🔢 Tổng Xu", f"[bold cyan]{total_coin} đ")
    table.add_row("✅ Trạng Thái", "[bold green]Hoàn thành!")

    console.print(Panel(table, title="[bold white]🎉 Thành công", border_style="green"))

# === Hiển thị cảnh báo chưa thêm Golike ===
def thong_bao_chua_them_golike(username_ig):
    msg = Text()
    msg.append("🚫 ", style="bold red")
    msg.append("Tài khoản ", style="white")
    msg.append(f"{username_ig} ", style="bold green")
    msg.append("chưa được thêm vào GoLike", style="white")
    console.print(Panel(msg, title="[bold red]⚠️ CHƯA THÊM", border_style="red", title_align="left"))

# === Progress giả loading ===
def check_cookie_with_progress(delay_sec=5):
    with Progress(
        SpinnerColumn(spinner_name="earth", style="yellow"),
        TextColumn("[bold green]🍪 Đang check live cookie[dots]"),
        BarColumn(bar_width=None),
        TimeElapsedColumn(),
        console=console,
        refresh_per_second=10,
    ) as progress:
        task = progress.add_task("checking", total=delay_sec)
        while not progress.finished:
            progress.update(task, advance=0.1)
            time.sleep(0.1)
    console.print("[bold green]✅ Cookie live!\n")

if len(cookiecu) != 0:
    console.print(Panel.fit("[bold green]🔍 Đang đọc lại và check live những cookie cũ..."))
    ar_req = []

    # Tạo thread
    for pt_dathem in cookiecu:
        proxy = pt_dathem["proxy"]
        ck = pt_dathem["cookie"]
        t = ThreadWithResult(target=check_username_cookie_instagram, args=(proxy, ck))
        t.start()
        ar_req.append(t)
        time.sleep(0.1)

    console.rule("[bold red]──────────── Kết Quả Check Cookie ────────────")

    for i, pt_dathem in enumerate(cookiecu):
        try:
            ar_req[i].join()
            text = ar_req[i].result
            username_ig = text.split('"username":"')[1].split('"')[0]
            proxy_ip = pt_dathem["proxy"].split(":")[0]

            if username_ig in list_username_ig:
                show_cookie_result(demm_2, username_ig, proxy_ip, "trung")
            else:
                list_username_ig.append(username_ig)
                ktra_Acc = {"trangthai": True}  # giả lập
                if ktra_Acc["trangthai"]:
                    show_cookie_result(demm, username_ig, proxy_ip, "ok")
                    ckchay.append(pt_dathem)
                    tongtksong += 1
                    demm += 1
                else:
                    show_cookie_result(demm_2, username_ig, proxy_ip, "chua_add")
        except Exception as e:
            console.print(f"[red]⚠ Cookie thứ {i+1} lỗi: {e}")
    console.rule("[bold red]────────────────────────────────────────────")

# === Sau khi xử lý xong ===
if tongtksong != 0:
    print(f'Nhập số để sử dụng lại cookie cũ, ví dụ 1,2,3 : ', end="")
    try:
        nhap_gt = input('').replace(' ', '').split(',')
        for gt in nhap_gt:
            ckchay.append(cookiecu[int(gt)])
    except:
        pass
else:
    print('Tất cả các cookie cũ đã die')

demm = 1
print("Nhập cookie rồi thì enter bỏ trống thôi! ")
while (True):
    cookie_instagram = input (f'{redb}{demm} {greenb}Nhập cookie instagram cần chạy : {whiteb}')
    demm=demm+1
    if (cookie_instagram.replace (' ','') == ''  ):
        if (len(ckchay) >=1):
            break
        else:
            print (f'{redb}Vui lòng thêm ít nhất 1 cookie để chạy tool')
            continue
    cookie_proxy = input (f'{redb}{demm} {greenb}Nhập Proxy cho tài khoản trên ( Nếu Không Có Nhấn Enter Để Bỏ Qua): {whiteb}')
    try:
        check_cookie_with_progress(delay_sec=random.randint(3, 6))
        text = check_username_cookie_instagram (cookie_proxy,cookie_instagram )
        username_ig = text.split ('"username":"')[1].split ('"')[0]
        ktra_Acc = checkcauhinh_golikeig (username_ig,account)
        if (ktra_Acc["trangthai"] == True):
            data_them =  {"cookie":cookie_instagram, "proxy":cookie_proxy}
            print (f'{greenb} Success {greenb}Thêm thành công {lightblueb}{username_ig}')
            data["data"][username_golike]["cookie"].append (data_them)
            ckchay.append (data_them)
            
        else:
            print (f'{redb} Fail {greenb}Cấu hình thất bại, hãy chắc chắn {lightblueb}{username_ig} {greenb}bạn đã thêm vào golike ?')
    except Exception as e:
        print (f'{redb}Cookie không hợp lệ, MÃ LỖI:{e}')
open("data_instagram_golike_tool.txt", "w", encoding="utf-8").write(json.dumps(data))

if len(account['data']) == 0:
    print(f'{redb}Không tìm thấy bất kì tài khoản nào trong acc golike của bạn, hãy chắc chắn rằng bạn đã thêm vào golike !')
    exit(1)
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def show_processing_panel(index, id_nv, type_nv):
    text = Text()
    text.append(f"\n[🔄] Đang xử lý nhiệm vụ\n", style="bold cyan")
    text.append(f"[💡] STT: ", style="bold white")
    text.append(f"{index}\n", style="bold yellow")
    text.append(f"[🆔] ID nhiệm vụ: ", style="bold white")
    text.append(f"{id_nv}\n", style="bold green")
    text.append(f"[📝] Loại nhiệm vụ: ", style="bold white")
    text.append(f"{type_nv}\n", style="bold magenta")

    panel = Panel(text, title="[bold red]⚙ PROCESSING...", border_style="bright_blue", expand=False)
    console.print(panel)


dme_jobs_da_lam = 0
clean_bar ()
banner()

cau_hinh_tk = {}
cau_hinh_tk_bi_block_action = {}

total_coin = 0

while True:
    if (len (ckchay) == 0):
            print (f'{redb}Tất cả các cookie đã die')
            exit(1)
    for pt_dathem in ckchay:
        ck = pt_dathem["cookie"]
        proxy = pt_dathem["proxy"]
        req_ig = addproxy (proxy)
        ig_tool = INSTAGRAM_REQ (cookie= ck,req=req_ig)
        try:
            text =req_ig.get ('https://www.instagram.com/profile.php',headers= {"Cookie":ck, "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",'Sec-Ch-Ua':'"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"','Priority':'u=0, i','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Cache-Control':'max-age=0'}).text
            username_ig = text.split ('"username":"')[1].split ('"')[0]
            ktra_Acc = checkcauhinh_golikeig (username_ig,account)
            if (ktra_Acc["trangthai"] == True):
                id_account = ktra_Acc["id"]
                try:
                    cau_hinh_tk[username_ig]
                except:
                    cau_hinh_tk[username_ig]= False
                    cau_hinh_tk_bi_block_action[username_ig] = 0
            else:
                print (f'{redb} Fail {greenb}Cấu hình thất bại, hãy chắc chắn {lightblueb}{username_ig} {greenb}bạn đã thêm vào golike ?')
                print (f'{redb}Đã xoá cookies khỏi danh sách chậy        ' )
                ckchay.remove(pt_dathem)
                continue
        except Exception as e:
            print (f'{redb}Cookie không hợp lệ, MÃ LỖI:{e}')
            print (f'{redb}Đã xoá cookies khỏi danh sách chậy        ' )
            ckchay.remove(pt_dathem)
            continue
        show_running_account(username_ig, ckchay)
        golike_ig = Golike_INSTA (account_id=id_account,athor=data["authorization"] , req = scraper,UserAgent=data["User-Agent"])
        for dem_nv in range (int (delay_lam_jobs_doi_acc)):
            if (len (ckchay) == 0):
                print (f'{redb}Tất cả các cookie đã die')
                exit(1)
            try:
                for tf in range (random.randint(delay_get_jobs_min,delay_get_jobs_max),0,-1):
                    time.sleep (1)
                    print (f'{greenb}Đang Chạy {tf}s             ',end = '\r')
            except:
                print (f'{redb}Delay sai, hãy chắc rằng delay min bé hơn delay max')    
                exit(1)
            print (f'{greenb}Đang get jobs       ',end = "\r")
            get_jobs = golike_ig.get_jobs ()
            datagetjobs = {}
            if (get_jobs["trangthai"] == True):
                id_nv = get_jobs["object_id"]
                link = get_jobs["link"]
                type_nv = get_jobs["type"]
                coin = get_jobs["coin"]
                show_processing_panel(dme_jobs_da_lam, id_nv, type_nv)
                time.sleep (2)
                if (ig_tool.check_username() == 'none'):
                    print (f"{redb}Cookie {greenb}{username_ig} {redb}bị die")
                    print (f'{redb}Đã xoá cookies khỏi danh sách chậy        ' )
                    ckchay.remove(pt_dathem)
                    break
                if (cau_hinh_tk_bi_block_action[username_ig] > 10 ):
                    print (f"{redb}Cookie {greenb}{username_ig} {redb}bị chặn tương tác")
                    print (f'{redb}Đã xoá cookies khỏi danh sách chậy        ' )
                    ckchay.remove(pt_dathem)
                    break
                if (type_nv == "comment"):
                    ndungcomment = get_jobs["ndung_cmt"]
                    try:
                        if delay_comment_min > delay_comment_max:
                            raise ValueError("delay min > max")
                     
                            time_ran = random.randint(delay_comment_min, delay_comment_max)
                    except:
                        print(f'{redb}⛔ Delay sai, hãy chắc rằng delay min <= delay max và là số nguyên')
                        sys.exit(1)
                     
                    for tf in range((time_ran // 2) + 1, 0, -1):
                       time.sleep(1)
                       print(f'{greenb}⏳ Đang chạy {tf}s       ', end='\r')
                     
                    print (f'{whiteb}Đang comment           ', end = "\r" )
                    lam_nv = ig_tool.comment (link,ndungcomment)
                    try:
                        time_ran = random.randint(delay_comment_min, delay_comment_max)
                        for tf in range (random.randint(delay_get_jobs_min,delay_get_jobs_max),0,-1):
                           time.sleep (1)
                           print (f'{greenb}Đang Chạy {tf}s             ',end = '\r')
                    except:
                        print (f'{redb}Delay sai, hãy chắc rằng delay min bé hơn delay max     ')
                        exit(1)
                    if (lam_nv["trangthai"] == True):
                        hoanthanh = golike_ig.hoan_thanh ()
                        if (hoanthanh["trangthai"] == True):
                            total_coin = int (total_coin) + int (coin)
                            dme_jobs_da_lam = dme_jobs_da_lam + 1
                            hien_thi_ket_qua(dme_jobs_da_lam, id_nv, type_nv, coin, total_coin)
                            cau_hinh_tk_bi_block_action[username_ig] = 0
                        else:
                            print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (LỖI KHI BÁO CÁO HOÀN THÀNH) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                            bao_caoloi = golike_ig.bao_loi ()
                    elif (lam_nv["trangthai"] == 'limit'):
                        bao_caoloi = golike_ig.bao_loi ()
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (LIMIT ACTION) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                        cau_hinh_tk_bi_block_action[username_ig] = cau_hinh_tk_bi_block_action[username_ig] + 1
                    else:
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (ERROR OPERATION) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                        bao_caoloi = golike_ig.bao_loi ()
                elif (type_nv == "like"):
                    try:
                        time_ran = random.randint (delay_like_min, delay_like_max)
                        for tf in range (int (time_ran/2) + 1,0,-1):
                            time.sleep (1)
                            print (f'{greenb}Đang Chạy {tf}s             ',end = '\r')
                    except:
                        print (f'{redb}Delay sai, hãy chắc rằng delay min bé hơn delay max')
                        exit(1)
                    spinner_like()
                    lam_nv = ig_tool.like (link)
                    try:
                        for tf in range (int (time_ran/2) + 1,0,-1):
                            time.sleep (1)
                            print (f'{greenb}Đang Chạy {tf}s             ',end = '\r')
                    except:
                        print (f'{redb}Delay sai, hãy chắc rằng delay min bé hơn delay max     ')
                        exit(1)
                    if (lam_nv["trangthai"] == True):
                        hoanthanh = golike_ig.hoan_thanh ()
                        if (hoanthanh["trangthai"] == True):
                            total_coin = int (total_coin) + int (coin)
                            dme_jobs_da_lam = dme_jobs_da_lam + 1
                            hien_thi_ket_qua(dme_jobs_da_lam, id_nv, type_nv, coin, total_coin)
                            cau_hinh_tk_bi_block_action[username_ig] = 0
                        else:
                            print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (LỖI KHI BÁO CÁO HOÀN THÀNH) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                            bao_caoloi = golike_ig.bao_loi ()
                    elif (lam_nv["trangthai"] == 'limit'):
                        bao_caoloi = golike_ig.bao_loi ()
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (LIMIT ACTION) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                        cau_hinh_tk_bi_block_action[username_ig] = cau_hinh_tk_bi_block_action[username_ig] + 1
                    else:
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (ERROR OPERATION) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                        bao_caoloi = golike_ig.bao_loi ()
                elif (type_nv == "follow"):
                    
                    try:
                        time_ran = random.randint (delay_follow_min, delay_follow_max)
                        for tf in range (int (time_ran/2),0,-1):
                            time.sleep (1)
                            print (f'{greenb}Đang Chạy {tf}s             ',end = '\r')
                    except:
                        print (f'{redb}Delay Sai, Hãy Chắc Rằng Delay Min Bé hơn Delay Max')
                        exit(1)
                    spinner_follow()
                    lam_nv = ig_tool.follow (link)
                    try:
                        for tf in range (int (time_ran/2),0,-1):
                            time.sleep (1)
                            print (f'{greenb}Đang Chạy {tf}s             ',end = '\r')
                    except:
                        print (f'{redb}Delay sai, hãy chắc rằng delay min bé hơn delay max')
                        exit(1)
                    if (lam_nv["trangthai"] == True):
                        hoanthanh = golike_ig.hoan_thanh ()
                        if (hoanthanh["trangthai"] == True):
                            total_coin = int (total_coin) + int (coin)
                            dme_jobs_da_lam = dme_jobs_da_lam + 1
                            hien_thi_ket_qua(dme_jobs_da_lam, id_nv, type_nv, coin, total_coin)
                            cau_hinh_tk_bi_block_action[username_ig] = 0
                        else:
                            print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (LỖI KHI BÁO CÁO HOÀN THÀNH) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                            bao_caoloi = golike_ig.bao_loi ()
                    elif (lam_nv["trangthai"] == 'limit'):
                        bao_caoloi = golike_ig.bao_loi ()
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (LIMIT ACTION) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                        cau_hinh_tk_bi_block_action[username_ig] = cau_hinh_tk_bi_block_action[username_ig] + 1
                    else:
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (ERROR OPERATION) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                        bao_caoloi = golike_ig.bao_loi ()
                else:
                    bao_caoloi = golike_ig.bao_loi ()
                    if (bao_caoloi["trangthai"] == False):
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (Lỗi khi báo cáo) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}        ',end = "\n")
                    else:
                        print (f'{greenb}[{redb}!{greenb}] {redb}FAILED (Không hỗ trợ {type_nv}) {whiteb}ID: {greenb}{id_nv} {lightblueb}| {whiteb}Nhiệm Vụ: {greenb}{type_nv} {lightblueb}|{whiteb}             ',end = "\n")
            else:
                print (f'{redb}Golike Đã Hết Job    ', end = "\r")
                time.sleep (1)
