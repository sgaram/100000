# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl

sepri = LineClient(authToken='EzlimSU48VWFhDZfzTOc.Uv/0YYcEoAwu5rWj4Sx9Ja.76awAWywQ3Wm8BKsw+6GSHjbat1Ldwsg6Hse5vYH2R0=')
sepri.log("Auth Token : " + str(sepri.authToken))
channel = LineChannel(sepri)
sepri.log("Channel Access Token : " + str(channel.channelAccessToken))

s1 = LineClient(authToken='EzQfDHcR5u78nvBL69Jf.XzmbAwonn5keEY4vw/uKlW.dRbjHH3Gpffd2EMQCXBEDhz8kd5BhGHUlCiYr+XRnLM=')
s1.log("Auth Token : " + str(s1.authToken))
channel1 = LineChannel(s1)
s1.log("Channel Access Token : " + str(channel1.channelAccessToken))

s2 = LineClient(authToken='EzsouIlqOiDjKAS2N7e0.9T/PGPFdadrWbCl3Gzx/Ga.Lpque6IDGJKDcG42Ce1zpRZVCNmkLjvjN6Vy6Q7VxXE=')
s2.log("Auth Token : " + str(s2.authToken))
channel2 = LineChannel(s2)
s2.log("Channel Access Token : " + str(channel2.channelAccessToken))

s3 = LineClient(authToken='EzRmNfRMY5wGyD6Ov6fd.tLlReCirgG96uB+Q5pwO+q.2H8qqx8Lkf+kkZ+6BRa3myg8O3omgzHEuNymqFP1cYg=')
s3.log("Auth Token : " + str(s3.authToken))
channel3 = LineChannel(s3)
s3.log("Channel Access Token : " + str(channel3.channelAccessToken))

s4 = LineClient(authToken='EzlBLrqAU0NMtI6Yhie1.lXZ4ob/KwrCUJfHRJ603qq.oRdUyzXVL0seW08bSNJmc2dJ5vtD4v7obCLIhfw6wKg=')
s4.log("Auth Token : " + str(s4.authToken))
channel4 = LineChannel(s4)
s4.log("Channel Access Token : " + str(channel4.channelAccessToken))

s5 = LineClient(authToken='EzbzYZpAY9si336sPX86.BaiKNxR2VN7zWCBrQS6P5G.tJnreoEm3L33MLux76qeNYBQpUmPOZyRa0Mi30imYeY=')
s5.log("Auth Token : " + str(s5.authToken))
channel5 = LineChannel(s5)
s5.log("Channel Access Token : " + str(channel5.channelAccessToken))

s6 = LineClient(authToken='EzD1CHx8oQUhNSKX0VFa.UHbbg4pHBjT5VwCYtXmXsG.5VDzs0mhlviNmRrt+HSuG9+fRNTqwsgUFmaSJPyRf9w=')
s6.log("Auth Token : " + str(s6.authToken))
channel6 = LineChannel(s6)
s6.log("Channel Access Token : " + str(channel6.channelAccessToken))

s7 = LineClient(authToken='Ez6Q3Q7EN8RSZ0b7nDHa.Oyj1ZAWaMt3CKaVDd5BW2G.Wj4wD5bDBl1SBGJe+F/DCoiP4g7HIOhWTStnR4cWYMA=')
s7.log("Auth Token : " + str(s7.authToken))
channel7 = LineChannel(s7)
s7.log("Channel Access Token : " + str(channel7.channelAccessToken))

s8 = LineClient(authToken='EzKqgyd08WOX6luqZHH4.UFxlUs4U2EOQjGvMmvWMDa.JlHIITF/iFUxCLpxyFarYO7lGiNIfzvSWSpJTnlpOsE=')
s8.log("Auth Token : " + str(s8.authToken))
channel8 = LineChannel(s8)
s8.log("Channel Access Token : " + str(channel8.channelAccessToken))

s9 = LineClient(authToken='EzrWhVPB4nD1N1HsSdl4.9UGdRKZXRTi7Enfms1+LPa.YuRTeVNcboLrB9EwyXJSBv1pKD4JHvCVcn1BwtSGObE=')
s9.log("Auth Token : " + str(s9.authToken))
channel9 = LineChannel(s9)
s9.log("Channel Access Token : " + str(channel9.channelAccessToken))

sw = LineClient(authToken='EzQTwbLwOZOz8DfjCQIb.zr+MvMh78HjcGGT1M17UEW.poh7WtFa/ZAWw8KAamqL4RxPH6+LBa4OCUxwS7BeAB4=')
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))

#FankZher Bot
poll = LinePoll(sepri)
call = sepri
creator = ["u9f09cfcb17d037e2936b751bd9d40ead"]
owner = ["u9f09cfcb17d037e2936b751bd9d40ead"]
admin = ["u9f09cfcb17d037e2936b751bd9d40ead"]
staff = ["ud2fd60fc6e5401101a5f50118dd4118c"]
mid = sepri.getProfile().mid
Amid = s1.getProfile().mid
Bmid = s2.getProfile().mid
Cmid = s3.getProfile().mid
Dmid = s4.getProfile().mid
Emid = s5.getProfile().mid
Fmid = s6.getProfile().mid
Gmid = s7.getProfile().mid
Hmid = s8.getProfile().mid
Imid = s9.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [sepri,s1,s2,s3,s4,s5,s6,s7,s8,s9]
ABC = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Zmid]
sepri = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []

welcome = []
simisimi = []
translateen = []
translateid = []
translateth = []
translatetw = []
translatear = []

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

sepProfile = sepri.getProfile()
myProfile["displayName"] = sepProfile.displayName
myProfile["statusMessage"] = sepProfile.statusMessage
myProfile["pictureStatus"] = sepProfile.pictureStatus

responsename1 = sepri.getProfile().displayName
responsename2 = s1.getProfile().displayName
responsename3 = s2.getProfile().displayName
responsename4 = s3.getProfile().displayName
responsename5 = s4.getProfile().displayName
responsename6 = s5.getProfile().displayName
responsename7 = s6.getProfile().displayName
responsename8 = s7.getProfile().displayName
responsename9 = s8.getProfile().displayName
responsename10 = s9.getProfile().displayName

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)    

Setbot1 = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot1)
Setbot2 = codecs.open("settings.json","r","utf-8")
settings = json.load(Setbot2)
Setbot3 = codecs.open("wait.json","r","utf-8")
wait = json.load(Setbot3)
Setbot4 = codecs.open("read.json","r","utf-8")
read = json.load(Setbot4)

mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def backupData():
    try:
        backup1 = Setmain
        f = codecs.open('setting.json','w','utf-8')
        json.dump(backup1, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup2 = settings
        f = codecs.open('settings.json','w','utf-8')
        json.dump(backup2, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup3 = wait
        f = codecs.open('wait.json','w','utf-8')
        json.dump(backup3, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup4 = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup4, f, sort_keys=True, indent=4, ensure_ascii=False)        
        return True
    except Exception as error:
        logError(error)
        return False     

def restartBot():
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention Userã{}ã\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider Userã{}ã\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masukã{}ã\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = sepri.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nDi group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member baperã{}ã\nByee  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = sepri.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["leave"]+"\nDari group "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\nâââ[ {} ]".format(str(sepri.getGroup(to).name))
                except:
                    no = "\nâââ[ Success ]"
        sepri.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))        

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = sepri.getAllContactIds()
        gid = sepri.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"â Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nð Group : "+str(len(gid))+"\nð Teman : "+str(len(teman))+"\nð Expired : In "+hari+"\nð Version : Python3\nð Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nð Runtime : \n â¢ "+bot
        sepri.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sepri.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "ââââââââââââââââââââââââââââââââ" + "\n" + \
                  "      â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â " + "\n" + \
                  "ââââââââââââââââââââââââââââââââ" + "\n" + \
                  "ââââââââââââââââââââââââââââââââ" + "\n" + \
                  "     â]Â·âªÂ·MenuÂ·âªÂ·[âº" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Help\n" + \
                  "â£â¬â¤ï¸ " + key + "Help bot\n" + \
                  "â£â¬â¤ï¸ " + key + "Translate\n" + \
                  "â£â¬â¤ï¸ " + key + "Meme\n" + \
                  "â£â¬â¤ï¸ " + key + "Me\n" + \
                  "â£â¬â¤ï¸ " + key + "Mymid\n" + \
                  "â£â¬â¤ï¸ " + key + "Midã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Info ã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Kick1 ã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Mybot\n" + \
                  "â£â¬â¤ï¸ " + key + "Status\n" + \
                  "â£â¬â¤ï¸ " + key + "Status translate\n" + \
                  "â£â¬â¤ï¸ " + key + "About\n" + \
                  "â£â¬â¤ï¸ " + key + "Restart\n" + \
                  "â£â¬â¤ï¸ " + key + "Runtime\n" + \
                  "â£â¬â¤ï¸ " + key + "Creator\n" + \
                  "â£â¬â¤ï¸ " + key + "Respon\n" + \
                  "â£â¬â¤ï¸ " + key + "Speed/Sp\n" + \
                  "â£â¬â¤ï¸ " + key + "Sprespon\n" + \
                  "â£â¬â¤ï¸ " + key + ".Tagall\n" + \
                  "â£â¬â¤ï¸ " + key + "Joinall\n" + \
                  "â£â¬â¤ï¸ " + key + "Byeall\n" + \
                  "â£â¬â¤ï¸ " + key + "Ginfo\n" + \
                  "â£â¬â¤ï¸ " + key + "Open\n" + \
                  "â£â¬â¤ï¸ " + key + "Close\n" + \
                  "â£â¬â¤ï¸ " + key + "Url grup\n" + \
                  "â£â¬â¤ï¸ " + key + "Reject\n" + \
                  "â£â¬â¤ï¸ " + key + "Gruplist\n" + \
                  "â£â¬â¤ï¸ " + key + "Infogrupãangkaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Infomemãangkaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Lurkingãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Lurkers\n" + \
                  "â£â¬â¤ï¸ " + key + ".Siderãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot1foto\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot2foto\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot3foto\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot4foto\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot5foto\n" + \
                  "â£â¬â¤ï¸ " + key + "Mykey\n" + \
                  "â£â¬â¤ï¸ " + key + "Resetkey\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "     âªÂ·HiburanÂ·âª" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot1name:\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot2name:\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot3name:\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot4name:\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot5name:\n" + \
                  "â£â¬â¤ï¸ " + key + "Meme@Nama@Teks1@Teks2\n" + \
                  "â£â¬â¤ï¸ " + key + "Ytmp4:ãJudul Video\n" + \
                  "â£â¬â¤ï¸ " + key + "Profilesmule:ãID Smuleã\n" + \
                  "â£â¬â¤ï¸ " + key + "Randomnumber:ãNmor-Nmorã\n" + \
                  "â£â¬â¤ï¸ " + key + "Gimage:ãKeywordã\n" + \
                  "â£â¬â¤ï¸ " + key + "Img food:ãNama Makananã\n" + \
                  "â£â¬â¤ï¸ " + key + "Cekig:ãID IGã\n" + \
                  "â£â¬â¤ï¸ " + key + "Profileig:ãNama IGã\n" + \
                  "â£â¬â¤ï¸ " + key + "Cekdate:ãtgl-bln-thnã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamtag:ãjumlahnyaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamtagã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamcall:ãjumlahnyaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamcall\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "     âªÂ·ProtectÂ·âª" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Notagãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Allproãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Protecturlãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Protectjoinãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Protectkickãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Protectcancelãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Protectinviteãon/offã\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "     âªÂ·SettingsÂ·âª" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Unsendãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Jointicketãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Stickerãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Responãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Respongiftãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Contactãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Autojoinãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Autoaddãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Welcomeãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Simiãon/offã\n" + \
                  "â£â¬â¤ï¸ " + key + "Autoleaveãon/offã\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "     âªÂ·AdminÂ·âª" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Admin:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Admin:delete\n" + \
                  "â£â¬â¤ï¸ " + key + "Staff:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Staff:delete\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot:delete\n" + \
                  "â£â¬â¤ï¸ " + key + "Adminaddã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Admindellã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Staffaddã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Staffdellã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Botaddã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Botdellã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Refresh\n" + \
                  "â£â¬â¤ï¸ " + key + "Listbot\n" + \
                  "â£â¬â¤ï¸ " + key + "Listadmin\n" + \
                  "â£â¬â¤ï¸ " + key + "Listprotect\n" + \
                  "â£â¬â¤ï¸ Ketikã Refresh ãJika Sudah\nâ£â¬â¤ï¸ Menggunakan Command Diatas...\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "      â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â " + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â]PROTECTION" + "\n" + \
                  "ââââââââââââââââââââââââââââââââ"
    return helpMessage
    
    

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "ââââââââââââââââââââââââââââââââ" + "\n" + \
                  "     â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â  " + "\n" + \
                  "ââââââââââââââââââââââââââââââââ" + "\n" + \
                  "ââââââââââââââââââââââââââââââââ" + "\n" + \
                  "     âªÂ·BOTÂ·âª" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Mytoken\n" + \
                  "â£â¬â¤ï¸ " + key + "Cek sider\n" + \
                  "â£â¬â¤ï¸ " + key + "Cek spam\n" + \
                  "â£â¬â¤ï¸ " + key + "Cek pesan\n" + \
                  "â£â¬â¤ï¸ " + key + "Cek respon\n" + \
                  "â£â¬â¤ï¸ " + key + "Cek welcome\n" + \
                  "â£â¬â¤ï¸ " + key + "Cek leave\n" + \
                  "â£â¬â¤ï¸ " + key + "Set sider:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "Set spam:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "Set pesan:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "Set respon:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "Set welcome:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "Set leave:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "Myname:ãNamaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot1name:ãNamaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot2name:ãNamaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot1upãKirim fotonyaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Bot2upãKirim fotonyaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Gift:ãMid korbanããJumlahã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spam:ãMid korbanããJumlahã\n" + \
				  "â£â¬â¤ï¸ " + key + "Spamtag:ãjumlahnyaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamtagã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamcall:ãjumlahnyaã\n" + \
                  "â£â¬â¤ï¸ " + key + "Spamcall\n" + \
				  "â£â¬â¤ï¸ " + key + "Updatefoto\n" + \
                  "â£â¬â¤ï¸ " + key + "Updategrup\n" + \
                  "â£â¬â¤ï¸ " + key + "Updatebot\n" + \
                  "â£â¬â¤ï¸ " + key + "Broadcast:ãTextã\n" + \
                  "â£â¬â¤ï¸ " + key + "SetkeyãNew Keyã\n" + \
                  "â£â¬â¤ï¸ " + key + "Mykey\n" + \
                  "â£â¬â¤ï¸ " + key + "Resetkey\n" + \
				  "â£â¬â¤ï¸ " + key + "Selfãon/offã\n" + \
				  "â£â¬â¤ï¸ " + key + "Hapus chat\n" + \
                  "â£â¬â¤ï¸ " + key + "Remove chat\n" + \
				  "â£â¬â¤ï¸ " + key + "Leave:ãNamagrupã\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "     âªÂ·BlacklistÂ·âª" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£â¬â¤ï¸ " + key + "Blc\n" + \
                  "â£â¬â¤ï¸ " + key + "Ban:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Unban:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Banã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Unbanã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Talkbanã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Untalkbanã@ã\n" + \
                  "â£â¬â¤ï¸ " + key + "Talkban:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Untalkban:on\n" + \
                  "â£â¬â¤ï¸ " + key + "Banlist\n" + \
                  "â£â¬â¤ï¸ " + key + "Talkbanlist\n" + \
                  "â£â¬â¤ï¸ " + key + "Clearban\n" + \
                  "â£â¬â¤ï¸ " + key + "Refresh\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "      â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â " + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                  "â]PROTECTION" + "\n" + \
                  "ââââââââââââââââââââââââââââââââ"
    return helpMessage1
    
def infomeme():
    helpMessage2 = """
ââââââââââââââââââââââââââââââââ
       â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â 
ââââââââââââââââââââââââââââââââ
ââââââââââââââââââââââââââââââââ
    âªÂ·List MemeÂ·âª
â£âââââââââââââââââââââââââââââââ
â£â¬â¤ï¸ Buzz
â£â¬â¤ï¸ Spongebob
â£â¬â¤ï¸ Patrick
â£â¬â¤ï¸ Doge
â£â¬â¤ï¸ Joker
â£â¬â¤ï¸ Xzibit
â£â¬â¤ï¸ You_tried
â£â¬â¤ï¸ cb
â£â¬â¤ï¸ blb
â£â¬â¤ï¸ wonka
â£â¬â¤ï¸ keanu
â£â¬â¤ï¸ cryingfloor
â£â¬â¤ï¸ disastergirl
â£â¬â¤ï¸ facepalm
â£â¬â¤ï¸ fwp
â£â¬â¤ï¸ grumpycat
â£â¬â¤ï¸ captain
â£â¬â¤ï¸ mmm
â£â¬â¤ï¸ rollsafe
â£â¬â¤ï¸ sad-obama
â£â¬â¤ï¸ sad-clinton
â£â¬â¤ï¸ aag
â£â¬â¤ï¸ sarcasticbear
â£â¬â¤ï¸ sk
â£â¬â¤ï¸ sparta
â£â¬â¤ï¸ sad
â£â¬â¤ï¸ contoh:
â£â¬â¤ï¸ Meme@buzz@lu tau?@gatau
â£âââââââââââââââââââââââââââââââ
      â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â 
â£âââââââââââââââââââââââââââââââ
â£âââââââââââââââââââââââââââââââ
â]PROTECTION
ââââââââââââââââââââââââââââââââ
"""
    return helpMessage2
    
