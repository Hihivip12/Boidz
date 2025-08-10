import requests, os, re, json, base64, random, uuid, sys
from time import sleep
from datetime import datetime
from pystyle import Colors, Colorate
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
trang = "\033[1;37m"
tim = "\033[1;35m"
xanh = "\033[1;36m"
thanh = f'{do}[{trang}</>{do}] {trang}=> '
listCookie = []
nhiem_vu_da_bat = {}
xam       = "\033[38;5;240m"  # xám chì
xanhbien  = "\033[38;5;33m"   # xanh biển đậm
cam       = "\033[38;5;208m"  # cam sáng
tim       = "\033[38;5;135m"  # tím pastel
xanhla    = "\033[38;5;34m"   # xanh lá rêu
trangnhat = "\033[38;5;255m"  # trắng nhạt
hongnhat  = "\033[38;5;213m"  # hồng phấn
camnhat   = "\033[38;5;215m"  # cam nhạt
lucnhat   = "\033[38;5;113m"  # xanh lá nhạt
lamnhat   = "\033[38;5;81m"   # xanh da trời pastel
reset     = "\033[0m"         # reset màu


def Server():
    response = requests.get('https://dhphuoc.click/api_key/server.php').json()
    if response['status'] == 'success': return 'LIVE' 
    else: return 'OFFLINE'
        
def thanhngang(so):
    for i in range(so):
        print(trang+'-',end ='')
    print('')

from rich.console import Console
from rich.panel import Panel
from pystyle import Colors, Colorate

console = Console()

from rich.console import Console
from rich.panel import Panel
from pystyle import Colors, Colorate
import os

console = Console()

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
  
    ascii_banner = r"""
██████╗░░█████╗░██╗███████╗
██╔══██╗██╔══██╗██║╚════██║
██████╦╝██║░░██║██║░░███╔═╝
██╔══██╗██║░░██║██║██╔══╝░░
██████╦╝╚█████╔╝██║███████╗
╚═════╝░░╚════╝░╚═╝╚══════╝
"""
    # In banner gradient
    print(Colorate.Horizontal(Colors.cyan_to_blue, ascii_banner, 1))

    # Nội dung thông tin
    info_tool = """[bold green]Admin:[/bold green] [yellow]Boiz[/yellow]
[bold green]Code By:[/bold green] [red]bõi[/red]
[bold green]Box Zalo:[/bold green] https://zalo.me/g/beizcs929[red][/red]
[bold green]Web Bán VPS :[/bold green] [red]éo cs[/red]
[bold green]Tool Này Không Phải Tôi Code Hoàn Toàn! 
[bold green]Tool đang sử dụng:[/bold green] [yellow]Nuôi Tài Khoản Facebook[/yellow]"""

    # Hiển thị thông tin tool trong Panel đẹp
    console.print(Panel.fit(info_tool, title="[bold cyan]THÔNG TIN", border_style="blue"))

    
from time import perf_counter, sleep
from rich.console import Console
from rich.text import Text

console = Console()

from time import perf_counter, sleep
from rich.console import Console
from rich.text import Text

console = Console()

def Delay(seconds: float, label="BVZONE"):
    animation = [
        ("✦", "red"),
        (" ✦", "yellow"),
        ("  ✦", "green"),
        ("   ✦", "cyan"),
        ("    ✦", "magenta"),
        ("     ✦", "red"),
        ("      ✦", "yellow"),
        ("       ✦", "green"),
        ("        ✦", "cyan"),
        ("         ✦", "bright_blue"),
        ("         ✦", "red"),
        ("        ✦", "yellow"),
        ("       ✦", "green"),
        ("      ✦", "cyan"),
        ("     ✦", "orange1"),  # Sửa từ 'organe1'
        ("    ✦", "red"),
        ("   ✦", "yellow"),
        ("  ✦", "green"),
        (" ✦", "cyan"),
        ("✦", "white"),
    ]
    index = 0
    start = perf_counter()

    while True:
        elapsed = perf_counter() - start
        remaining = seconds - elapsed
        if remaining <= 0:
            break

        msg = Text.assemble(
            ("💤 ", "bold"),
            (label, "bold cyan"),
            (" | Delay: ", "green"),
            (f"{remaining:5.2f}s ", "bold yellow"),
            animation[index]
        )
        console.print(msg, end="\r", highlight=False)
        sleep(0.05)
        index = (index + 1) % len(animation)

    console.print(" " * 60, end="\r")  # Xoá dòng cũ sau khi xong




        
