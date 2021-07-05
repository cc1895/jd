Skip to content
￼￼
Pull requests
Issues
Marketplace
Explore
 
￼ 
cc1895
/
jd
forked from blucewyan/jd
 Watch 
0
￼ Star0 Fork3
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
 main 
jd/collect/dwnc.py / Jump to 
Go to file
￼
cc1895 Update and rename 搜集/dwnc.py to collect/dwnc.py
Latest commit e3915d4 2 minutes ago
 History
 2 contributors
￼￼
89 lines (89 sloc)  2.08 KB
RawBlame
 ￼ ￼
Skip to content
PullsIssuesMarketplace
Explore
 
ycyfff/scripts
 Watch 0
 Star0
 Fork0
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
 main 
scripts/dwnc.py / Jump to 
Go to file
lxgaishiqi 创建 dwnc.py
Latest commit 679c052 2 days ago History
 1 contributor
7146 lines (7056 sloc)  249 KB
RawBlame
  
 CAN_NOTIFY = True 
 import datetime 
 import json 
 import os 
 import random 
 import time 
 from collections import defaultdict 
 from pprint import pprint 
 try: 
 from notify import send 
 except Exception as e: 
 CAN_NOTIFY = False 
 import requests 
   if CAN_NOTIFY: 
 print('启用通知成功', flush=True) 
 else: 
 print('启用通知失败，缺少notify.py', flush=True) 
   class Dwnc: 
 GAME_ID = 'dwnc' 
 VERSION = os.getenv('DWNC_VERSION') if os.getenv('DWNC_VERSION') else '1.1.7' 
 ENV = 'release' 
 IGNORE_URLS = ['/login'] 
   def __init__(self, openid=None, sessid=None, account=None, ua=None): 
 self.ua = ua if ua else 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.7(0x1800072d) NetType/WIFI Language/zh_CN' 
 self.account = account if account else openid 
 self.openid = openid 
 self.sessid = sessid 
 if not self.openid: 
 raise Exception('请检查openid是否填写') 
 if not self.sessid: 
 raise Exception('请检查sessid是否填写') 
 self.first = True 
 self.is_help = False 
 self._cache = {} 
 self.level = 0 
 self.gold = 0 
 self.exp = 0 
 self.coupon = 0 
 self.redpack = 0 
 self.diamond = 0 
 self.cash = 0 
 self.skip_info = {} 
 self.building_info = {} 
 self.skip_list = {} 
 self.seeds_info = {} 
 self.level_info = {} 
 self.task_daily = {} 
 self.helper_info = {} 
 self.task_main = {} 
 self.config = {} 
 self.day_times = defaultdict(int) 
 self.land_info = {} 
 self.land_list = {} 
 self.worker_list = {} 
 self.worker_list2 = {} 
 self.worker_info = {} 
 self.sign_info = {} 
 self.auction_list = {} 
 self.load_setting() 
 self.orders = {} 
 self.warehouse = {} 
 self.can_speed = True 
 self.can_video = True 
 self.can_gold = True 
   def load_settin
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