def translate():
    helpTranslate =    "ââââââââââââââââââââââââââââââââ" + "\n" + \
                       "     â¢ââªÍÍ¡âFunkZherâªÍÍ¡ââ¬â¤ï¸Â " + "\n" + \
                       "ââââââââââââââââââââââââââââââââ" + "\n" + \
                       "ââââââââââââââââââââââââââââââââ" + "\n" + \
                       "     â]Â·âªÂ·TranslateÂ·âªÂ·[âº" + "\n" + \
                       "â£âââââââââââââââââââââââââââââââ" + "\n" + \
	                   "â£â¬â¤ï¸ Autotransãen-on/en-offã\n" + \
                       "â£â¬â¤ï¸ Autotransãid-on/id-offã\n" + \
                       "â£â¬â¤ï¸ Autotransãth-on/th-offã\n" + \
                       "â£â¬â¤ï¸ Autotransãtw-on/tw-offã\n" + \
                       "â£â¬â¤ï¸ Autotransãar-on/ar-offã\n" + \
                       "â£â¬â¤ï¸ af : afrikaans" + "\n" + \
                       "â£â¬â¤ï¸ sq : albanian" + "\n" + \
                       "â£â¬â¤ï¸ am : amharic" + "\n" + \
                       "â£â¬â¤ï¸ ar : arabic" + "\n" + \
                       "â£â¬â¤ï¸ hy : armenian" + "\n" + \
                       "â£â¬â¤ï¸ az : azerbaijani" + "\n" + \
                       "â£â¬â¤ï¸ eu : basque" + "\n" + \
                       "â£â¬â¤ï¸ be : belarusian" + "\n" + \
                       "â£â¬â¤ï¸ bn : bengali" + "\n" + \
                       "â£â¬â¤ï¸ bs : bosnian" + "\n" + \
                       "â£â¬â¤ï¸ bg : bulgarian" + "\n" + \
                       "â£â¬â¤ï¸ ca : catalan" + "\n" + \
                       "â£â¬â¤ï¸ ceb : cebuano" + "\n" + \
                       "â£â¬â¤ï¸ ny : chichewa" + "\n" + \
                       "â£â¬â¤ï¸ zh-cn : chinese (simplified)" + "\n" + \
                       "â£â¬â¤ï¸ zh-tw : chinese (traditional)" + "\n" + \
                       "â£â¬â¤ï¸ co : corsican" + "\n" + \
                       "â£â¬â¤ï¸ hr : croatian" + "\n" + \
                       "â£â¬â¤ï¸ cs : czech" + "\n" + \
                       "â£â¬â¤ï¸ da : danish" + "\n" + \
                       "â£â¬â¤ï¸ nl : dutch" + "\n" + \
                       "â£â¬â¤ï¸ en : english" + "\n" + \
                       "â£â¬â¤ï¸ eo : esperanto" + "\n" + \
                       "â£â¬â¤ï¸ et : estonian" + "\n" + \
                       "â£â¬â¤ï¸ tl : filipino" + "\n" + \
                       "â£â¬â¤ï¸ fi : finnish" + "\n" + \
                       "â£â¬â¤ï¸ fr : french" + "\n" + \
                       "â£â¬â¤ï¸ fy : frisian" + "\n" + \
                       "â£â¬â¤ï¸ gl : galician" + "\n" + \
                       "â£â¬â¤ï¸ ka : georgian" + "\n" + \
                       "â£â¬â¤ï¸ de : german" + "\n" + \
                       "â£â¬â¤ï¸ el : greek" + "\n" + \
                       "â£â¬â¤ï¸ gu : gujarati" + "\n" + \
                       "â£â¬â¤ï¸ ht : haitian creole" + "\n" + \
                       "â£â¬â¤ï¸ ha : hausa" + "\n" + \
                       "â£â¬â¤ï¸ haw : hawaiian" + "\n" + \
                       "â£â¬â¤ï¸ iw : hebrew" + "\n" + \
                       "â£â¬â¤ï¸ hi : hindi" + "\n" + \
                       "â£â¬â¤ï¸ hmn : hmong" + "\n" + \
                       "â£â¬â¤ï¸ hu : hungarian" + "\n" + \
                       "â£â¬â¤ï¸ is : icelandic" + "\n" + \
                       "â£â¬â¤ï¸ ig : igbo" + "\n" + \
                       "â£â¬â¤ï¸ id : indonesian" + "\n" + \
                       "â£â¬â¤ï¸ ga : irish" + "\n" + \
                       "â£â¬â¤ï¸ it : italian" + "\n" + \
                       "â£â¬â¤ï¸ ja : japanese" + "\n" + \
                       "â£â¬â¤ï¸ jw : javanese" + "\n" + \
                       "â£â¬â¤ï¸ kn : kannada" + "\n" + \
                       "â£â¬â¤ï¸ kk : kazakh" + "\n" + \
                       "â£â¬â¤ï¸ km : khmer" + "\n" + \
                       "â£â¬â¤ï¸ ko : korean" + "\n" + \
                       "â£â¬â¤ï¸ ku : kurdish (kurmanji)" + "\n" + \
                       "â£â¬â¤ï¸ ky : kyrgyz" + "\n" + \
                       "â£â¬â¤ï¸ lo : lao" + "\n" + \
                       "â£â¬â¤ï¸ la : latin" + "\n" + \
                       "â£â¬â¤ï¸ lv : latvian" + "\n" + \
                       "â£â¬â¤ï¸ lt : lithuanian" + "\n" + \
                       "â£â¬â¤ï¸ lb : luxembourgish" + "\n" + \
                       "â£â¬â¤ï¸ mk : macedonian" + "\n" + \
                       "â£â¬â¤ï¸ mg : malagasy" + "\n" + \
                       "â£â¬â¤ï¸ ms : malay" + "\n" + \
                       "â£â¬â¤ï¸ ml : malayalam" + "\n" + \
                       "â£â¬â¤ï¸ mt : maltese" + "\n" + \
                       "â£â¬â¤ï¸ mi : maori" + "\n" + \
                       "â£â¬â¤ï¸ mr : marathi" + "\n" + \
                       "â£â¬â¤ï¸ mn : mongolian" + "\n" + \
                       "â£â¬â¤ï¸ my : myanmar (burmese)" + "\n" + \
                       "â£â¬â¤ï¸ ne : nepali" + "\n" + \
                       "â£â¬â¤ï¸ no : norwegian" + "\n" + \
                       "â£â¬â¤ï¸ ps : pashto" + "\n" + \
                       "â£â¬â¤ï¸ fa : persian" + "\n" + \
                       "â£â¬â¤ï¸ pl : polish" + "\n" + \
                       "â£â¬â¤ï¸ pt : portuguese" + "\n" + \
                       "â£â¬â¤ï¸ pa : punjabi" + "\n" + \
                       "â£â¬â¤ï¸ ro : romanian" + "\n" + \
                       "â£â¬â¤ï¸ ru : russian" + "\n" + \
                       "â£â¬â¤ï¸ sm : samoan" + "\n" + \
                       "â£â¬â¤ï¸ gd : scots gaelic" + "\n" + \
                       "â£â¬â¤ï¸ sr : serbian" + "\n" + \
                       "â£â¬â¤ï¸ st : sesotho" + "\n" + \
                       "â£â¬â¤ï¸ sn : shona" + "\n" + \
                       "â£â¬â¤ï¸ sd : sindhi" + "\n" + \
                       "â£â¬â¤ï¸ si : sinhala" + "\n" + \
                       "â£â¬â¤ï¸ sk : slovak" + "\n" + \
                       "â£â¬â¤ï¸ sl : slovenian" + "\n" + \
                       "â£â¬â¤ï¸ so : somali" + "\n" + \
                       "â£â¬â¤ï¸ es : spanish" + "\n" + \
                       "â£â¬â¤ï¸ su : sundanese" + "\n" + \
                       "â£â¬â¤ï¸ sw : swahili" + "\n" + \
                       "â£â¬â¤ï¸ sv : swedish" + "\n" + \
                       "â£â¬â¤ï¸ tg : tajik" + "\n" + \
                       "â£â¬â¤ï¸ ta : tamil" + "\n" + \
                       "â£â¬â¤ï¸ te : telugu" + "\n" + \
                       "â£â¬â¤ï¸ th : thai" + "\n" + \
                       "â£â¬â¤ï¸ tr : turkish" + "\n" + \
                       "â£â¬â¤ï¸ uk : ukrainian" + "\n" + \
                       "â£â¬â¤ï¸ ur : urdu" + "\n" + \
                       "â£â¬â¤ï¸ uz : uzbek" + "\n" + \
                       "â£â¬â¤ï¸ vi : vietnamese" + "\n" + \
                       "â£â¬â¤ï¸ cy : welsh" + "\n" + \
                       "â£â¬â¤ï¸ xh : xhosa" + "\n" + \
                       "â£â¬â¤ï¸ yi : yiddish" + "\n" + \
                       "â£â¬â¤ï¸ yo : yoruba" + "\n" + \
                       "â£â¬â¤ï¸ zu : zulu" + "\n" + \
                       "â£â¬â¤ï¸ fil : Filipino" + "\n" + \
                       "â£â¬â¤ï¸ he : Hebrew" + "\n" + \
                       "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                       "  Contoh: tr sepriche" + "\n" + \
                       "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                       "â£âââââââââââââââââââââââââââââââ" + "\n" + \
                       "â]Â·âªline.me/ti/p/~sepriche" + "\n" + \
                       "ââââââââââââââââââââââââââââââââ"
    return helpTranslate

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                wait["blacklist"][op.param2] = True
                try:
                    if sepri.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            sepri.reissueGroupTicket(op.param1)
                            X = sepri.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            sepri.updateGroup(X)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if s1.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                s1.reissueGroupTicket(op.param1)
                                X = s1.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                s1.updateGroup(X)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if s2.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    s2.reissueGroupTicket(op.param1)
                                    X = s2.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    s2.updateGroup(X)
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if s3.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        s3.reissueGroupTicket(op.param1)
                                        X = s3.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        s3.updateGroup(X)
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if s4.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            s4.reissueGroupTicket(op.param1)
                                            X = s4.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            s4.updateGroup(X)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if s1.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                s1.reissueGroupTicket(op.param1)
                                                X = s1.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                s1.updateGroup(X)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                                                
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
                        sepri.leaveGroup(op.param1)
                    else:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
                    else:
                        sepri.acceptGroupInvitation(op.param1)
                        ginfo = sepri.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s1.acceptGroupInvitation(op.param1)
                        ginfo = s1.getGroup(op.param1)
                        s1.leaveGroup(op.param1)
                    else:
                        s1.acceptGroupInvitation(op.param1)
                        ginfo = s1.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s2.acceptGroupInvitation(op.param1)
                        ginfo = s2.getGroup(op.param1)
                        s2.leaveGroup(op.param1)
                    else:
                        s2.acceptGroupInvitation(op.param1)
                        ginfo = s2.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s3.acceptGroupInvitation(op.param1)
                        ginfo = s3.getGroup(op.param1)
                        s3.leaveGroup(op.param1)
                    else:
                        s3.acceptGroupInvitation(op.param1)
                        ginfo = s3.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s4.acceptGroupInvitation(op.param1)
                        ginfo = s4.getGroup(op.param1)
                        s4.leaveGroup(op.param1)
                    else:
                        s4.acceptGroupInvitation(op.param1)
                        ginfo = s4.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s5.acceptGroupInvitation(op.param1)
                        ginfo = s5.getGroup(op.param1)
                    else:
                        s5.acceptGroupInvitation(op.param1)
                        ginfo = s5.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s6.acceptGroupInvitation(op.param1)
                        ginfo = s6.getGroup(op.param1)
                        s6.leaveGroup(op.param1)
                    else:
                        s6.acceptGroupInvitation(op.param1)
                        ginfo = s6.getGroup(op.param1)
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s7.acceptGroupInvitation(op.param1)
                        ginfo = s7.getGroup(op.param1)
                        s7.leaveGroup(op.param1)
                    else:
                        s7.acceptGroupInvitation(op.param1)
                        ginfo = s7.getGroup(op.param1)
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s8.acceptGroupInvitation(op.param1)
                        ginfo = s8.getGroup(op.param1)
                        s8.leaveGroup(op.param1)
                    else:
                        s8.acceptGroupInvitation(op.param1)
                        ginfo = s8.getGroup(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        s9.acceptGroupInvitation(op.param1)
                        ginfo = s9.getGroup(op.param1)
                        s9.leaveGroup(op.param1)
                    else:
                        s9.acceptGroupInvitation(op.param1)
                        ginfo = s9.getGroup(op.param1)

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = sepri.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            group = s1.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(KAC).cancelGroupInvitation(op.param1,[_mid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = sepri.getGroup(op.param1)
                contact = sepri.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leaveMembers(op.param1, [op.param2])
                sepri.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = sepri.getGroup(op.param1)
                contact = sepri.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                sepri.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = sepri.getGroup(op.param1)
                contact = sepri.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                welcomeMembers(op.param1, [op.param2])
                sepri.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        s2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            s3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                s4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    s5.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        s6.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            s7.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        sepri.sendMessage(op.param1, wait["message"])

#===========KICK============#
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass
                
#===========Cancel============#

        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Bots:    
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            s1.findAndAddContactsByMid(op.param1,[Zmid])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            s1.inviteIntoGroup(op.param1,[Zmid])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                s2.findAndAddContactsByMid(op.param1,[Zmid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                s2.inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        sepri.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

        if op.type == 19:
            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s5.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s6.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s7.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s8.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        s9.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                            s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                            G= random.choice(KAC).getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).updateGroup(G)
                        except:
                            pass
                return

            if Amid + Bmid + Cmid + Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    try:
                        sepri.inviteIntoGroup(op.param1,[op.param3])
                        s1.acceptGroupInvitation(op.param1)
                        s2.acceptGroupInvitation(op.param1)
                        s3.acceptGroupInvitation(op.param1)
                        s4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            sepri.inviteIntoGroup(op.param1,[op.param3])
                            s1.acceptGroupInvitation(op.param1)
                            s2.acceptGroupInvitation(op.param1)
                            s3.acceptGroupInvitation(op.param1)
                            s4.acceptGroupInvitation(op.param1)
                        except:
                            pass
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        s1.findAndAddContactsByMid(op.param1,admin)
                        s1.inviteIntoGroup(op.param1,admin)
                        s1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            s2.findAndAddContactsByMid(op.param1,admin)
                            s2.inviteIntoGroup(op.param1,admin)
                            s2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        s1.findAndAddContactsByMid(op.param1,staff)
                        s1.inviteIntoGroup(op.param1,staff)
                        s1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            s4.findAndAddContactsByMid(op.param1,staff)
                            s4.inviteIntoGroup(op.param1,staff)
                            s4.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["seprireadPoint"]:
                   if op.param2 in Setmain["seprireadMember"][op.param1]:
                       pass
                   else:
                       Setmain["seprireadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = sepri.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = sepri.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        sepri.sendImageWithURL(op.param1, image)                        
                    
        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = sepri.getGroup(at)
                                sepri = sepri.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "ã Gambar Dihapus ã\nâ¢ Pengirim : "
                                ret_ = "â¢ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\nâ¢ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(sepri.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':sepri.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                sepri.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                sepri.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = sepri.getGroup(at)
                                sepri = sepri.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "âªÍÍ¡ââ¬â¤ï¸Â ã Pesan Dihapus ã\n"
                                ret_ += "âªÍÍ¡ââ¬â¤ï¸Â  Pengirim : {}".format(str(sepri.displayName))
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                sepri.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = sepri.getGroup(at)
                                sepri = sepri.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "ã Sticker Dihapus ã\n"
                                ret_ += "â¢ Pengirim : {}".format(str(sepri.displayName))
                                ret_ += "\nâ¢ Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\nâ¢ Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                sepri.sendMessage(at, str(ret_))
                                sepri.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message                    
               if msg.to in simisimi:
                   try:
                       if msg.text is not None:
                           simi = msg.text
                           r = requests.get("http://corrykalam.pw/api/chatbot.php?text="+simi)
                           data = r.text
                           data = json.loads(data)
                           if data["status"] == 200:
                               sepri.sendMessage(msg.to, str(data["answer"])) 
                   except Exception as error:
                       pass
                   
               if msg.to in translateen:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='en')
                           A = hasil.text
                           sepri.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                           
                           
               if msg.to in translateid:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='id')
                           A = hasil.text
                           sepri.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translateth:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='th')
                           A = hasil.text
                           sepri.sendMessage(msg.to, A)
                   except Exception as error:
                       pass
                   
               if msg.to in translatetw:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='zh-tw')
                           A = hasil.text
                           sepri.sendMessage(msg.to, A)
                   except Exception as error:
                       pass 
                   
               if msg.to in translatear:
                   try:
                       if msg.text is not None:
                           kata = msg.text                           
                           translator = Translator()
                           hasil = translator.translate(kata, dest='ar')
                           A = hasil.text
                           sepri.sendMessage(msg.to, A)
                   except Exception as error:
                       pass                    

        if op.type == 25 or op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sepri.sendMessage(msg.to, wait["Respontag"])
                           sepri.sendMessage(msg.to, None, contentMetadata={"STKID":"72417427","STKPKGID":"4351989","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentiongift"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           idth = ["a0768339-c2d3-4189-9653-2909e9bb6f58","ec4a14ea-7437-407b-aee7-96b1cbbc1b4b","f35bd31f-5ec7-4b2f-b659-92adf5e3d151","ba1d5150-3b5f-4768-9197-01a3f971aa34","2b4ccc45-7309-47fe-a006-1a1edb846ddb","168d03c3-dbc2-456f-b982-3d6f85f52af2","d4f09a5f-29df-48ac-bca6-a204121ea165","517174f2-1545-43b9-a28f-5777154045a6","762ecc71-7f71-4900-91c9-4b3f213d8b26","2df50b22-112d-4f21-b856-f88df2193f9e"]
                           plihth = random.choice(idth)
                           jenis = ["5","6","7","8"]
                           plihjenis = random.choice(jenis)
                           sepri.sendMessage(msg.to, "sukses send gift\nððð.")
                           sepri.sendMessage(msg._from, None, contentMetadata={"PRDID":plihth,"PRDTYPE":"THEME","MSGTPL":plihjenis}, contentType=9)
                           break                       
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sepri.sendMessage(msg.to, "oit...")
                           sepri.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,"ãCek ID Stickerã\nð STKID : " + msg.contentMetadata["STKID"] + "\nâªÍÍ¡ââ¬â¤ï¸Â  STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nâªÍÍ¡ââ¬â¤ï¸Â  STKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = sepri.getContact(msg.contentMetadata["mid"])
                        path = sepri.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  Nama : " + msg.contentMetadata["displayName"] + "\nâªÍÍ¡ââ¬â¤ï¸Â  MID : " + msg.contentMetadata["mid"] + "\nâªÍÍ¡ââ¬â¤ï¸Â  Status : " + contact.statusMessage + "\nâªÍÍ¡ââ¬â¤ï¸Â  Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        sepri.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 0:
                msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                
            if msg.contentType == 1:
                    path = sepri.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
            if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\nã Sticker Info ã"
                   ret_ += "\nâ¢ Sticker ID : {}".format(stk_id)
                   ret_ += "\nâ¢ Sticker Version : {}".format(stk_ver)
                   ret_ += "\nâ¢ Sticker Package : {}".format(pkg_id)
                   ret_ += "\nâ¢ Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = sepri.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
                                                      
                            
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    sepri.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = sepri.getContact(msg.contentMetadata["mid"])
                        path = sepri.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  Nama : " + msg.contentMetadata["displayName"] + "\nâªÍÍ¡ââ¬â¤ï¸Â  MID : " + msg.contentMetadata["mid"] + "\nâªÍÍ¡ââ¬â¤ï¸Â  Status : " + contact.statusMessage + "\nâªÍÍ¡ââ¬â¤ï¸Â  Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        sepri.sendImageWithURL(msg.to, image)
#===========ADD BOT============#
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sepri.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        sepri.sendMessage(msg.to,"Contact itu bukan anggota sepri BOT")
#===========ADD STAFF============#
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        sepri.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        sepri.sendMessage(msg.to,"Contact itu bukan staff")
#===========ADD ADMIN============#
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        sepri.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
               #         sepri.sendMessage(msg.to,"Contact itu jago desah")
#===========ADD BLACKLIST============#
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        sepri.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        sepri.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#===========TALKBAN============#
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        sepri.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        sepri.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        sepri.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        sepri.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#===========UPDATE FOTO============#
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = sepri.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            sepri.sendMessage(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = sepri.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     sepri.updateGroupPicture(msg.to, path)
                     sepri.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["seprifoto"]:
                            path = sepri.downloadObjectMsg(msg_id)
                            del Setmain["seprifoto"][mid]
                            sepri.updateProfilePicture(path)
                            sepri.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["seprifoto"]:
                            path = s1.downloadObjectMsg(msg_id)
                            del Setmain["seprifoto"][Amid]
                            s1.updateProfilePicture(path)
                            s1.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = s1.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     s1.updateProfilePicture(path1)
                     s1.sendMessage(msg.to, "Berhasil mengubah foto profile bot")               

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        sepri.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               sepri.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                sepri.sendMessage(msg.to, "âªÍÍ¡ââ¬â¤ï¸Â Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                sepri.sendMessage(msg.to, "âªÍÍ¡ââ¬â¤ï¸Â Selfbot dinonaktifkan")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               sepri.sendMessage(msg.to, str(helpMessage1))
                               
                        elif cmd == "meme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage2 = infomeme()
                               sepri.sendMessage(msg.to, str(helpMessage2))
                               
                        elif cmd == "translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpTranslate = translate()
                               sepri.sendMessage(msg.to, str(helpTranslate))                               
                               
                        if cmd == "unsend on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                sepri.sendMessage(msg.to, "âªÍÍ¡ââ¬â¤ï¸Â Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsend off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                sepri.sendMessage(msg.to, "âªÍÍ¡ââ¬â¤ï¸Â Deteksi Unsend Dinonaktifkan")                                

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ââââââââââââââââââ\nââ           âââ S T A T U S âââ\nââ£ââââââââââââââââââââ\n"
                                if wait["unsend"] == True: md+="âââ¥ â UnsendãONã\n"
                                else: md+="âââ¥ â UnsendãOFFã\n"                                
                                if wait["sticker"] == True: md+="âââ¥ â StickerãONã\n"
                                else: md+="âââ¥ â StickerãOFFã\n"
                                if wait["contact"] == True: md+="âââ¥ â ContactãONã\n"
                                else: md+="âââ¥ â ContactãOFFã\n"
                                if wait["talkban"] == True: md+="âââ¥ â TalkbanãONã\n"
                                else: md+="âââ¥ â TalkbanãOFFã\n"
                                if wait["Mentionkick"] == True: md+="âââ¥ â NotagãONã\n"
                                else: md+="âââ¥ â NotagãOFFã\n"
                                if wait["detectMention"] == True: md+="âââ¥ â ResponãONã\n"
                                else: md+="âââ¥ â ResponãOFFã\n"
                                if wait["Mentiongift"] == True: md+="âââ¥ â RespongiftãONã\n"
                                else: md+="âââ¥ â RespongiftãOFFã\n"                                
                                if wait["autoJoin"] == True: md+="âââ¥ â AutojoinãONã\n"
                                else: md+="âââ¥ â AutojoinãOFFã\n"
                                if settings["autoJoinTicket"] == True: md+="âââ¥ â JointicketãONã\n"
                                else: md+="âââ¥ â JointicketãOFFã\n"                                
                                if wait["autoAdd"] == True: md+="âââ¥ â AutoaddãONã\n"
                                else: md+="âââ¥ â AutoaddãOFFã\n"
                                if msg.to in welcome: md+="âââ¥ â WelcomeãONã\n"
                                else: md+="âââ¥ â WelcomeãOFFã\n"
                                if msg.to in simisimi: md+="âââ¥ â SimisimiãONã\n"
                                else: md+="âââ¥ â SimisimiãOFFã\n"                                
                                if wait["autoLeave"] == True: md+="âââ¥ â AutoleaveãONã\n"
                                else: md+="âââ¥ â AutoleaveãOFFã\n"
                                if msg.to in protectqr: md+="âââ¥ â ProtecturlãONã\n"
                                else: md+="âââ¥ â ProtecturlãOFFã\n"
                                if msg.to in protectjoin: md+="âââ¥ â ProtectjoinãONã\n"
                                else: md+="âââ¥ â ProtectjoinãOFFã\n"
                                if msg.to in protectkick: md+="âââ¥ â ProtectkickãONã\n"
                                else: md+="âââ¥ â ProtectkickãOFFã\n"
                                if msg.to in protectcancel: md+="âââ¥ â ProtectcancelãONã\n"
                                else: md+="âââ¥ â ProtectcancelãOFFã\n"
                                if msg.to in protectinvite: md+="âââ¥ â ProtectinviteãONã\n"
                                else: md+="âââ¥ â ProtectinviteãOFFã\n"                                                
                                sepri.sendMessage(msg.to, md+"ââ£ââââââââââââââââââââ\nââFunkZher Bot\nââProtection\n  ââââââââââââââââââ")
                                
                        elif cmd == "status translate":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ââââââââââââââââââ\nââ â¥ STATUS TRANSLATE â¥\nââ£ââââââââââââââââââââ\n"
                                if msg.to in translateen: md+="âââ¥ â EnglishãONã\n"
                                else: md+="âââ¥ â EnglishãOFFã\n"
                                if msg.to in translateid: md+="âââ¥ â IndonesiaãONã\n"
                                else: md+="âââ¥ â IndonesiaãOFFã\n"
                                if msg.to in translateth: md+="âââ¥ â ThailandãONã\n"
                                else: md+="âââ¥ â ThailandãOFFã\n"
                                if msg.to in translatetw: md+="âââ¥ â TaiwanãONã\n"
                                else: md+="âââ¥ â TaiwanãOFFã\n"
                                if msg.to in translatear: md+="âââ¥ â ArabãONã\n"
                                else: md+="âââ¥ â ArabãOFFã\n"       
                                sepri.sendMessage(msg.to, md+"ââ£ââââââââââââââââââââ\nâââ§ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nâââ§ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n  ââââââââââââââââââ")                                

                        elif cmd == "ayam" or text.lower() == 'ayam':
                            if msg._from in admin:
                                sepri.sendImageWithURL(msg.to,"https://4.bp.blogspot.com/-8ZWMbtQOFxM/WA7F0qzNlWI/AAAAAAAAEpA/D7d8SRk2n1UkVeokgMpVQUWo8fpsXCCEgCLcB/s1600/foto%2Blucu%2Bngakak.jpg") 

                        elif cmd == "funkzher" or text.lower() == 'funkzher':
                            sepri.sendImageWithURL(msg.to,"https://4.bp.blogspot.com/-ep5ISQIVk6g/W_ZiRS6k7AI/AAAAAAAAAQY/rKMINF8byiw0zbC0IH5j7sSgUDXU70zUQCLcBGAs/s1600/PicsArt_11-04-09.02.36.jpg") 
          
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        sepri.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s5.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s6.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s7.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s8.acceptGroupInvitationByTicket(op.param1,Ticket)
                        s9.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        sepri.inviteIntoGroup(op.param1,[Zmid])
                        sepri.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass

                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sepri.kickoutFromGroup(op.param1,[op.param2])
                        sepri.findAndAddContactsByMid(op.param3)
                        sepri.inviteIntoGroup(op.param1,[Zmid])
                        sepri.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        sepri.kickoutFromGroup(op.param1,[op.param2])
                        sepri.findAndAddContactsByMid(op.param3)
                        sepri.inviteIntoGroup(op.param1,[Zmid])
                        sepri.sendMessage(op.param1,"=AntiJS Invited=")
  
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            sepri.kickoutFromGroup(op.param1,[op.param2])
                            sepri.findAndAddContactsByMid(op.param3)
                            sepri.inviteIntoGroup(op.param1,[op.param3])
                            sepri.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass

                        elif cmd == "antijs stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = sepri.getGroup(msg.to)
                                    sepri.inviteIntoGroup(msg.to, [Zmid])
                                    sepri.sendMessage(msg.to,"Grup ã"+str(ginfo.name)+"ã Aman Dari JS")
                                except:
                                    pass

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "Anti JS Diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Anti JS Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS Sudah Tidak Aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)                

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               sepri.sendMessage1(msg)

                        elif text.lower() == "mid":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, msg._from)
                               s1.sendMessage(msg.to, msg._from)
                               s2.sendMessage(msg.to, msg._from)
                               s3.sendMessage(msg.to, msg._from)
                               s4.sendMessage(msg.to, msg._from)
                               s5.sendMessage(msg.to, msg._from)
                               s6.sendMessage(msg.to, msg._from)
                               s7.sendMessage(msg.to, msg._from)
                               s8.sendMessage(msg.to, msg._from)
                               s9.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = sepri.getContact(key1)
                               sepri.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               sepri.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = sepri.getContact(key1)
                               sepri.sendMessage(msg.to, "â§ Nama : "+str(mi.displayName)+"\nð Mid : " +key1+"\nð Status : "+str(mi.statusMessage))
                               sepri.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(sepri.getContact(key1)):
                                   sepri.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   sepri.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               sepri.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               sepri.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   sepri.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   sepri.removeAllMessages(op.param2)
                                   s1.removeAllMessages(op.param2)
                                   s2.removeAllMessages(op.param2)
                                   s3.removeAllMessages(op.param2)
                                   s4.removeAllMessages(op.param2)
                                   s5.removeAllMessages(op.param2)
                                   s6.removeAllMessages(op.param2)
                                   s7.removeAllMessages(op.param2)
                                   s8.removeAllMessages(op.param2)
                                   s9.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = sepri.getGroupIdsJoined()
                               for group in saya:
                                   sepri.sendMessage(group,"=======[BROADCAST]=======\n\n"+pesan+"\n\nCreator : line.me/ti/p/~adit_cmct")

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãMykeyã\nSetkey bot muã " + str(Setmain["keyCommand"]) + " ã")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sepri.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sepri.sendMessage(msg.to, "ãSetkeyã\nSetkey diganti jadiã{}ã".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               sepri.sendMessage(msg.to, "ãSetkeyã\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               sepri.sendMessage(msg.to, "âªÍÍ¡ââ¬â¤ï¸Â Restart Sukses")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               sepri.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = sepri.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(sepri.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sepri.sendMessage(msg.to, "â§ BOT Grup Info\n\n â§ Nama Group : {}".format(G.name)+ "\nð ID Group : {}".format(G.id)+ "\nð Pembuat : {}".format(G.creator.displayName)+ "\nð Waktu Dibuat : {}".format(str(timeCreated))+ "\nð Jumlah Member : {}".format(str(len(G.members)))+ "\nð Jumlah Pending : {}".format(gPending)+ "\nð Group Qr : {}".format(gQr)+ "\nð Group Ticket : {}".format(gTicket))
                                sepri.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                sepri.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sepri.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = sepri.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = sepri.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(sepri.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "âªÍÍ¡ââ¬â¤ï¸Â  BOT Grup Info\n"
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Name : {}".format(G.name)
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  ID : {}".format(G.id)
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Creator : {}".format(gCreator)
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Created Time : {}".format(str(timeCreated))
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Member : {}".format(str(len(G.members)))
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Pending : {}".format(gPending)
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Qr : {}".format(gQr)
                                ret_ += "\nâªÍÍ¡ââ¬â¤ï¸Â  Ticket : {}".format(gTicket)
                                ret_ += ""
                                sepri.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = sepri.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = sepri.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "âªÍÍ¡ââ¬â¤ï¸Â  "+ str(no) + ". " + mem.displayName
                                sepri.sendMessage(to,"âªÍÍ¡ââ¬â¤ï¸Â  Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\nãTotal %i Membersã" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = sepri.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = sepri.getGroup(i)
                                if ginfo == group:
                                    s1.leaveGroup(i)
                                    sepri.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = sepri.getAllContactIds()
                               for i in gid:
                                   G = sepri.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "ââ " + str(a) + ". " +G.displayName+ "\n"
                               sepri.sendMessage(msg.to,"âââ[ FRIEND LIST ]\nââ\n"+ma+"ââ\nâââ[ Totalã"+str(len(gid))+"ãFriends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = sepri.getGroupIdsJoined()
                               for i in gid:
                                   G = sepri.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "ââ " + str(a) + ". " +G.name+ "\n"
                               sepri.sendMessage(msg.to,"âââ[ GROUP LIST ]\nââ\n"+ma+"ââ\nâââ[ Totalã"+str(len(gid))+"ãGroups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = s1.getGroupIdsJoined()
                               for i in gid:
                                   G = s1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "ââ " + str(a) + ". " +G.name+ "\n"
                               s1.sendMessage(msg.to,"âââ[ GROUP LIST ]\nââ\n"+ma+"ââ\nâââ[ Totalã"+str(len(gid))+"ãGroups ]")


                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = s1.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   s1.updateGroup(X)
                                   s1.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = s1.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   s1.updateGroup(X)
                                   s1.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = s1.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      s1.updateGroup(x)
                                   gurl = s1.reissueGroupTicket(msg.to)
                                   s1.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                   
                                   
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                              ginvited = sepri.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      sepri.rejectGroupInvitation(gid)
                                  sepri.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  sepri.sendMessage(to, "Tidak ada undangan yang tertunda")

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sepri.sendMessage(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                s1.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1foto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["seprifoto"][mid] = True
                                sepri.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2foto":
                            if msg._from in admin:
                                Setmain["seprifoto"][Amid] = True
                                s1.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3foto":
                            if msg._from in admin:
                                Setmain["seprifoto"][Bmid] = True
                                s2.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4foto":
                            if msg._from in admin:
                                Setmain["seprifoto"][Cmid] = True
                                s3.sendMessage(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot5foto":
                            if msg._from in admin:
                                Setmain["seprifoto"][Dmid] = True
                                s4.sendMessage(msg.to,"Kirim fotonya.....")
                               

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sepri.getProfile()
                                profile.displayName = string
                                sepri.updateProfile(profile)
                                sepri.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sepri.getProfile()
                                profile.displayName = string
                                sepri.updateProfile(profile)
                                sepri.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = s1.getProfile()
                                profile.displayName = string
                                s1.updateProfile(profile)
                                s1.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = s2.getProfile()
                                profile.displayName = string
                                s2.updateProfile(profile)
                                s2.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = s3.getProfile()
                                profile.displayName = string
                                s3.updateProfile(profile)
                                s3.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = s4.getProfile()
                                profile.displayName = string
                                s4.updateProfile(profile)
                                s4.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == ".tagall" or text.lower() == 'ð':
                          if wait["selfbot"] == True:
                               group = sepri.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, jml = [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  BOT\n\n"+ma+"\nTotalã%sãBOT" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +sepri.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  Admin Funkzher BOT\n\nâªÍÍ¡ââ¬â¤ï¸Â Creator BOT:\n"+ma+"\nâªÍÍ¡ââ¬â¤ï¸Â Admin:\n"+mb+"\nâªÍÍ¡ââ¬â¤ï¸Â Staff:\n"+mc+"\nâªÍÍ¡ââ¬â¤ï¸Â Totalã%sã" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +sepri.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +sepri.getGroup(group).name + "\n"                                    
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  BOT Protection\n\nâªÍÍ¡ââ¬â¤ï¸Â  PROTECT URL :\n"+ma+"\nâªÍÍ¡ââ¬â¤ï¸Â  PROTECT KICK :\n"+mb+"\nâªÍÍ¡ââ¬â¤ï¸Â  PROTECT JOIN :\n"+md+"\nâªÍÍ¡ââ¬â¤ï¸Â  PROTECT CANCEL:\n"+mc+"\nâªÍÍ¡ââ¬â¤ï¸Â  PROTECT INVITE :\n"+me+"\nTotalã%sãProtect yang aktif" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectinvite))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                sepri.sendMessage(msg.to,responsename1)
                                s1.sendMessage(msg.to,responsename2)
                                s2.sendMessage(msg.to,responsename3)
                                s3.sendMessage(msg.to,responsename4)
                                s4.sendMessage(msg.to,responsename5)
                                s5.sendMessage(msg.to,responsename2)
                                s6.sendMessage(msg.to,responsename3)
                                s7.sendMessage(msg.to,responsename4)
                                s8.sendMessage(msg.to,responsename5)
                                s8.sendMessage(msg.to,responsename5)

                        elif cmd == "invite":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
                                    sepri.inviteIntoGroup(msg.to, anggota)
                                    s1.acceptGroupInvitation(msg.to)
                                    s2.acceptGroupInvitation(msg.to)
                                    s3.acceptGroupInvitation(msg.to)
                                    s4.acceptGroupInvitation(msg.to)
                                    s5.acceptGroupInvitation(msg.to)
                                    s6.acceptGroupInvitation(msg.to)
                                    s7.acceptGroupInvitation(msg.to)
                                    s8.acceptGroupInvitation(msg.to)
                                    s9.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
    
                        elif cmd == "joinall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                ginfo = sepri.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                sepri.updateGroup(G)
                                invsend = 0
                                Ticket = sepri.reissueGroupTicket(msg.to)
                                s1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s2.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s3.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s4.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s5.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s6.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s8.acceptGroupInvitationByTicket(msg.to,Ticket)
                                s9.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = s9.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                s9.updateGroup(G)

                        elif cmd == "byeall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                sepri.sendMessage(msg.to, "pasukan pulang")
                                s1.leaveGroup(msg.to)
                                s2.leaveGroup(msg.to)
                                s3.leaveGroup(msg.to)
                                s4.leaveGroup(msg.to)
                                s5.leaveGroup(msg.to)
                                s6.leaveGroup(msg.to)
                                s7.leaveGroup(msg.to)
                                s8.leaveGroup(msg.to)
                                s9.leaveGroup(msg.to)

                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                sepri.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = sepri.getGroupIdsJoined()
                                for i in gid:
                                    h = sepri.getGroup(i).name
                                    if h == ng:
                                        s1.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        s1.leaveGroup(i)
                                        sepri.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = sepri.getGroup(msg.to)
                                ginfo = sepri.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                sepri.updateGroup(G)
                                invsend = 0
                                Ticket = sepri.reissueGroupTicket(msg.to)
                                s1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = s1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                s1.updateGroup(G)


                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = sepri.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = sepri.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = sepri.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sepri.sendMessage(msg.to, " â§ BOT Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               sepri.sendMessage(msg.to, "speed...")
                               elapsed_time = time.time() - start
                               sepri.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s1.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s2.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s3.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s4.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s5.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s6.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s7.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s8.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               s9.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['seprireadPoint'][msg.to] = msg_id
                                 Setmain['seprireadMember'][msg.to] = {}
                                 sepri.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['seprireadPoint'][msg.to]
                                 del Setmain['seprireadMember'][msg.to]
                                 sepri.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['seprireadPoint']:
                                if Setmain['seprireadMember'][msg.to] != {}:
                                    nad = []
                                    for x in Setmain['seprireadMember'][msg.to]:
                                        nad.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(nad)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in nad:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(nad):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(sepri.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        sepri.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['seprireadPoint'][msg.to]
                                        del Setmain['seprireadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['seprireadPoint'][msg.to] = msg.id
                                    Setmain['seprireadMember'][msg.to] = {}
                                else:
                                    sepri.sendMessage(msg.to, "User kosong...")
                            else:
                                sepri.sendMessage(msg.to, "Ketik lurking on dulu")

                        elif cmd == ".sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sepri.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == ".sider off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sepri.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  sepri.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                                      
                        elif cmd.startswith("musik: "):
                          if msg._from in admin:    
                            try:
                                search = msg.text.replace("musik: ","")
                                r = requests.get("https://farzain.xyz/api/premium/joox.php?apikey=al11241519&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "ã Hasil Musik ã\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                hasil += "\n\nLink : \n3. M4A : {}".format(str(audio["m4a"]))
                                sepri.sendImageWithURL(msg.to, str(data["gambar"]))
                                sepri.sendMessage(msg.to, str(hasil))
                                sepri.sendMessage(msg.to, "Downloading...")
                                sepri.sendMessage(msg.to, "ã Result MP3 ã")
                                sepri.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                sepri.sendMessage(msg.to, "ã Result M4A ã")
                                sepri.sendVideoWithURL(msg.to, str(audio["m4a"]))
                                sepri.sendMessage(msg.to, str(data["lirik"]))
                                sepri.sendMessage(msg.to, "Success Download...")
                            except Exception as error:
                            	sepri.sendMessage(msg.to, "ã Result Error ã\n" + str(error))

                        elif cmd.startswith("randomnumber: "):                            	
                            if msg._from in admin:
                                separate = msg.text.split(" ")
                                angka = msg.text.replace(separate[0] + " ","")  
                                tgb = angka.split("-")
                                num1 = tgb[0]
                                num2 = tgb[1]
                                r = requests.get("https://farzain.xyz/api/random.php?min="+num1+"&max="+num2)
                                data = r.json()
                                sepri.sendMessage(msg.to,"Hasil : "+str(data["url"]))
                                
                                
                        elif cmd.startswith("1cak"):
                          if msg._from in admin:
                              r=requests.get("https://api-1cak.herokuapp.com/random")
                              data=r.text
                              data=json.loads(data)
                              print(data)
                              hasil = "Result :\n"
                              hasil += "\nID : " +str(data["id"])
                              hasil += "\nTitle : " + str(data["title"])
                              hasil += "\nUrl : " + str(data["url"]) 
                              hasil += "\nVotes : " + str(data["votes"])
                              sepri.sendMessage(msg.to, str(hasil))
        
                        elif cmd.startswith("musik2: "):
                          if msg._from in admin:    
                            try:
                                dan = msg.text.replace("musik2: ","")
                                r = requests.get("http://corrykalam.pw/api/joox.php?song={}"+urllib.parse.quote(dan))
                                data = r.json()
                                l = data["lyric"].replace("ti:","Judul: ")
                                i = l.replace("ar:","Penyanyi: ")
                                r = i.replace("al:","Album: ")
                                ii = r.replace("[by:]","")
                                k = ii.replace("[offset:0]","")
                                lirik = k.replace("***Lirik didapat dari pihak ketiga***\n","")
                                sepri.sendImageWithURL(msg.to, data["image"])
                                t = "[ Music ]"
                                t += "\n\nJudul: "+str(data["title"])
                                t+="\nPenyanyi: "+str(data["singer"])
                                t+="\n\n[ Finish ]\n\n"+str(lirik)
                                sepri.sendMessage(msg.to, str(t))
                                sepri.sendAudioWithURL(msg.to, data["url"])
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("playlist "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "ââââ[ List Lagu ]ââââ"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ââ[ Total {} Lagu ]ââ".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \nâ§ã {}Playlist {}:nomor ã ".format(str(),str(search))
                                    ret_ += "\nâ§ã {}Lirik {}:nomor ã ".format(str(),str(search))
                                    sepri.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "âââââ[ Detail Musik ]ââââ"
                                            ret_ += "\nââ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\nââ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\nââ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\nâââ[ Tunggu Audionya ]âââ"
                                            sepri.sendMessage(msg.to, str(ret_))
                                            sepri.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass
                            
                        elif cmd.startswith("lirik "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "ââââ[ List Lirik ]ââââ"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n  ââ[ Total {} Lagu ]ââ".format(str(len(data["results"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \nâ§ã {}Lirik {}:nomor ã".format(str(),str(search))
                                    ret_ += "\nâ§ã {}Playlist {}:nomor ã ".format(str(),str(search))
                                    sepri.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        sepri.sendMessage(msg.to, str(lyric))
                            except Exception as error:
                                pass                                        
        
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        sepri.sendImageWithURL(msg.to, str(food["url"]))
                                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                sepri.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                sepri.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                sepri.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	
                            	
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            sepri.sendImageWithURL(msg.to, image)
          

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nâ§ Author : ' + str(vid.author)
                                    durasi = '\nâ§ Duration : ' + str(vid.duration)
                                    suka = '\nâ§ Likes : ' + str(vid.likes)
                                    rating = '\nâ§ Rating : ' + str(vid.rating)
                                    deskripsi = '\nâ§ Deskripsi : ' + str(vid.description)
                                sepri.sendVideoWithURL(msg.to, me)
                                sepri.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sepri.sendMessage(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nâ§ Author : ' + str(vid.author)
                                    durasi = '\nâ§ Duration : ' + str(vid.duration)
                                    suka = '\nâ§ Likes : ' + str(vid.likes)
                                    rating = '\nâ§ Rating : ' + str(vid.rating)
                                    deskripsi = '\nâ§ Deskripsi : ' + str(vid.description)
                                sepri.sendImageWithURL(msg.to, me)
                                sepri.sendAudioWithURL(msg.to, shi)
                                sepri.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sepri.sendMessage(msg.to,str(e))
                                    
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                sepri.sendMessage(msg.to, detail + user + user1 + followers + following + post + link + details)
                                sepri.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                sepri.sendMessage(msg.to, str(njer))
                                
                        elif cmd.startswith("cekig:"):
                            if msg._from in admin:
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://farzain.xyz/api/ig_profile.php?apikey=arTdnVbJkW1EuzDNQrIxQDvHARIDcQ&id={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "âââ[ Profile Instagram ]"
                                        ret_ += "\nââ Nama : {}".format(str(data["info"]["full_name"]))
                                        ret_ += "\nââ Username : {}".format(str(data["info"]["username"]))
                                        ret_ += "\nââ Bio : {}".format(str(data["info"]["bio"]))
                                        ret_ += "\nââ URL Bio : {}".format(str(data["info"]["url_bio"]))
                                        ret_ += "\nââ Pengikut : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\nââ Diikuti : {}".format(str(data["count"]["followers"]))
                                        ret_ += "\nââ Total Post : {}".format(str(data["count"]["post"]))
                                        ret_ += "\nâââ[ https://www.instagram.com/{} ]".format(search)
                                        path = data["info"]["profile_pict"]
                                        sepri.sendMessage(to, str(ret_))
                                        sepri.sendImageWithURL(to, str(path))
                                except Exception as e:
                                    sepri.sendMessage(msg.to, str(e))                                  

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            sepri.sendMessage(msg.to,"ð I N F O R M A S I ð\n\n"+"ð Date Of Birth : "+lahir+"\nð Age : "+usia+"\nð Ultah : "+ultah+"\nð Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["seprilimit"] = num
                                sepri.sendMessage(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sepri.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["seprilimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                sepri.sendMessage1(msg)
                                            except Exception as e:
                                                sepri.sendMessage(msg.to,str(e))
                                    else:
                                        sepri.sendMessage(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = sepri.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sepri.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        sepri.sendMessage(msg.to,str(e))
                                else:
                                    sepri.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sepri.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}, contentType=9)
                                      s1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      sepri.sendMessage(midd, str(Setmain["seprimessage1"]))
                                      s1.sendMessage(midd, str(Setmain["seprimessage1"]))

                                  
                        elif 'Mybottoken' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in creator:
                               sepri.sendMessage(msg.to,"sepri\n"+sepri.authToken)
                               sepri.sendMessage(msg.to,"KI\n"+s1.authToken)

#==============================================================================# 
                        elif msg.text.lower().startswith("tr-af "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='af')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sq "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sq')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-am "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='am')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ar "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ar')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hy')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-az "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='az')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-eu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='eu')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-be "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='be')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bn')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bs')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-bg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='bg')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ca "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ca')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ceb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ceb')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ny "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ny')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-cn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-cn')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zh-tw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zh-tw')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-co "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='co')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hr')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cs "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cs')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-da "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='da')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-nl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='nl')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-en "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='en')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-et "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='et')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fi')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fr')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fy')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gl')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ka "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ka')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-de "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='de')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-el "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='el')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gu')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ht "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ht')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ha "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ha')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-haw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='haw')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-iw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='iw')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hi')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hmn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hmn')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-hu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='hu')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-is "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='is')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ig "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ig')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-id "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='id')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ga "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ga')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-it "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='it')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ja "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ja')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-jw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='jw')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-kn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='kn')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-kk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='kk')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-km "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='km')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ko "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ko')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ku "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ku')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ky "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ky')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lo "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lo')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-la "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='la')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lv "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lv')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lt')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-lb "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='lb')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mk')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mg')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ms "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ms')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ml "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ml')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mt')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mi')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mr')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-mn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='mn')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-my "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='my')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ne "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ne')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-no "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='no')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ps "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ps')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fa "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fa')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pl')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pt "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pt')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-pa "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='pa')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ro "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ro')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ru "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ru')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sm "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sm')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-gd "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='gd')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sr')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-st "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='st')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sn "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sn')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sd "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sd')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-si "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='si')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sk')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sl "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sl')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-so "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='so')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-es "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='es')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-su "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='su')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sw "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sw')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-sv "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='sv')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-tg "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='tg')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ta "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ta')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-te "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='te')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-th "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='th')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-tr "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='tr')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-uk "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='uk')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-ur "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='ur')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-uz "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='uz')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-vi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='vi')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-cy "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='cy')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-xh "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='xh')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yi "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yi')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-yo "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='yo')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-zu "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='zu')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-fil "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='fil')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)
                        elif msg.text.lower().startswith("tr-he "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:                            
                            sep = text.split(" ")
                            isi = text.replace(sep[0] + " ","")
                            translator = Translator()
                            hasil = translator.translate(isi, dest='he')
                            A = hasil.text
                            sepri.sendMessage(msg.to, A)

#===========Settings============#
                        elif 'Simi ' in msg.text:
                              spl = msg.text.replace('Simi ','')
                              if spl == 'on':
                                  if msg.to in simisimi:
                                       msgs = "Simi-simi sudah aktif"
                                  else:
                                       simisimi.append(msg.to)
                                       ginfo = s1.getGroup(msg.to)
                                       msgs = "Simi-simi Diaktifkan\nDi Group : " +str(ginfo.name)
                                  s1.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in simisimi:
                                         simisimi.remove(msg.to)
                                         ginfo = s1.getGroup(msg.to)
                                         msgs = "Simi-simi Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Simi-simi Sudah Tidak Aktif"
                                    s1.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs) 
                                    
                        elif 'Autotrans th-' in msg.text:
                              spl = msg.text.replace('Autotrans th-','')
                              if spl == 'on':
                                  if msg.to in translateth:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateth.append(msg.to)
                                       ginfo = s1.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  s1.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateth:
                                         translateth.remove(msg.to)
                                         ginfo = s1.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    s1.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)                                    
                                    
                        elif 'Autotrans en-' in msg.text:
                              spl = msg.text.replace('Autotrans en-','')
                              if spl == 'on':
                                  if msg.to in translateen:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateen.append(msg.to)
                                       ginfo = s1.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  s1.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateen:
                                         translateen.remove(msg.to)
                                         ginfo = s1.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    s1.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)
                                    
                        elif 'Autotrans id-' in msg.text:
                              spl = msg.text.replace('Autotrans id-','')
                              if spl == 'on':
                                  if msg.to in translateid:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translateid.append(msg.to)
                                       ginfo = s1.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  s1.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translateid:
                                         translateid.remove(msg.to)
                                         ginfo = s1.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    s1.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)
                                    
                        elif 'Autotrans tw-' in msg.text:
                              spl = msg.text.replace('Autotrans tw-','')
                              if spl == 'on':
                                  if msg.to in translatetw:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatetw.append(msg.to)
                                       ginfo = s1.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  s1.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatetw:
                                         translatetw.remove(msg.to)
                                         ginfo = s1.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    s1.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)
                                    
                        elif 'Autotrans ar-' in msg.text:
                              spl = msg.text.replace('Autotrans ar-','')
                              if spl == 'on':
                                  if msg.to in translatear:
                                       msgs = "Auto Translate sudah aktif"
                                  else:
                                       translatear.append(msg.to)
                                       ginfo = s1.getGroup(msg.to)
                                       msgs = "Auto Translate Diaktifkan\nDi Group : " +str(ginfo.name)
                                  s1.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in translatear:
                                         translatear.remove(msg.to)
                                         ginfo = s1.getGroup(msg.to)
                                         msgs = "Auto Translate Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Auto Translate Sudah Tidak Aktif"
                                    s1.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)                                    

                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "âªÍÍ¡ââ¬â¤ï¸Â Welcome Msg sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)
                                    