def decode_base64(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = decoded_bytes.decode('utf-8')
    return decoded_str

def encode_to_base64(_data):
    byte_representation = _data.encode('utf-8')
    base64_bytes = base64.b64encode(byte_representation)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string
        
class Facebook:
    def __init__(self, cookie: str):
        try:
            self.fb_dtsg = ''
            self.jazoest = ''
            self.cookie = cookie
            self.session = requests.Session()
            self.id = self.cookie.split('c_user=')[1].split(';')[0]
            self.headers = {'authority': 'www.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-language': 'vi', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'viewport-width': '1366', 'Cookie': self.cookie}
            url = self.session.get(f'https://www.facebook.com/{self.id}', headers=self.headers).url
            response = self.session.get(url, headers=self.headers).text
            matches = re.findall(r'\["DTSGInitialData",\[\],\{"token":"(.*?)"\}', response)
            if len(matches) > 0:
                self.fb_dtsg += matches[0]
                self.jazoest += re.findall(r'jazoest=(.*?)\"', response)[0]
        except:
            pass

    def info(self):
        try:
            get = self.session.get('https://www.facebook.com/me', headers=self.headers).url
            url = 'https://www.facebook.com/' + get.split('%2F')[-2] + '/' if 'next=' in get else get
            response = self.session.get(url, headers=self.headers, params={"locale": "vi_VN"})
            data_split = response.text.split('"CurrentUserInitialData",[],{')
            json_data = '{' + data_split[1].split('},')[0] + '}'
            parsed_data = json.loads(json_data)
            id = parsed_data.get('USER_ID', '0')
            name = parsed_data.get('NAME', '')
            if id == '0' and name == '': return 'cookieout'
            elif '828281030927956' in response.text: return '956'
            elif '1501092823525282' in response.text: return '282'
            elif '601051028565049' in response.text: return 'spam'
            else: id, name = parsed_data.get('USER_ID'), parsed_data.get('NAME')
            return {'success': 200, 'id': id, 'name': name}
        except:
            pass

    def timban(self, text):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
                'variables': '{"count":5,"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"23bd9138-cec6-4e71-aaeb-225fc8964e5b","tsid":"0.10477759801522946"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GLOBAL_SEARCH"},"filters":[],"text":"'+text+'"},"cursor":null,"feedbackSource":23,"fetch_filters":true,"renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider":true,"__relay_internal__pv__CometFeedStoryDynamicResolutionPhotoAttachmentRenderer_experimentWidthrelayprovider":500,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider":false}',
                'server_timestamps': 'true',
                'doc_id': '9545374252239656'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data).json()
            profile = response["data"]["serpResponse"]["results"]["edges"][0]['rendering_strategy']['result_rendering_strategies'][0]['view_model']['profile']
            name = profile.get('name')
            uid = profile.get('id')
            return {'status': 'success', 'id': uid, 'name': name} 
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}
    
    def ketban(self, idkb):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'FriendingCometFriendRequestSendMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1748257667487,475021,190055527696468,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1748257603766,498383,391724414624676,,","click_proof_validation_result":null,"friend_requestee_ids":["'+idkb+'"],"friending_channel":"PROFILE_BUTTON","warn_ack_for_ids":[],"actor_id":"'+self.id+'","client_mutation_id":"6"},"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '8805328442902902'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data).json()
            trangthai = response["data"]["friend_request_send"]["friend_requestees"]
            if trangthai and trangthai[0].get('friendship_status') == 'OUTGOING_REQUEST':
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}
        
    def getidpost(self):
        try:
            variables = {"RELAY_INCREMENTAL_DELIVERY": True, "clientQueryId": "b7876288-8582-4b5a-9420-76f62adfe671", "count": 5, "cursor": None, "feedLocation": "NEWSFEED", "feedStyle": "DEFAULT", "orderby": ["TOP_STORIES"], "renderLocation": "homepage_stream", "scale": 1, "useDefaultActor": False}
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometNewsFeedPaginationQuery',
                'variables': json.dumps(variables),
                'server_timestamps': 'true',
                'doc_id': '29492828377027602'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data).text
            if '"post_id":"' in response:
                id = response.split('\"post_id\":\"')[1].split('\",')[0]
                return {'status': 'success', 'idpost': id}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}
        
    def getidgr(self, noidung):
        try:
            data = {
                'av': self.id,
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'SearchCometResultsInitialResultsQuery',
                'variables': '{"allow_streaming":false,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":false,"high_confidence_config":null,"intercept_config":null,"sts_disambiguation":null,"watch_config":null},"context":{"bsid":"435c49d4-a957-431e-834f-d1da37a5f10b","tsid":"0.37005625332226133"},"experience":{"client_defined_experiences":["ADS_PARALLEL_FETCH"],"encoded_server_defined_params":null,"fbid":null,"type":"GROUPS_TAB"},"filters":[],"text":"'+noidung+'"},"count":5,"cursor":"AboQDCkcpXHJTbFDxObZS3n0GamptQsxZrcXlcMFwGKIy8t_OUZV16uazBcCgVOMdao8EgVEpXIG4MarCu1ndTCT45yz6IlSEOoYZsWeqF88dZnyorpLHnwlfVTjfYgLOTH6ehf3WNbEtWS0QH3J4A4edpfakj35aqL9swaRPEe1KSYtaF_h7wjzfta_lLSzyM3JvI6JxKyZmMZJ_DAnhJw3MvQE5zgckZpVwJLHeYmG38bV6CQOTaa2hI8PY1xq5segTD2TAZZ-GJASsyGbZ8iJnjhT1MrtF5v5t_l4X4k1XXHs8woxmR1hmLVRhQGcXcwIms5_kCPaVPGE_ZBqvDGtoSq1vzx5qDIx49eXD-frk0ESlo_Nvj7ix7sXrHDZRpmA2ljWLZjmOXChNzGltKw7KekWeE0BrynOmH7k-L9pu85PJ5MVHm3uR-fFZWx8ytKb5DDwo1vN-pylOwsXs9MYR394Hcv8P4s9k90a4wqcsMHBNQmrcFO4Ab6nXcveCvFVWrF1hAEI0n9F69ye-QIy048hbmveTYV13UOLB5yrVWmAAYDuDlSS64-fHXNziJue641DOHnCxSOdPkKI6tCGm01UQgDJynSG56qtcF9HL8snD_5gZ9sDvqD8VCl-23LbiwRe2WjKrjUPaJmkk1fVLzXPrR8DURyrqHB5WBkE-Tn1idUEZaFMdKn2SSpdGB-9TIGrSWveurlC3483IkPkLveq2s0pr68FPPLMMO7Bk9art2BvG9JwszZjnQ8KjnDCmnUX1a71iCwM_iLnbuENJvWZtEO4Rjqu4XwqRtMWhc9RPZvKOaJY9L2e4DLvZbbARN0o-dS78Epa77LB-Th84FXyTs7KrZ_X57DwMjrYxh9CPyG-dMaxJtC8E-e2tFCYf9jRGgY1QrWky9rSz7oHHVnyDzNGqn-UOyHO8DSGve2mmvuQ6CubtYmcHTIL1SzU-_xhfHVpmzJiZ5lY_fwoncc-VC0uNkdoeVUmdl4OtxbTBr7VY2t5A-arm5Vy3_Dmj2hkGrUTAHFi7Zq4hehYaS04WBuYCKxiuO6Bjq7tWFVa2wnYNrTbEqTUVkc0ie5Bd7O-6Hz_PZa3Z_YWPxuobu2QpGQ_hwMBrFFNpZfPXWYPPO_ggdxV5qnRUbml5wQMyzD7w2p-NQr0jfqHPymCUjFpWj5PZUfwY4CPL-K5Ll7cTFjr6q1epx-0Xcvd5PKnt3hzfiY9yF1AygVKPM7g9KyLk9QNjV5Svjxj0tzsmxis6crBFT1PbeaHaxEkS41OnLHia80Q33yHUpfL7LoZ8QhSAYeObJR8wvmaBYZFQj5qIaYm1agsOl2Z_ukhRcDilQwX_gbPJnuJTcxDEoioLBxt5wdno4j8U7fusivPNVgKIN0Cy3znZwQOPwjDz6ZxnuhYMd9RrmG_un8eV1W6ypT1EVNRRUZlMdb3cMiFyx4CA59xaDhqpPMh_rOLoIV7RTDMjC7IdFHtAP2z4FX6Xv1TYDwipiacO-NGff2nEniPEjYIfhNKFvQQN-MRwaAVXI_VeoIfQ-B8kF2HN3fPGtTkppbuGhFAzx5trYkllKyVZZfGh23fFlAy1UyNStJ4hi61ivshFOOfgHVQpdUNV_nqE1MVPmBPIM2jwB6DpCFamSpX8Wn1LQkgdzlJRMmng-C8sAxwHeIgy5JA_CN-p2KCBCTwV_2D07lGbIVwtgZNqFWnNZa0HlX-bWGJDUGH4r_2Ns_G0VVE-VxBVcIGFC6d1iX98HS_6_ykwSc3Z2KB4nnWNlUa4gyWOlev2yg","feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":true,"focusCommentID":null,"locale":null,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1,"stream_initial_count":0,"useDefaultActor":false,"__relay_internal__pv__GHLShouldChangeAdIdFieldNamerelayprovider":true,"__relay_internal__pv__GHLShouldChangeSponsoredDataFieldNamerelayprovider":true,"__relay_internal__pv__IsWorkUserrelayprovider":false,"__relay_internal__pv__FBReels_deprecate_short_form_video_context_gkrelayprovider":true,"__relay_internal__pv__FeedDeepDiveTopicPillThreadViewEnabledrelayprovider":false,"__relay_internal__pv__CometImmersivePhotoCanUserDisable3DMotionrelayprovider":false,"__relay_internal__pv__WorkCometIsEmployeeGKProviderrelayprovider":false,"__relay_internal__pv__IsMergQAPollsrelayprovider":false,"__relay_internal__pv__FBReelsMediaFooter_comet_enable_reels_ads_gkrelayprovider":true,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false,"__relay_internal__pv__CometUFIShareActionMigrationrelayprovider":true,"__relay_internal__pv__CometUFI_dedicated_comment_routable_dialog_gkrelayprovider":false,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":true,"__relay_internal__pv__FBReelsIFUTileContent_reelsIFUPlayOnHoverrelayprovider":true}',
                'server_timestamps': 'true',
                'doc_id': '24016506881293628'
            }
            response = self.session.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data).json()
            thongtin = response['data']["serpResponse"]["results"]['edges'][0]['rendering_strategy']['view_model']['profile']
            name = thongtin.get('name')
            uid = thongtin.get('id')
            return {'status': 'success', 'id': uid, 'name': name}
        except:
            return {'status': 'error', 'trangthai': 'thatbai'}
        
    def reaction(self, id, type):
        try:
            reac = {"LIKE": "1635855486666999","LOVE": "1678524932434102","CARE": "613557422527858","HAHA": "115940658764963","WOW": "478547315650144","SAD": "908563459236466","ANGRY": "444813342392137"}
            idreac = reac.get(type)
            data = {'av': self.id,'fb_dtsg': self.fb_dtsg,'jazoest': self.jazoest,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation','variables': fr'{{"input":{{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1719027162723,322693,4748854339,,","feedback_id":"{encode_to_base64("feedback:"+str(id))}","feedback_reaction_id":"{idreac}","feedback_source":"NEWS_FEED","is_tracking_encrypted":true,"tracking":["AZWUDdylhKB7Q-Esd2HQq9i7j4CmKRfjJP03XBxVNfpztKO0WSnXmh5gtIcplhFxZdk33kQBTHSXLNH-zJaEXFlMxQOu_JG98LVXCvCqk1XLyQqGKuL_dCYK7qSwJmt89TDw1KPpL-BPxB9qLIil1D_4Thuoa4XMgovMVLAXncnXCsoQvAnchMg6ksQOIEX3CqRCqIIKd47O7F7PYR1TkMNbeeSccW83SEUmtuyO5Jc_wiY0ZrrPejfiJeLgtk3snxyTd-JXW1nvjBRjfbLySxmh69u-N_cuDwvqp7A1QwK5pgV49vJlHP63g4do1q6D6kQmTWtBY7iA-beU44knFS7aCLNiq1aGN9Hhg0QTIYJ9rXXEeHbUuAPSK419ieoaj4rb_4lA-Wdaz3oWiWwH0EIzGs0Zj3srHRqfR94oe4PbJ6gz5f64k0kQ2QRWReCO5kpQeiAd1f25oP9yiH_MbpTcfxMr-z83luvUWMF6K0-A-NXEuF5AiCLkWDapNyRwpuGMs8FIdUJmPXF9TGe3wslF5sZRVTKAWRdFMVAsUn-lFT8tVAZVvd4UtScTnmxc1YOArpHD-_Lzt7NDdbuPQWQohqkGVlQVLMoJNZnF_oRLL8je6-ra17lJ8inQPICnw7GP-ne_3A03eT4zA6YsxCC3eIhQK-xyodjfm1j0cMvydXhB89fjTcuz0Uoy0oPyfstl7Sm-AUoGugNch3Mz2jQAXo0E_FX4mbkMYX2WUBW2XSNxssYZYaRXC4FUIrQoVhAJbxU6lomRQIPY8aCS0Ge9iUk8nHq4YZzJgmB7VnFRUd8Oe1sSSiIUWpMNVBONuCIT9Wjipt1lxWEs4KjlHk-SRaEZc_eX4mLwS0RcycI8eXg6kzw2WOlPvGDWalTaMryy6QdJLjoqwidHO21JSbAWPqrBzQAEcoSau_UHC6soSO9UgcBQqdAKBfJbdMhBkmxSwVoxJR_puqsTfuCT6Aa_gFixolGrbgxx5h2-XAARx4SbGplK5kWMw27FpMvgpctU248HpEQ7zGJRTJylE84EWcVHMlVm0pGZb8tlrZSQQme6zxPWbzoQv3xY8CsH4UDu1gBhmWe_wL6KwZJxj3wRrlle54cqhzStoGL5JQwMGaxdwITRusdKgmwwEQJxxH63GvPwqL9oRMvIaHyGfKegOVyG2HMyxmiQmtb5EtaFd6n3JjMCBF74Kcn33TJhQ1yjHoltdO_tKqnj0nPVgRGfN-kdJA7G6HZFvz6j82WfKmzi1lgpUcoZ5T8Fwpx-yyBHV0J4sGF0qR4uBYNcTGkFtbD0tZnUxfy_POfmf8E3phVJrS__XIvnlB5c6yvyGGdYvafQkszlRrTAzDu9pH6TZo1K3Jc1a-wfPWZJ3uBJ_cku-YeTj8piEmR-cMeyWTJR7InVB2IFZx2AoyElAFbMuPVZVp64RgC3ugiyC1nY7HycH2T3POGARB6wP4RFXybScGN4OGwM8e3W2p-Za1BTR09lHRlzeukops0DSBUkhr9GrgMZaw7eAsztGlIXZ_4"],"session_id":"{uuid.uuid4()}","actor_id":"{self.id}","client_mutation_id":"3"}},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}}','server_timestamps': 'true','doc_id': '7047198228715224',}
            _get = self.session.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data)
            if '{"data":{"feedback_react":{"feedback":{"id":' in _get.text:
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            pass
        
    def comment(self, id, msg):
        try:
            data = {'av': self.id,'fb_dtsg': self.fb_dtsg,'jazoest': self.jazoest,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'useCometUFICreateCommentMutation','variables': fr'{{"feedLocation":"DEDICATED_COMMENTING_SURFACE","feedbackSource":110,"groupID":null,"input":{{"client_mutation_id":"4","actor_id":"{self.id}","attachments":null,"feedback_id":"{encode_to_base64(f"feedback:{id}")}","formatting_style":null,"message":{{"ranges":[],"text":"{msg}"}},"attribution_id_v2":"CometHomeRoot.react,comet.home,via_cold_start,1718688700413,194880,4748854339,,","vod_video_timestamp":null,"feedback_referrer":"/","is_tracking_encrypted":true,"tracking":["AZX1ZR3ETYfGknoE2E83CrSh9sg_1G8pbUK70jA-zjEIcfgLxA-C9xuQsGJ1l2Annds9fRCrLlpGUn0MG7aEbkcJS2ci6DaBTSLMtA78T9zR5Ys8RFc5kMcx42G_ikh8Fn-HLo3Qd-HI9oqVmVaqVzSasZBTgBDojRh-0Xs_FulJRLcrI_TQcp1nSSKzSdTqJjMN8GXcT8h0gTnYnUcDs7bsMAGbyuDJdelgAlQw33iNoeyqlsnBq7hDb7Xev6cASboFzU63nUxSs2gPkibXc5a9kXmjqZQuyqDYLfjG9eMcjwPo6U9i9LhNKoZwlyuQA7-8ej9sRmbiXBfLYXtoHp6IqQktunSF92SdR53K-3wQJ7PoBGLThsd_qqTlCYnRWEoVJeYZ9fyznzz4mT6uD2Mbyc8Vp_v_jbbPWk0liI0EIm3dZSk4g3ik_SVzKuOE3dS64yJegVOQXlX7dKMDDJc7P5Be6abulUVqLoSZ-cUCcb7UKGRa5MAvF65gz-XTkwXW5XuhaqwK5ILPhzwKwcj3h-Ndyc0URU_FJMzzxaJ9SDaOa9vL9dKUviP7S0nnig0sPLa5KQgx81BnxbiQsAbmAQMr2cxYoNOXFMmjB_v-amsNBV6KkES74gA7LI0bo56DPEA9smlngWdtnvOgaqlsaSLPcRsS0FKO3qHAYNRBwWvMJpJX8SppIR1KiqmVKgeQavEMM6XMElJc9PDxHNZDfJkKZaYTJT8_qFIuFJVqX6J9DFnqXXVaFH4Wclq8IKZ01mayFbAFbfJarH28k_qLIxS8hOgq9VKNW5LW7XuIaMZ1Z17XlqZ96HT9TtCAcze9kBS9kMJewNCl-WYFvPCTCnwzQZ-HRVOM04vrQOgSPud7vlA3OqD4YY2PSz_ioWSbk98vbJ4c7WVHiFYwQsgQFvMzwES20hKPDrREYks5fAPVrHLuDK1doffY1hPTWF2KkSt0uERAcZIibeD5058uKSonW1fPurOnsTpAg8TfALFu1QlkcNt1X4dOoGpYmBR7HGIONwQwv5-peC8F758ujTTWWowBqXzJlA2boriCvdZkvS15rEnUN57lyO8gINQ5heiMCQN8NbHMmrY_ihJD3bdM4s2TGnWH4HBC2hi0jaIOJ8AoCXHQMaMdrGE1st7Y3R_T6Obg6VnabLn8Q-zZfToKdkiyaR9zqsVB8VsMrAtEz0yiGpaOF3KdI2sxvii3Q5XWIYN6gyDXsXVykFS25PsjPmXCF8V1mS7x6e9N9PtNTWwT8IGBZp9frOTQN2O52dOhPdsuCHAf0srrBVHbyYfCMYbOqYEEXQG0pNAmG_wqbTxNew9kTsXDRzYKW-NmEJcvy_xh1dDwg8xJc58Cl71e-rau3iP7o8mWhVSaxi4Bi6LAuj4UKVCt3IYCfm9AR1d5LqBFWU9LrJbRZSMlmUYwZf7PlrKmpnCnZvuismiL7DH3cnUjP0lWAvhy3gxZm1MK8KyRzWmHnTNqaVlL37c2xoE4YSyponeOu5D-lRl_Dp_C2PyR1kG6G0TCWS66UbU89Fu1qmwWjeQwYhzj2Jly9LRyClAbe86VJhIZE18YLPB-n1ng78qz7hHtQ8qT4ejY4csEjSRjjnHdz8U-06qErY-CXNNsVtzpYGuzZ1ZaXqzAQkUcREm98KR8c1vaXaQXumtDklMVgs76gLqZyiG1eCRbOQ6_EcQv7GeFnq5UIqoMH_Xzc78otBTvC5j3aCs5Pvf6k3gQ5ZU7E4uFVhZA7xoyD8sPX6rhdGL8JmLKJSGZQM5ccWpfpDJ5RWJp0bIJdnAJQ8gsYMRAI2OBxx2m2c76lNiUnB750dMe2H3pFzFQVkWQLkmGVY37cgmRNHyXboDMQ1U2nlbNH017dmklJCk4jVU8aA9Gpo8oHw","{{\"assistant_caller\":\"comet_above_composer\",\"conversation_guide_session_id\":\"{uuid.uuid4()}\",\"conversation_guide_shown\":null}}"],"feedback_source":"DEDICATED_COMMENTING_SURFACE","idempotence_token":"client:{uuid.uuid4()}","session_id":"{uuid.uuid4()}"}},"inviteShortLinkKey":null,"renderLocation":null,"scale":1,"useDefaultActor":false,"focusCommentID":null}}','server_timestamps': 'true','doc_id': '7994085080671282',}
            cmt = self.session.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).json()
            if '"feedback_submitted":true' in str(cmt) or 'create_comment' in str(cmt):
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            pass
        
    def follow(self, id):
        try:
            data = {'av': self.id,'fb_dtsg': self.fb_dtsg,'jazoest': self.jazoest,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'CometUserFollowMutation','variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1719765181042,489343,250100865708545,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,unexpected,1719765155735,648442,391724414624676,,;SearchCometGlobalSearchDefaultTabRoot.react,comet.search_results.default_tab,tap_search_bar,1719765153341,865155,391724414624676,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+str(id)+'","tracking":null,"actor_id":"'+str(self.id)+'","client_mutation_id":"5"},"scale":1}','server_timestamps': 'true','doc_id': '25581663504782089',}
            response = self.session.post('https://www.facebook.com/api/graphql/',data=data,headers=self.headers)
            if '"subscribe_status":"IS_SUBSCRIBED"' in response.text:
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            pass
        
    def group(self, id):
        try:
            data = {'av':self.id,'fb_dtsg':self.fb_dtsg,'jazoest':self.jazoest,'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5853134681430324','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]',}
            response = self.session.post('https://www.facebook.com/api/graphql/',headers=self.headers, data=data)
            if id in response.text:
                return {'status': 'success', 'trangthai': 'thanhcong'}
            else:
                return {'status': 'error', 'trangthai': 'thatbai'}
        except:
            pass

def addcookie():
    i = 0
    while True:
        i += 1
        cookie = input(f'{luc}Nhập Cookie Facebook Số{vang} {i}{trang}: {vang}')
        if cookie == '' and i != 1:
            break 
        fb = Facebook(cookie)
        info = fb.info()
        if 'success' in info:
            name = info['name']
            print(f'{thanh}{luc}Tên Facebook: {vang}{name}')
            thanhngang(65)
            listCookie.append(cookie)
        else:
            print(f'{do}Cookie Facebook Die ! Vui Lòng Nhập Lại !!!')
            i -= 1

from rich.table import Table
from rich.prompt import Prompt
from rich.console import Console

console = Console()

def menu_chon_cookie():
    table = Table(title="🍪 CHỌN COOKIE FACEBOOK", style="bold cyan")
    table.add_column("Lựa chọn", justify="center", style="bold yellow")
    table.add_column("Mô tả", style="bold white")

    table.add_row("[1]", "Sử dụng cookie Facebook đã lưu")
    table.add_row("[2]", "Nhập cookie Facebook mới")
    
    console.print(table)
    chon = Prompt.ask("[bold green]Nhập lựa chọn của bạn[/bold green]", choices=["1", "2"], default="1")
    return chon

from rich.prompt import Confirm
from rich.panel import Panel
from rich.console import Console

console = Console()

def chon_nhiem_vu():
    banner()  # Hiển thị banner đẹp

    console.print(Panel.fit("[bold cyan]🛠️ BẬT TẮT TÍNH NĂNG TƯƠNG TÁC", style="bold blue"))

    comment = Confirm.ask("[green]➤ Bật comment dạo?", default=False)
    group = Confirm.ask("[green]➤ Tham gia nhóm dạo?", default=False)
    reaction = Confirm.ask("[green]➤ Thả cảm xúc dạo?", default=False)
    follow = Confirm.ask("[green]➤ Follow dạo?", default=False)
    add_friend = Confirm.ask("[green]➤ Gửi lời mời kết bạn dạo?", default=False)

    thanhngang(65)

    return comment, group, reaction, follow, add_friend

from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def chon_cam_xuc():
    nhiem_vu_da_bat['reaction'] = True

    table = Table(title="💖 Chọn Nhiệm Vụ Cảm Xúc Facebook", style="cyan")
    table.add_column("STT", style="bold yellow", justify="center")
    table.add_column("Cảm Xúc", style="bold green")

    table.add_row("1", "👍 LIKE")
    table.add_row("2", "❤️ LOVE")
    table.add_row("3", "💗 CARE")
    table.add_row("4", "😂 HAHA")
    table.add_row("5", "😮 WOW")
    table.add_row("6", "😢 SAD")
    table.add_row("7", "😡 ANGRY")

    console.print(table)
    console.print("[bold green]Bạn có thể chọn nhiều loại cảm xúc (VD: 1345)[/bold green]")

    ds_camxuc = {
        "1": "LIKE",
        "2": "LOVE",
        "3": "CARE",
        "4": "HAHA",
        "5": "WOW",
        "6": "SAD",
        "7": "ANGRY"
    }

    chon = Prompt.ask("[bold blue]Nhập số để chọn nhiệm vụ cảm xúc[/bold blue]").strip()
    camxucchon = [ds_camxuc[c] for c in chon if c in ds_camxuc]
    return camxucchon

from rich.console import Console

console = Console()

def xu_ly_loi_taikhoan(check, namefb, listCookie, cookie, fb):
    if 'spam' in check:
        console.print(f"[bold red]⚠️ Tài khoản [yellow]{namefb}[/yellow] đã bị [red]SPAM[/red]")
        fb.clickDissMiss()

    elif '282' in check:
        console.print(f"[bold red]🔒 Tài khoản [yellow]{namefb}[/yellow] đã bị [red]Checkpoint 282[/red]")
        listCookie.remove(cookie)
        return True  # chuyển acc

    elif '956' in check:
        console.print(f"[bold red]🔐 Tài khoản [yellow]{namefb}[/yellow] đã bị [red]Checkpoint 956[/red]")
        listCookie.remove(cookie)
        return True  # chuyển acc

    else:
        console.print(f"[bold red]🚫 Tài khoản [yellow]{namefb}[/yellow] đã bị [red]Out Cookie[/red], đã xoá khỏi danh sách.")
        listCookie.remove(cookie)
        return True  # chuyển acc

    return False  # không cần chuyển acc


from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def chon_noidung_comment():
    comments = []

    table = Table(title=" NHẬP COMMENT", style="bold blue")
    table.add_column("Lựa chọn", justify="center", style="yellow")
    table.add_column("Chức năng", style="white")
    table.add_row("1", "Tự nhập nội dung comment")
    table.add_row("2", "Dùng danh sách comment random từ tool")

    console.print(table)
    chon = Prompt.ask("[bold green]Nhập lựa chọn[/bold green]", choices=["1", "2"], default="1")

    if chon == "1":
        console.print("[bold cyan]✍️ Nhập từng comment, để trống để kết thúc:[/bold cyan]")
        i = 1
        while True:
            cmt = Prompt.ask(f"[bold yellow]Nội dung comment #{i}[/bold yellow]").strip()
            if cmt == "":
                break
            comments.append(cmt)
            i += 1
    else:
        # Danh sách comment mặc định (bạn có thể sửa/tăng thêm tuỳ thích)
        comments = [
            "Tuyệt vời quá!",
            "Xịn ghê á 😍",
            "chất lượng thật sự!",
            "Ủng hộ 100 điểm nha 😁",
            "Like mạnh bài này 😎",
            "Lên top đi nào 🔥",
            "Comment cho vui^^",
            "Cười xỉu 😂😂😂",
            "Chuẩn không cần chỉnh!",
            "đẹp quá trời luôn!"
        ]
        console.print(f"[bold magenta]✅ Đã chọn {len(comments)} comment từ tool ngẫu nhiên.[/bold magenta]")

    return comments


from rich.prompt import IntPrompt
from rich.console import Console

console = Console()

def nhap_delay():
    while True:
        try:
            delay = IntPrompt.ask("[bold green]⏱ Nhập Delay (số giây giữa mỗi nhiệm vụ)[/bold green]")
            if delay <= 0:
                console.print("[bold red]⚠️ Vui lòng nhập số lớn hơn 0![/bold red]")
                continue
            return delay   # ✅ Thêm dòng này để trả về giá trị sau khi nhập đúng
        except Exception:
            console.print("[bold red]❌ Nhập không hợp lệ. Vui lòng nhập số![/bold red]")

# Ví dụ sử dụng



from rich.prompt import IntPrompt
from rich.console import Console

console = Console()

def nhap_jobb_block():
    while True:
        try:
            jobb = IntPrompt.ask("[bold cyan]Sau bao nhiêu nhiệm vụ thì nghỉ chống block?[/bold cyan]")
            if jobb <= 1:
                console.print("[bold red]⚠️ Phải lớn hơn 1![/bold red]")
                continue
            return jobb
        except Exception:
            console.print("[bold red]❌ Nhập sai định dạng! Vui lòng nhập số.[/bold red]")

from rich.prompt import IntPrompt
from rich.console import Console

console = Console()

def nhap_delay_block(jobb_block: int):
    while True:
        try:
            delay_block = IntPrompt.ask(
                f"[bold cyan]⏱ Sau {jobb_block} nhiệm vụ nghỉ bao nhiêu giây?[/bold cyan]"
            )
            return delay_block
        except Exception:
            console.print("[bold red]❌ Vui lòng nhập số nguyên![/bold red]")

from rich.live import Live
from rich.text import Text
from time import sleep
import json

def tai_du_lieu_cookie():
    with Live(refresh_per_second=4) as live:
        for i in range(10):  # Hiệu ứng xoay khoảng 1 giây
            dots = "." * (i % 4)
            live.update(Text(f"[cyan]📂 Đang tải dữ liệu đã lưu{dots}[/cyan]", justify="left"))
            sleep(0.1)

    with open('cookiefb-add.json', 'r') as f:
        return json.load(f)

from rich.prompt import IntPrompt
from rich.console import Console

console = Console()

def nhap_job_break():
    while True:
        try:
            jobbreak = IntPrompt.ask("[bold cyan]🔄 Sau bao nhiêu nhiệm vụ thì chuyển acc?[/bold cyan]")
            if jobbreak <= 1:
                console.print("[bold red]⚠️ Nhập số lớn hơn 1 để tránh lỗi![/bold red]")
                continue
            return jobbreak
        except Exception:
            console.print("[bold red]❌ Lỗi! Vui lòng nhập số nguyên.[/bold red]")

from rich.prompt import Confirm
from rich.console import Console

console = Console()

def nhap_an_id():
    return Confirm.ask("[bold cyan]🕵️ Bạn có muốn ẩn ID Facebook khi chạy tool?[/bold cyan]", default=False)
from rich.console import Console

console = Console()

def hien_thi_dong_nhiem_vu(stt, timejob, noidung, idpost):
    console.print(
        f"[red]|[/red] [bold yellow]{stt:>3}[/bold yellow] "
        f"[red]|[/red] [green]{timejob:<8}[/green] "
        f"[red]|[/red] [cyan]{noidung:<25}[/cyan] "
        f"[red]|[/red] [white]{idpost}[/white]",
        highlight=False
    )

server = Server()
if server != 'LIVE': print(f'{thanh}{luc}Trạng Thái Server{trang}: {trang}[{do}{server}{trang}]'); os.remove(sys.argv[0]); sys.exit(); quit()
else: 
    banner()
    if os.path.exists(f'cookiefb-add.json') == False:
        addcookie()
        with open('cookiefb-add.json','w') as f:
            json.dump(listCookie, f)
    else:
        chon = menu_chon_cookie()
        thanhngang(65)
        while True:
            if chon == '1':
                listCookie = tai_du_lieu_cookie()
                break
            elif chon == '2':
                addcookie()
                with open('cookiefb-add.json','w') as f:
                    json.dump(listCookie, f)
                break
            else:
                print(f'{do}Vui Lòng Nhập Đúng !!!')
    comment, group, reaction, follow, add_friend = chon_nhiem_vu()
    if comment:
       comments = chon_noidung_comment()

        
    if reaction:
        camxucchon = chon_cam_xuc()
    if group:
        nhiem_vu_da_bat['group'] = True
        
    if follow:
        nhiem_vu_da_bat['follow'] = True
        
    if add_friend:
        nhiem_vu_da_bat['add_friend'] = True
        
        try:
            delay = nhap_delay()
            print(f"⏳ Delay đã chọn: {delay} giây")
        except:
            print(f'{do}Vui Lòng Nhập Số')
        try:
            JobbBlock = nhap_jobb_block()
        except:
            print(f'{do}Vui Lòng Nhập Số')
        try:
            DelayBlock = nhap_delay_block(JobbBlock)
        except:
            print(f'{do}Vui Lòng Nhập Số')
        try:
            JobBreak = nhap_job_break()
        except:
            print(f'{do}Vui Lòng Nhập Số')
    runidfb = nhap_an_id()
    stt = 0
    while True:
        if len(listCookie) == 0:
            print(f'{do}Đã Xóa Tất Cả Cookie, Vui Lòng Nhập Lại !!!')
            addcookie()
            with open('cookiefb-add.json','w') as f:
                json.dump(listCookie, f)
        for cookie in listCookie:
            chuyen = False
            nextDelay = False
            JobFail, JobSuccess = 0, 0
            fb = Facebook(cookie)
            info = fb.info()
            if 'success' in info:
                namefb = info['name']
                idfb = str(info['id'])
                idrun = idfb[0]+idfb[1]+idfb[2]+"#"*(int(len(idfb)-3)) if str(runidfb).upper() == 'Y' else idfb

            else:
                print(f'{do}Cookie Facebook Die ! Đã Xóa Ra Khỏi List !!!')
                listCookie.remove(cookie)
                break
            from rich.panel import Panel

            info = f"[cyan]🔰 ID:[/cyan] [yellow]{idrun}[/yellow]\n[cyan]👤 Tên:[/cyan] [yellow]{namefb}[/yellow]"
            console.print(Panel(info, title="[bold green]THÔNG TIN FACEBOOK[/bold green]", border_style="bright_magenta"))
            while True:
                try:
                    nhiemvu = random.choice(list(nhiem_vu_da_bat.keys()))
                    if nhiemvu == "comment":
                        getpost = fb.getidpost()
                        if getpost.get('trangthai') == 'thatbai':
                            JobFail += 1
                            print(f'{trang}[{do}ERROR{trang}] {trang}Không Tìm Thấy Bài Nào', '            ', end="\r")
                        else:
                            idpost = getpost['idpost']
                            noidung = random.choice(comments)
                            cmt = fb.comment(idpost, noidung)
                            if cmt.get('trangthai') == 'thanhcong':
                                nextDelay, timejob = True, datetime.now().strftime('%H:%M:%S')
                                JobSuccess += 1
                                stt += 1
                                hien_thi_dong_nhiem_vu(stt, timejob, noidung, idpost)
                            else:
                                JobFail += 1
                                print(f'{trang}[{do}ERROR{trang}] {trang}Không Cmt Được', '            ', end="\r")
                    
                    if nhiemvu == "group":
                        gioitinh = random.choice(['female', 'male'])
                        ten = requests.get('https://dhphuoc.click/vietnamese-name-generator?gioitinh='+gioitinh).json()['data']['name']
                        timgr = fb.getidgr(ten)
                        if timgr.get('trangthai') == 'thatbai':
                            JobFail += 1
                            print(f'{trang}[{do}ERROR{trang}] {trang}Không Tìm Thấy Id Group Nào', '            ', end="\r")
                        else: 
                            id, name = timgr['id'], timgr['name']
                            thamgia = fb.group(id)
                            if thamgia.get('trangthai') == 'thanhcong':
                                nextDelay, timejob = True, datetime.now().strftime('%H:%M:%S')
                                JobSuccess += 1
                                stt += 1
                                print(f"{xam} ┃ {cam}[{stt}] {xam} ┃ {xam} {trangnhat}{timejob} {xam} ┃ {xam} {camnhat}THAMGIANHOM{xam}  ┃ {xam} {lamnhat}{name}")
                            else:
                                JobFail += 1
                                print(f'{trang}[{do}ERROR{trang}] {trang}Không Tham Gia Được Nhóm', '            ', end="\r")
                                
                    if nhiemvu == "reaction":
                        getpost = fb.getidpost()
                        if getpost.get('trangthai') == 'thatbai':
                            JobFail += 1
                            print(f'{trang}[{do}ERROR{trang}] {trang}Không Tìm Thấy Bài Nào', '            ', end="\r")
                        else:
                            idpost = getpost['idpost']
                            camxuc = random.choice(camxucchon)
                            tha = fb.reaction(idpost, camxuc)
                            if tha.get('trangthai') == 'thanhcong':
                                nextDelay, timejob = True, datetime.now().strftime('%H:%M:%S')
                                JobSuccess += 1
                                stt += 1
                                print(f"{xam} ┃ {cam}[{stt}] {xam} ┃ {xam} {trangnhat}{timejob} {xam} ┃ {xam} {camnhat}{camxuc}{xam}  ┃ {xam} {lamnhat}{idpost}")
                            else:
                                JobFail += 1
                                print(f'{trang}[{do}ERROR{trang}] {trang}Không Có Nút Cảm Xúc', '            ', end="\r")
                                
                    if nhiemvu == "follow":
                        gioitinh = random.choice(['female', 'male'])
                        ten = requests.get('https://dhphuoc.click/vietnamese-name-generator?gioitinh='+gioitinh).json()['data']['name']
                        timbb = fb.timban(ten)
                        if timbb.get('trangthai') == 'thatbai':
                            JobFail += 1
                            print(f'{trang}[{do}ERROR{trang}] {trang}Không Tìm Thấy Id Nào', '            ', end="\r")
                        else:
                            id, name = timbb['id'], timbb['name']
                            if fb.follow(id).get('trangthai') == 'thanhcong':
                                nextDelay, timejob = True, datetime.now().strftime('%H:%M:%S')
                                JobSuccess += 1
                                stt += 1
                                print(f"{xam} ┃ {cam}[{stt}] {xam} ┃ {xam} {trangnhat}{timejob} {xam} ┃ {xam} {camnhat}FOLLOWCHEO{xam}  ┃ {xam} {lamnhat}{name}")
                            else:
                                JobFail += 1
                                print(f'{trang}[{do}ERROR{trang}] {trang}Không Có Nút Theo Dõi', '            ', end="\r")
                                
                    if nhiemvu == "add_friend":
                        gioitinh = random.choice(['female', 'male'])
                        ten = requests.get('https://dhphuoc.click/vietnamese-name-generator?gioitinh='+gioitinh).json()['data']['name']
                        timbb = fb.timban(ten)
                        if timbb.get('trangthai') == 'thatbai':
                            JobFail += 1
                            print(f'{trang}[{do}ERROR{trang}] {trang}Không Tìm Thấy Id Nào', '            ', end="\r")
                        else:
                            id, name = timbb['id'], timbb['name']
                            ketban = fb.ketban(id)
                            if ketban.get('trangthai') == 'thanhcong':
                                nextDelay, timejob = True, datetime.now().strftime('%H:%M:%S')
                                JobSuccess += 1
                                stt += 1
                                print(f"{xam} ┃ {cam}[{stt}] {xam} ┃ {xam} {trangnhat}{timejob} {xam} ┃ {xam} {camnhat}KẾT BẠN{xam}  ┃ {xam} {lamnhat}{name}")
                            else:
                                JobFail += 1
                                print(f'{trang}[{do}ERROR{trang}] {trang}Không Có Nút Kết Bạn', '            ', end="\r")
                                
                    if JobFail >= 20:
                        check = fb.info()
                        chuyen = xu_ly_loi_taikhoan(check, namefb, listCookie, cookie, fb)
                        if chuyen:
                           break

                    if JobSuccess != 0 and JobSuccess % int(JobBreak) == 0:
                        chuyen = True
                        break

                    if nextDelay == True:
                        if stt % int(JobbBlock)==0:
                            Delay(DelayBlock)
                        else:
                            Delay(delay)

                    if chuyen == True:
                        break
                except:
                    pass