#===========Protection============#                                    

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect url sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect join sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)
                                    
                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect invite sudah aktif"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = sepri.getGroup(msg.to)
                                       msgs = "âªÍÍ¡ââ¬â¤ï¸Â Protect invite diaktifkan\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Protect invite dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite sudah tidak aktif"
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)                                                                      

                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectinvite:
                                      msgs = ""
                                  else:
                                      protectinvite.append(msg.to)                                      
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = sepri.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = sepri.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  sepri.sendMessage(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""                                         
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = sepri.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    sepri.sendMessage(msg.to, "ãDinonaktifkanã\n" + msgs)

#===========KICKOUT============#

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin[target] = True
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in creator:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del admin[target]
                                           f=codecs.open('admin.json','w','utf-8')
                                           json.dump(admin, f, sort_keys=True, indent=4,ensure_ascii=False)                                            
                                           sepri.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in sepri:
                                       try:
                                           staff.remove(target)
                                           sepri.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in sepri:
                                       try:
                                           Bots.remove(target)
                                           sepri.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:delete" or text.lower() == 'admin:delete':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:delete" or text.lower() == 'staff:delete':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:delete" or text.lower() == 'bot:delete':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sepri.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                                ma = ""
                                for i in admin:
                                    ma = s1.getContact(i)
                                    s1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                                ma = ""
                                for i in staff:
                                    ma = s1.getContact(i)
                                    s1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                                ma = ""
                                for i in Bots:
                                    ma = s1.getContact(i)
                                    s1.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                sepri.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = False
                                sepri.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                sepri.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                sepri.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto respon dinonaktifkan")
                                
                        elif cmd == "respongift on" or text.lower() == 'respongift on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto respon gift diaktifkan")

                        elif cmd == "respongift off" or text.lower() == 'respongift off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentiongift"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto respon gift dinonaktifkan")                                

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto Leave Diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto Leave Dimatikan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto Add Diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto Add Dimatikan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Detect Sticker Diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Detect Sticker Dimatikan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto Join Ticket Diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Auto Join Ticket Dimatikan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sepri.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           sepri.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sepri.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                sepri.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                sepri.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  Blacklist User\n\n"+ma+"\nTotalã%sãBlacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                sepri.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +sepri.getContact(m_id).displayName + "\n"
                                sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â  Talkban User\n\n"+ma+"\nTotalã%sãTalkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    sepri.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = sepri.getContact(i)
                                        sepri.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = sepri.getContacts(wait["blacklist"])
                              mc = "ï¿½ï¿½ï¿½%iãUser Blacklist" % len(ragets)
                              sepri.sendMessage(msg.to,"âªÍÍ¡ââ¬â¤ï¸Â Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Pesan Message")
                              else:
                                  wait["message"] = spl
                                  sepri.sendMessage(msg.to, "ãPesan Msgã\nPesan Message diganti jadi :\n\nã{}ã".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Welcome Message")
                              else:
                                  wait["welcome"] = spl
                                  sepri.sendMessage(msg.to, "ãWelcome Msgã\nWelcome Message diganti jadi :\n\nã{}ã".format(str(spl)))
                                  
                        elif 'Set leave: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set leave: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Leave Message")
                              else:
                                  wait["leave"] = spl
                                  sepri.sendMessage(msg.to, "ãLeave Msgã\nLeave Message diganti jadi :\n\nã{}ã".format(str(spl)))                                    

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Respon Message")
                              else:
                                  wait["Respontag"] = spl
                                  sepri.sendMessage(msg.to, "ãRespon Msgã\nRespon Message diganti jadi :\n\nã{}ã".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["seprimessage1"] = spl
                                  sepri.sendMessage(msg.to, "ãSpam Msgã\nSpam Message diganti jadi :\n\nã{}ã".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  sepri.sendMessage(msg.to, "Gagal mengganti Sider Message")
                              else:
                                  wait["mention"] = spl
                                  sepri.sendMessage(msg.to, "ãSider Msgã\nSider Message diganti jadi :\n\nã{}ã".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãPesan Msgã\nPesan Message lu :\n\nã " + str(wait["message"]) + " ã")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãWelcome Msgã\nWelcome Message lu :\n\nã " + str(wait["welcome"]) + " ã")
                               
                        elif text.lower() == "cek leave":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãLeave Msgã\nLeave Message lu :\n\nã " + str(wait["leave"]) + " ã")                                 

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãRespon Msgã\nRespon Message lu :\n\nã " + str(wait["Respontag"]) + " ã")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãSpam Msgã\nSpam Message lu :\n\nã " + str(Setmain["seprimessage1"]) + " ã")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               sepri.sendMessage(msg.to, "ãSider Msgã\nSider Message lu :\n\nã " + str(wait["mention"]) + " ã")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = sepri.findGroupByTicket(ticket_id)
                                     sepri.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sepri.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group1 = s1.findGroupByTicket(ticket_id)
                                     s1.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     s1.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group2 = s2.findGroupByTicket(ticket_id)
                                     s2.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     s2.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group3 = s3.findGroupByTicket(ticket_id)
                                     s3.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     s3.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group4 = s4.findGroupByTicket(ticket_id)
                                     s4.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     s4.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group = s5.findGroupByTicket(ticket_id)
                                     s5.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     s5.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group1 = s6.findGroupByTicket(ticket_id)
                                     s6.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     s6.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group2 = s7.findGroupByTicket(ticket_id)
                                     s7.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     s7.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group3 = s8.findGroupByTicket(ticket_id)
                                     s8.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     s8.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))
                                     group4 = s9.findGroupByTicket(ticket_id)
                                     s9.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     s9.sendMessage(msg.to, "FunkZher JOIN GROUP : %s" % str(group.name))


    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
