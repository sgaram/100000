import ARIFISTIFIK
from ARIFISTIFIK import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import youtube_dl
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
#FUNKZHER BOT

cl = LineClient(authToken='EzD2VtmJZqSQuxSYULCc.Uv/0YYcEoAwu5rWj4Sx9Ja.KtwDgO6+EDMv4I9Bj7OFteu7v2yJ4bSXlubAJ6LQkVw=')
cl.log("Auth Token : " + str(cl.authToken))
channel = LineChannel(cl)
cl.log("Channel Access Token : " + str(channel.channelAccessToken))

ki = LineClient(authToken='EzqxUlHa7fJ4CK6nW2Af.XzmbAwonn5keEY4vw/uKlW.gnHUb4aVq0LJzAvMilB/sugwliFTEMHOrIDaibzLnXc=')
ki.log("Auth Token : " + str(ki.authToken))
channel1 = LineChannel(ki)
ki.log("Channel Access Token : " + str(channel1.channelAccessToken))

kk = LineClient(authToken='EzqfkU8n35nOkRW0tGf0.9T/PGPFdadrWbCl3Gzx/Ga.t6314tHfihMLXerKkc88/Z9D22vxibAI7fbMi5A6VZ0=')
kk.log("Auth Token : " + str(kk.authToken))
channel2 = LineChannel(kk)
kk.log("Channel Access Token : " + str(channel2.channelAccessToken))

kc = LineClient(authToken='EzwkQRV4ikVFeHlbZFYd.tLlReCirgG96uB+Q5pwO+q.T05h54NBMRTj44/an2PUZ53WvWA4EINswnGhb7GNuZA=')
kc.log("Auth Token : " + str(kc.authToken))
channel3 = LineChannel(kc)
kc.log("Channel Access Token : " + str(channel3.channelAccessToken))

ke = LineClient(authToken='Ezx1c4NT2uh6K9ET9191.lXZ4ob/KwrCUJfHRJ603qq.T2l+rfV80gtnFaUpLCHPD9Zft8QBagBPIIRmyj/g6X8=')
ke.log("Auth Token : " + str(ke.authToken))
channel4 = LineChannel(ke)
ke.log("Channel Access Token : " + str(channel4.channelAccessToken))

cl1 = LineClient(authToken='EzmS5uSCYB7hy7zWIt56.BaiKNxR2VN7zWCBrQS6P5G.RYiLnaezTznX7199HaDx3bAkMvP6P9mJwz6YsPiz0HQ=')
cl1.log("Auth Token : " + str(cl1.authToken))
channel5 = LineChannel(cl1)
cl1.log("Channel Access Token : " + str(channel5.channelAccessToken))

ki1 = LineClient(authToken='EzL2DkHaxaoV1qlG0Yza.UHbbg4pHBjT5VwCYtXmXsG.W4lCTw4GgUGfO+p3nHXuD90uFrODQQGpZfCCapAAUI4=')
ki1.log("Auth Token : " + str(ki1.authToken))
channel6 = LineChannel(ki1)
ki1.log("Channel Access Token : " + str(channel6.channelAccessToken))

kk1 = LineClient(authToken='EzBJWLyG63WKDxeRVQLa.Oyj1ZAWaMt3CKaVDd5BW2G.vV3W8vo0CXBk4nnhC7kbp23EN9sMtLijT9vFFHrG9Fk=')
kk1.log("Auth Token : " + str(kk1.authToken))
channel7 = LineChannel(kk1)
kk1.log("Channel Access Token : " + str(channel7.channelAccessToken))

kc1 = LineClient(authToken='EzBlABzMjYSjO1YAUMz4.UFxlUs4U2EOQjGvMmvWMDa.Uyy2+9JaUh3+sH11vejbKfPPQfo0PY4r/jUlCicsVMA=')
kc1.log("Auth Token : " + str(kc1.authToken))
channel8 = LineChannel(kc1)
kc1.log("Channel Access Token : " + str(channel8.channelAccessToken))

ke1 = LineClient(authToken='Ez3tIbSO0DtVCzlNO8y4.9UGdRKZXRTi7Enfms1+LPa.OCqGjfZwbUti8KaNlNi8lLlICxw4MTw/e8RjjWN54D4=')
ke1.log("Auth Token : " + str(ke1.authToken))
channel9 = LineChannel(ke1)
ke1.log("Channel Access Token : " + str(channel9.channelAccessToken))

#sw = LineClient()
sw = LineClient(authToken='EzqvVupjbe7dT7lWN1pb.zr+MvMh78HjcGGT1M17UEW.48DxWvRw7di2q2NtQwpeS2VcI5GbA80A7eQ7tUi0ht4=')
sw.log("Auth Token : " + str(sw.authToken))
channel11 = LineChannel(sw)
sw.log("Channel Access Token : " + str(channel11.channelAccessToken))

poll = LinePoll(cl)
call = cl
creator = ["u9f09cfcb17d037e2936b751bd9d40ead"]
owner = ["u9f09cfcb17d037e2936b751bd9d40ead"]
admin = ["u9f09cfcb17d037e2936b751bd9d40ead"]
staff = ["u9f09cfcb17d037e2936b751bd9d40ead"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ke.getProfile().mid
Emid = cl1.getProfile().mid
Fmid = ki1.getProfile().mid
Gmid = kk1.getProfile().mid
Hmid = kc1.getProfile().mid
Imid = ke1.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,ke]
ABC = [cl1,ki1,kk1,kc1,ke1]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Zmid]
FunkZher = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []

welcome = []

responsename1 = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
responsename3 = kk.getProfile().displayName
responsename4 = kc.getProfile().displayName
responsename5 = ke.getProfile().displayName
responsename6 = cl1.getProfile().displayName
responsename7 = ki1.getProfile().displayName
responsename8 = kk1.getProfile().displayName
responsename9 = kc1.getProfile().displayName
responsename10 = ke1.getProfile().displayName

settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "mention":"masuk ka..",
    "Respontag":"oit...",
    "welcome":"Selamat datang",
    "comment":"Like like & like by sepriche",
    "message":"Terimakasih sudah add ",
    }

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
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
        textx = "Total Mention User?{}?\n\n  [ Mention ]\n1. ".format(str(len(mid)))
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
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User?{}?\nHaii ".format(str(len(mid)))
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
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk?{}?\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
        teman = cl.getAllContactIdsx()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"?-?Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n?-?Group : "+str(len(gid))+"\n?-?Teman : "+str(len(teman))+"\n?-?Expired : In "+hari+"\n?-?Version : ARIFISTIFIK\n?-?Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n?-?Runtime : \n ? "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

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
    helpMessage = "?-?MENU HELP\n" + \
                  "?-?" + key + "Me\n" + \
                  "?-?" + key + "Mid?@?\n" + \
                  "?-?" + key + "Info?@?\n" + \
                  "?-?" + key + "Nk?@?\n" + \
                  "?-?" + key + "Kick1?@?\n" + \
                  "?-?" + key + "Mybot\n" + \
                  "?-?" + key + "Status\n" + \
                  "?-?" + key + "About\n" + \
                  "?-?" + key + "Restart\n" + \
                  "?-?" + key + "Runtime\n" + \
                  "?-?" + key + "Creator\n" + \
                  "?-?" + key + "Speed/Sp\n" + \
                  "?-?" + key + "Sprespon\n" + \
                  "?-?" + key + ".Tagall\n" + \
                  "?-?" + key + "Joinall\n" + \
                  "?-?" + key + "Byeall\n" + \
                  "?-?" + key + "Byeme\n" + \
                  "?-?" + key + "Leave?Namagrup?\n" + \
                  "?-?" + key + "Ginfo\n" + \
                  "?-?" + key + "Open\n" + \
                  "?-?" + key + "Close\n" + \
                  "?-?" + key + "Url grup\n" + \
                  "?-?" + key + "Gruplist\n" + \
                  "?-?" + key + "Infogrup?angka?\n" + \
                  "?-?" + key + "Infomem?angka?\n" + \
                  "?-?" + key + "Remove chat\n" + \
                  "?-?" + key + "Lurking?on/off?\n" + \
                  "?-?" + key + "Lurkers\n" + \
                  "?-?" + key + "Sider?on/off?\n" + \
                  "?-?" + key + "Updatefoto\n" + \
                  "?-?" + key + "Updategrup\n" + \
                  "?-?" + key + "Updatebot\n" + \
                  "?-?" + key + "Broadcast:?Text?\n" + \
                  "?-?" + key + "Setkey?New Key?\n" + \
                  "?-?" + key + "Mykey\n" + \
                  "?-?" + key + "Resetkey\n" + \
                  "?-?" + key + "ID line:?Id Line nya?\n" + \
                  "?-?" + key + "Sholat:?Nama Kota?\n" + \
                  "?-?" + key + "Cuaca:?Nama Kota?\n" + \
                  "?-?" + key + "Lokasi:?Nama Kota?\n" + \
                  "?-?" + key + "Music:?Judul Lagu?\n" + \
                  "?-?" + key + "Lirik:?Judul Lagu?\n" + \
                  "?-?" + key + "Ytmp3:?Judul Lagu?\n" + \
                  "?-?" + key + "Ytmp4:?Judul Video?\n" + \
                  "?-?" + key + "Profileig:?Nama IG?\n" + \
                  "?-?" + key + "Cekdate:?tgl-bln-thn?\n" + \
                  "?-?" + key + "Jumlah:?angka?\n" + \
                  "?-?" + key + "Spamtag?@?\n" + \
                  "?-?" + key + "Spamcall:?jumlahnya?\n" + \
                  "?-?" + key + "Spamcall\n" + \
                  "?-?" + key + "Warmode?on/off?\n" + \
                  "?-?" + key + "Protectinvite?on/off?\n" + \
                  "?-?" + key + "Protecturl?on/off?\n" + \
                  "?-?" + key + "Protectjoin?on/off?\n" + \
                  "?-?" + key + "Protectkick?on/off?\n" + \
                  "?-?" + key + "Protectcancel?on/off?\n" + \
                  "?-?" + key + "Antijs?on/off?\n" + \
                  "?-?" + key + "Antijs stay\n" + \
                  "?-?" + key + "Ghost?on/off?\n" + \
                  "?-?" + key + "Sticker?on/off?\n" + \
                  "?-?" + key + "Respon?on/off?\n" + \
                  "?-?" + key + "Contact?on/off?\n" + \
                  "?-?" + key + "Autojoin?on/off?\n" + \
                  "?-?" + key + "Autoadd?on/off?\n" + \
                  "?-?" + key + "Welcome?on/off?\n" + \
                  "?-?" + key + "Autoleave?on/off?\n" + \
                  "?-?" + key + "Admin:on\n" + \
                  "?-?" + key + "Admin:repeat\n" + \
                  "?-?" + key + "Staff:on\n" + \
                  "?-?" + key + "Staff:repeat\n" + \
                  "?-?" + key + "Bot:on\n" + \
                  "?-?" + key + "Bot:repeat\n" + \
                  "?-?" + key + "Adminadd?@?\n" + \
                  "?-?" + key + "Admindell?@?\n" + \
                  "?-?" + key + "Staffadd?@?\n" + \
                  "?-?" + key + "Staffdell?@?\n" + \
                  "?-?" + key + "Botadd?@?\n" + \
                  "?-?" + key + "Botdell?@?\n" + \
                  "?-?" + key + "Refresh\n" + \
                  "?-?" + key + "Listbot\n" + \
                  "?-?" + key + "Listadmin\n" + \
                  "?-?" + key + "Listprotect\n" + \
                  "?-?TEAM FANKZHER"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "?-?HELP BOT\n" + \
                  "?-?" + key + "Blc\n" + \
                  "?-?" + key + "Ban:on\n" + \
                  "?-?" + key + "Unban:on\n" + \
                  "?-?" + key + "Ban?@?\n" + \
                  "?-?" + key + "Unban?@?\n" + \
                  "?-?" + key + "Talkban?@?\n" + \
                  "?-?" + key + "Untalkban?@?\n" + \
                  "?-?" + key + "Talkban:on\n" + \
                  "?-?" + key + "Untalkban:on\n" + \
                  "?-?" + key + "Banlist\n" + \
                  "?-?" + key + "Talkbanlist\n" + \
                  "?-?" + key + "Clearban\n" + \
                  "?-?" + key + "Refresh\n" + \
                  "?-?" + key + "Cek sider\n" + \
                  "?-?" + key + "Cek spam\n" + \
                  "?-?" + key + "Cek pesan \n" + \
                  "?-?" + key + "Cek respon \n" + \
                  "?-?" + key + "Cek welcome\n" + \
                  "?-?" + key + "Set sider:?Text?\n" + \
                  "?-?" + key + "Set spam:?Text?\n" + \
                  "?-?" + key + "Set pesan:?Text?\n" + \
                  "?-?" + key + "Set respon:?Text?\n" + \
                  "?-?" + key + "Set welcome:?Text?\n" + \
                  "?-?" + key + "Myname:?Nama?\n" + \
                  "?-?" + key + "Bot1name:?Nama?\n" + \
                  "?-?" + key + "Bot2name:?Nama?\n" + \
                  "?-?" + key + "Bot3name:?Nama?\n" + \
                  "?-?" + key + "Bot1up?Kirim fotonya?\n" + \
                  "?-?" + key + "Bot2up?Kirim fotonya?\n" + \
                  "?-?" + key + "Bot3up?Kirim fotonya?\n" + \
                  "?-?" + key + "Gift:?Mid korban??Jumlah?\n" + \
                  "?-?" + key + "Spam:?Mid korban??Jumlah?\n" + \
                  "?-?TEAM FANKZHER"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ke.reissueGroupTicket(op.param1)
                                            X = ke.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ke.updateGroup(X)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if cl1.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                cl1.reissueGroupTicket(op.param1)
                                                X = cl1.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                cl1.updateGroup(X)
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl1.acceptGroupInvitation(op.param1)
                        ginfo = cl1.getGroup(op.param1)
                        cl1.leaveGroup(op.param1)
                    else:
                        cl1.acceptGroupInvitation(op.param1)
                        ginfo = cl1.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki1.acceptGroupInvitation(op.param1)
                        ginfo = ki1.getGroup(op.param1)
                        ki1.leaveGroup(op.param1)
                    else:
                        ki1.acceptGroupInvitation(op.param1)
                        ginfo = ki1.getGroup(op.param1)
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk1.acceptGroupInvitation(op.param1)
                        ginfo = kk1.getGroup(op.param1)
                        kk1.leaveGroup(op.param1)
                    else:
                        kk1.acceptGroupInvitation(op.param1)
                        ginfo = kk1.getGroup(op.param1)
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc1.acceptGroupInvitation(op.param1)
                        ginfo = kc1.getGroup(op.param1)
                        kc1.leaveGroup(op.param1)
                    else:
                        kc1.acceptGroupInvitation(op.param1)
                        ginfo = kc1.getGroup(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke1.acceptGroupInvitation(op.param1)
                        ginfo = ke1.getGroup(op.param1)
                        ke1.leaveGroup(op.param1)
                    else:
                        ke1.acceptGroupInvitation(op.param1)
                        ginfo = ke1.getGroup(op.param1)

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	cl1.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk1.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kc1.kickoutFromGroup(op.param1,[op.param2])
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
                        cl.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 19:
            try:
                if op.param1 in ghost:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
            except:
                pass             
                
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
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        sw.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"=AntiJS Invited=")
                        
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"=Admin Invited=")
                else:
                    pass
            except:
                pass
#-------------------------------------------------------------------------------                
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
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
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki.updateGroup(G)
                                    Ticket = ki.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl1.kickoutFromGroup(op.param1,[op.param2])
                                        ki1.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki1.kickoutFromGroup(op.param1,[op.param2])
                                            kk1.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
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
                        kk1.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc1.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke1.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    kc1.updateGroup(G)
                                    Ticket = kc1.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc1.updateGroup(G)
                                    Ticket = kc1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        ki1.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kk1.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
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
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl1.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki1.kickoutFromGroup(op.param1,[op.param2])
                                cl1.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = ki1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk1.kickoutFromGroup(op.param1,[op.param2])
                                    ki1.updateGroup(G)
                                    Ticket = ki1.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = ki1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    ki1.updateGroup(G)
                                    Ticket = ki1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kc1.kickoutFromGroup(op.param1,[op.param2])
                                        kk1.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke1.kickoutFromGroup(op.param1,[op.param2])
                                            kc1.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
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
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = cl1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = cl1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    cl1.updateGroup(G)
                                    Ticket = cl1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ki1.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            cl1.kickoutFromGroup(op.param1,[op.param2])
                                            kk1.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
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
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                        kk1.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk1.kickoutFromGroup(op.param1,[op.param2])
                            kc1.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc1.kickoutFromGroup(op.param1,[op.param2])
                                ke1.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ke1.kickoutFromGroup(op.param1,[op.param2])
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return

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
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        cl1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            cl1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                cl1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    cl1.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        cl1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki1.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            cl1.acceptGroupInvitation(op.param1)
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
                        kc1.kickoutFromGroup(op.param1,[op.param2])
                        ke1.inviteIntoGroup(op.param1,[op.param3])
                        ki1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke1.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            ki1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                ki1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kk.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kk.updateGroup(G)
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        ki1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            ki1.acceptGroupInvitation(op.param1)
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
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        kk1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl1.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kk1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki1.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kk1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kk1.kickoutFromGroup(op.param1,[op.param2])
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc.updateGroup(G)
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        kc1.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        kk1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ke1.kickoutFromGroup(op.param1,[op.param2])
                                            cl1.inviteIntoGroup(op.param1,[op.param3])
                                            kk1.acceptGroupInvitation(op.param1)
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
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        ki1.inviteIntoGroup(op.param1,[op.param3])
                        kc1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            kk1.inviteIntoGroup(op.param1,[op.param3])
                            kc1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                ke1.inviteIntoGroup(op.param1,[op.param3])
                                kc1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = cl.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    cl.updateGroup(G)
                                    Ticket = cl.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        kc1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            cl1.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            kc1.acceptGroupInvitation(op.param1)
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
                        ki1.kickoutFromGroup(op.param1,[op.param2])
                        cl1.inviteIntoGroup(op.param1,[op.param3])
                        ke1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk1.kickoutFromGroup(op.param1,[op.param2])
                            ki1.inviteIntoGroup(op.param1,[op.param3])
                            ke1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc1.kickoutFromGroup(op.param1,[op.param2])
                                kk1.inviteIntoGroup(op.param1,[op.param3])
                                ke1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    G = kc1.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    ki1.kickoutFromGroup(op.param1,[op.param2])
                                    kc1.updateGroup(G)
                                    Ticket = kc1.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    cl1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ki1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kk1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    G = kc1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kc1.updateGroup(G)
                                    Ticket = kc1.reissueGroupTicket(op.param1)
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl1.inviteIntoGroup(op.param1,[op.param3])
                                        ke1.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            ki1.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                            ke1.acceptGroupInvitation(op.param1)
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
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
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
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["ARreadPoint"]:
                   if op.param2 in Setmain["ARreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["ARreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        cl.sendImageWithURL(op.param1, image)                        
                        
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 26:
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
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n??STKID : " + msg.contentMetadata["STKID"] + "\n??STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n??STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"??Nama : " + msg.contentMetadata["displayName"] + "\n??MID : " + msg.contentMetadata["mid"] + "\n??Status Msg : " + contact.statusMessage + "\n??Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"??Nama : " + msg.contentMetadata["displayName"] + "\n??MID : " + msg.contentMetadata["mid"] + "\n??Status Msg : " + contact.statusMessage + "\n??Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot FunkZher")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "bot on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Bot aktif")
                                ki.sendText(msg.to, "Bot aktif")
                                kk.sendText(msg.to, "Bot aktif")
                                kc.sendText(msg.to, "Bot aktif")
                                ke.sendText(msg.to, "Bot aktif")
                                cl1.sendText(msg.to, "Bot aktif")
                                ki1.sendText(msg.to, "Bot aktif")
                                kk1.sendText(msg.to, "Bot aktif")
                                kc1.sendText(msg.to, "Bot aktif")
                                ke1.sendText(msg.to, "Bot aktif")
                                
                        elif cmd == "bot off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Bot not aktif")
                                ki.sendText(msg.to, "Bot not aktif")
                                kk.sendText(msg.to, "Bot not aktif")
                                kc.sendText(msg.to, "Bot not aktif")
                                ke.sendText(msg.to, "Bot not aktif")
                                cl1.sendText(msg.to, "Bot not aktif")
                                ki1.sendText(msg.to, "Bot not aktif")
                                kk1.sendText(msg.to, "Bot not aktif")
                                kc1.sendText(msg.to, "Bot not aktif")
                                ke1.sendText(msg.to, "Bot not aktif")
                                            
                        elif cmd == "help bot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "  ?????????????????\n         ? S T A T U S ?\n?????????????????\n"
                                if wait["sticker"] == True: md+="?-?STC?ON?\n"
                                else: md+="?-?STC?OFF?\n"
                                if wait["contact"] == True: md+="?-?Contact?ON?\n"
                                else: md+="?-?Contact?OFF?\n"
                                if wait["talkban"] == True: md+="?-?Talkban?ON?\n"
                                else: md+="?-?Talkban?OFF?\n"
                                if wait["detectMention"] == True: md+="?-?Respon?ON?\n"
                                else: md+="?-?Respon?OFF?\n"
                                if wait["autoJoin"] == True: md+="?-?Autojoin?ON?\n"
                                else: md+="?-?Autojoin?OFF?\n"
                                if wait["autoAdd"] == True: md+="?-?Autoadd?ON?\n"
                                else: md+="?-?Autoadd?OFF?\n"
                                if msg.to in welcome: md+="?-?Welcome?ON?\n"
                                else: md+="?-?Welcome?OFF?\n"
                                if wait["autoLeave"] == True: md+="?-?Autoleave?ON?\n"
                                else: md+="?-?Autoleave?OFF?\n"
                                if msg.to in protectqr: md+="?-?Protecturl?ON?\n"
                                else: md+="?-?Protecturl?OFF?\n"
                                if msg.to in protectjoin: md+="?-?Protectjoin?ON?\n"
                                else: md+="?-?Protectjoin?OFF?\n"
                                if msg.to in protectkick: md+="?-?Protectkick?ON?\n"
                                else: md+="?-?Protectkick?OFF?\n"
                                if msg.to in protectinvite: md+="?-?Protectinvite?ON?\n"
                                else: md+="?-?Protectinvite?OFF?\n"
                                if msg.to in protectcancel: md+="?-?Protectcancel?ON?\n"
                                else: md+="?-?Protectcancel?OFF?\n"
                                if msg.to in protectantijs: md+="?-?Antijs?ON?\n"
                                else: md+="?-?Antijs?OFF?\n"                                   
                                cl.sendMessage(msg.to, md+"?????????????????\nFunkZher Bot\nPROTECTION\n  ?????????????????")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"Creator Bot FunkZher") 

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "? Type Selfbot ?\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid} 
                               cl.sendMessage(msg.to, "??????")
                               cl.sendMessage1(msg)
                      #         cl.sendMessage(msg.to, None, contentMetadata={"STKID":"51626530","STKPKGID":"11538","STKVER":"1"}, contentType=7)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                               ki.sendMessage(msg.to, msg._from)
                               kk.sendMessage(msg.to, msg._from)
                               kc.sendMessage(msg.to, msg._from)
                               ke1.sendMessage(msg.to, msg._from)
                               cl1.sendMessage(msg.to, msg._from)
                               ki1.sendMessage(msg.to, msg._from)
                               kk1.sendMessage(msg.to, msg._from)
                               kc1.sendMessage(msg.to, msg._from)
                               ke1.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "?-?Nama : "+str(mi.displayName)+"\n?-?Mid : " +key1+"\n?-?Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Emid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Fmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Gmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Hmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Imid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   cl1.removeAllMessages(op.param2)
                                   ki1.removeAllMessages(op.param2)
                                   kk1.removeAllMessages(op.param2)
                                   kc1.removeAllMessages(op.param2)
                                   ke1.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"done")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Mykey?\nSetkey bot mu? " + str(Setmain["keyCommand"]) + " ?")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "?Setkey?\nSetkey diganti jadi?{}?".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "?Setkey?\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "please wait...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "bot active...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "?-?FunkZher Bot Info\n\n?-?Nama Group : {}".format(G.name)+ "\n?-?ID Group : {}".format(G.id)+ "\n?-?Pembuat : {}".format(G.creator.displayName)+ "\n?-?Waktu Dibuat : {}".format(str(timeCreated))+ "\n?-?Jumlah Member : {}".format(str(len(G.members)))+ "\n?-?Jumlah Pending : {}".format(gPending)+ "\n?-?Group Qr : {}".format(gQr)+ "\n?-?Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
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
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "?-?FunkZher Bot Grup Info\n"
                                ret_ += "\n?-?Nama Group : {}".format(G.name)
                                ret_ += "\n?-?ID Group : {}".format(G.id)
                                ret_ += "\n?-?Pembuat : {}".format(gCreator)
                                ret_ += "\n?-?Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n?-?Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n?-?Jumlah Pending : {}".format(gPending)
                                ret_ += "\n?-?Group Qr : {}".format(gQr)
                                ret_ += "\n?-?Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "?-?"+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"?-?Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n?Total %i Members?" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    cl1.leaveGroup(i)
                                    ki1.leaveGroup(i)
                                    kk1.leaveGroup(i)
                                    kc1.leaveGroup(i)
                                    ke1.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "url grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"send foto")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"send foto")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendText(msg.to,"send foto")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendText(msg.to,"send foto")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendText(msg.to,"send foto")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendText(msg.to,"send foto")

                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                ke.sendText(msg.to,"send foto")

                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                cl1.sendText(msg.to,"send foto")

                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                ki1.sendText(msg.to,"send foto")

                        elif cmd == "bot7up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                kk1.sendText(msg.to,"send foto")

                        elif cmd == "bot8up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Hmid] = True
                                kc1.sendText(msg.to,"send foto")

                        elif cmd == "bot9up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Imid] = True
                                ke1.sendText(msg.to,"send foto")
                                
                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendText(msg.to,"send foto")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl1.getProfile()
                                profile.displayName = string
                                cl1.updateProfile(profile)
                                cl1.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki1.getProfile()
                                profile.displayName = string
                                ki1.updateProfile(profile)
                                ki1.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk1.getProfile()
                                profile.displayName = string
                                kk1.updateProfile(profile)
                                kk1.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc1.getProfile()
                                profile.displayName = string
                                kc1.updateProfile(profile)
                                kc1.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke1.getProfile()
                                profile.displayName = string
                                ke1.updateProfile(profile)
                                ke1.sendMessage(msg.to,"bot name " + string + "")

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"bot name " + string + "")

#===========BOT UPDATE============#
                        elif cmd == ".tagall" or text.lower() == '.togel':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
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
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"?-?FunkZher Bot\n\n"+ma+"\nTotal?%s? Bots" %(str(len(Bots))))

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
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"?-?FunkZher Bot\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal?%s? Delta" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"?-?FunkZher Bot\n\n?-?PROTECT URL :\n"+ma+"\n?-?PROTECT KICK :\n"+mb+"\n?-?PROTECT JOIN :\n"+md+"\n?-?PROTECT CANCEL:\n"+mc+"\n?-?PROTECT INVITE:\n"+mc+"\nTotal?%s?Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel)+len(protectcancel))))

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to,responsename1)
                                ki.sendMessage(msg.to,responsename2)
                                kk.sendMessage(msg.to,responsename3)
                                kc.sendMessage(msg.to,responsename4)
                                ke.sendMessage(msg.to,responsename5)
                                cl1.sendMessage(msg.to,responsename6)
                                ki1.sendMessage(msg.to,responsename7)
                                kk1.sendMessage(msg.to,responsename8)
                                kc1.sendMessage(msg.to,responsename9)
                                ke1.sendMessage(msg.to,responsename10)

                        elif cmd == "invitebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    cl1.acceptGroupInvitation(msg.to)
                                    ki1.acceptGroupInvitation(msg.to)
                                    kk1.acceptGroupInvitation(msg.to)
                                    kc1.acceptGroupInvitation(msg.to)
                                    ke1.acceptGroupInvitation(msg.to)
                                except:
                                    pass
                                
                        elif cmd == "js stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Zmid])
                                    cl.sendMessage(msg.to,"js stay"+str(ginfo.name)+"")
                                except:
                                    pass
    
                        elif cmd == "joinall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                cl1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke1.updateGroup(G)

                        elif cmd == "byeall":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                cl1.leaveGroup(msg.to)
                                ki1.leaveGroup(msg.to)
                                kk1.leaveGroup(msg.to)
                                kc1.leaveGroup(msg.to)
                                ke1.leaveGroup(msg.to)
                                
                        elif cmd == "byeme":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        cl1.leaveGroup(i)
                                        ki1.leaveGroup(i)
                                        kk1.leaveGroup(i)
                                        kc1.leaveGroup(i)
                                        ke1.leaveGroup(i)
                                        cl.sendMessage(to,"Berhasil keluar dari grup " +h)

                        elif cmd == "assist1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "assist2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "assist3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "kicker join":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kicker bye":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "FunkZher Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['ARreadPoint'][msg.to] = msg_id
                                 Setmain['ARreadMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['ARreadPoint'][msg.to]
                                 del Setmain['ARreadMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['ARreadPoint']:
                                if Setmain['ARreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['ARreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
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
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['ARreadPoint'][msg.to]
                                        del Setmain['ARreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['ARreadPoint'][msg.to] = msg.id
                                    Setmain['ARreadMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == ".sider on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
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
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "?Jadwal Sholat?"
                                         ret_ += "\n?-?Lokasi : " + data[0]
                                         ret_ += "\n?-?" + data[1]
                                         ret_ += "\n?-?" + data[2]
                                         ret_ += "\n?-?" + data[3]
                                         ret_ += "\n?-?" + data[4]
                                         ret_ += "\n?-?" + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "?Status Cuaca?"
                                    ret_ += "\n?-?Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n?-?Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n?-?Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n?-?Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n?-?Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "?Info Lokasi?"
                                    ret_ += "\n?-?Location : " + data[0]
                                    ret_ += "\n?-?Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "???[ Lyric ]"
                                          ret_ += "\n? Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n? Durasi : {}".format(str(song[1]))
                                          ret_ += "\n? Link : {}".format(str(song[3]))
                                          ret_ += "\n???[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendText(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "???[ Music ]"
                                          ret_ += "\n? Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n? Durasi : {}".format(str(song[1]))
                                          ret_ += "\n? Link : {}".format(str(song[3]))
                                          ret_ += "\n???[ Waiting Audio ]"
                                      cl.sendText(msg.to, str(ret_))
                                      cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendText(to, "Musik tidak ditemukan")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"?Google Image?\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

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
                                    author = '\n\n?-?Author : ' + str(vid.author)
                                    durasi = '\n?-?Duration : ' + str(vid.duration)
                                    suka = '\n?-?Likes : ' + str(vid.likes)
                                    rating = '\n?-?Rating : ' + str(vid.rating)
                                    deskripsi = '\n?-?Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

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
                                    author = '\n\n?-?Author : ' + str(vid.author)
                                    durasi = '\n?-?Duration : ' + str(vid.duration)
                                    suka = '\n?-?Likes : ' + str(vid.likes)
                                    rating = '\n?-?Rating : ' + str(vid.rating)
                                    deskripsi = '\n?-?Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "?-?Link : " + "https://www.instagram.com/" + instagram
                                text = "?-?Name : "+namaIG+"\n?-?Username : "+usernameIG+"\n?-?Biography : "+bioIG+"\n?-?Follower : "+followerIG+"\n?-?Following : "+followIG+"\n?-?Post : "+mediaIG+"\n?-?Verified : "+verifIG+"\n?-?Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"?-?I N F O R M A S I ?\n\n"+"?-?Date Of Birth : "+lahir+"\n?-?Age : "+usia+"\n?-?Ultah : "+ultah+"\n?-?Zodiak : "+zodiak)

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["ARlimit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

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
                                    jmlh = int(Setmain["ARlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ke.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      cl1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ke1.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["ARmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["ARmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome on ?? "
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome on ??  "
                                  cl.sendMessage(msg.to, msgs)
                                  ki.sendMessage(msg.to, msgs)
                                  kk.sendMessage(msg.to, msgs)
                                  kc.sendMessage(msg.to, msgs)
                                  ke.sendMessage(msg.to, msgs)
                                  cl1.sendMessage(msg.to, msgs)
                                  ki1.sendMessage(msg.to, msgs)
                                  kk1.sendMessage(msg.to, msgs)
                                  kc1.sendMessage(msg.to, msgs)
                                  ke1.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome off ??  "
                                    else:
                                         msgs = "Welcome off ?? "
                                    cl.sendMessage(msg.to, msgs)
                                    ki.sendMessage(msg.to, msgs)
                                    kk.sendMessage(msg.to, msgs)
                                    kc.sendMessage(msg.to, msgs)
                                    ke.sendMessage(msg.to, msgs)
                                    cl1.sendMessage(msg.to, msgs)
                                    ki1.sendMessage(msg.to, msgs)
                                    kk1.sendMessage(msg.to, msgs)
                                    kc1.sendMessage(msg.to, msgs)
                                    ke1.sendMessage(msg.to, msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url enable ??"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url enable ??"
                                  cl.sendMessage(msg.to, msgs)
                                  ki.sendMessage(msg.to, msgs)
                                  kk.sendMessage(msg.to, msgs)
                                  kc.sendMessage(msg.to, msgs)
                                  ke.sendMessage(msg.to, msgs)
                                  cl1.sendMessage(msg.to, msgs)
                                  ki1.sendMessage(msg.to, msgs)
                                  kk1.sendMessage(msg.to, msgs)
                                  kc1.sendMessage(msg.to, msgs)
                                  ke1.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url disable ??"
                                    else:
                                         msgs = "Protect url disable ??"
                                    cl.sendMessage(msg.to, msgs)
                                    ki.sendMessage(msg.to, msgs)
                                    kk.sendMessage(msg.to, msgs)
                                    kc.sendMessage(msg.to, msgs)
                                    ke.sendMessage(msg.to, msgs)
                                    cl1.sendMessage(msg.to, msgs)
                                    ki1.sendMessage(msg.to, msgs)
                                    kk1.sendMessage(msg.to, msgs)
                                    kc1.sendMessage(msg.to, msgs)
                                    ke1.sendMessage(msg.to, msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick  enable ??"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick enable ?? "
                                  cl.sendMessage(msg.to, msgs)
                                  ki.sendMessage(msg.to, msgs)
                                  kk.sendMessage(msg.to, msgs)
                                  kc.sendMessage(msg.to, msgs)
                                  ke.sendMessage(msg.to, msgs)
                                  cl1.sendMessage(msg.to, msgs)
                                  ki1.sendMessage(msg.to, msgs)
                                  kk1.sendMessage(msg.to, msgs)
                                  kc1.sendMessage(msg.to, msgs)
                                  ke1.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick disable  ?? "
                                    else:
                                         msgs = "Protect kick disable  ?? "
                                    cl.sendMessage(msg.to,  msgs)
                                    ki.sendMessage(msg.to, msgs)
                                    kk.sendMessage(msg.to, msgs)
                                    kc.sendMessage(msg.to, msgs)
                                    ke.sendMessage(msg.to, msgs)
                                    cl1.sendMessage(msg.to, msgs)
                                    ki1.sendMessage(msg.to, msgs)
                                    kk1.sendMessage(msg.to, msgs)
                                    kc1.sendMessage(msg.to, msgs)
                                    ke1.sendMessage(msg.to, msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join enable ?? "
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join enable ?? "
                                  cl.sendMessage(msg.to, msgs)
                                  ki.sendMessage(msg.to, msgs)
                                  kk.sendMessage(msg.to, msgs)
                                  kc.sendMessage(msg.to, msgs)
                                  ke.sendMessage(msg.to, msgs)
                                  cl1.sendMessage(msg.to, msgs)
                                  ki1.sendMessage(msg.to, msgs)
                                  kk1.sendMessage(msg.to, msgs)
                                  kc1.sendMessage(msg.to, msgs)
                                  ke1.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join disable  ?? "
                                    else:
                                         msgs = "Protect join disable  ?? "
                                    cl.sendMessage(msg.to, msgs)
                                    ki.sendMessage(msg.to, msgs)
                                    kk.sendMessage(msg.to, msgs)
                                    kc.sendMessage(msg.to, msgs)
                                    ke.sendMessage(msg.to, msgs)
                                    cl1.sendMessage(msg.to, msgs)
                                    ki1.sendMessage(msg.to, msgs)
                                    kk1.sendMessage(msg.to, msgs)
                                    kc1.sendMessage(msg.to, msgs)
                                    ke1.sendMessage(msg.to, msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite enable ?? "
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite enable ??  "
                                  cl.sendMessage(msg.to, msgs)
                                  ki.sendMessage(msg.to, msgs)
                                  kk.sendMessage(msg.to, msgs)
                                  kc.sendMessage(msg.to, msgs)
                                  ke.sendMessage(msg.to, msgs)
                                  cl1.sendMessage(msg.to, msgs)
                                  ki1.sendMessage(msg.to, msgs)
                                  kk1.sendMessage(msg.to, msgs)
                                  kc1.sendMessage(msg.to, msgs)
                                  ke1.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite disable ??  "
                                    else:
                                         msgs = "Protect invite disable ?? "
                                    cl.sendMessage(msg.to, msgs)
                                    ki.sendMessage(msg.to, msgs)
                                    kk.sendMessage(msg.to, msgs)
                                    kc.sendMessage(msg.to, msgs)
                                    ke.sendMessage(msg.to, msgs)
                                    cl1.sendMessage(msg.to, msgs)
                                    ki1.sendMessage(msg.to, msgs)
                                    kk1.sendMessage(msg.to, msgs)
                                    kc1.sendMessage(msg.to, msgs)
                                    ke1.sendMessage(msg.to, msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel enable  ?? "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel enable  ?? "
                                  cl.sendMessage(msg.to, msgs)
                                  ki.sendMessage(msg.to, msgs)
                                  kk.sendMessage(msg.to, msgs)
                                  kc.sendMessage(msg.to, msgs)
                                  ke.sendMessage(msg.to, msgs)
                                  cl1.sendMessage(msg.to, msgs)
                                  ki1.sendMessage(msg.to, msgs)
                                  kk1.sendMessage(msg.to, msgs)
                                  kc1.sendMessage(msg.to, msgs)
                                  ke1.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel  disable  ?? "
                                    else:
                                         msgs = "Protect cancel disable  ?? "
                                    cl.sendMessage(msg.to, msgs)
                                    ki.sendMessage(msg.to, msgs)
                                    kk.sendMessage(msg.to, msgs)
                                    kc.sendMessage(msg.to, msgs)
                                    ke.sendMessage(msg.to, msgs)
                                    cl1.sendMessage(msg.to, msgs)
                                    ki1.sendMessage(msg.to, msgs)
                                    kk1.sendMessage(msg.to, msgs)
                                    kc1.sendMessage(msg.to, msgs)
                                    ke1.sendMessage(msg.to, msgs)

                        elif 'Antijs ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Antijs ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "AntiJS  active ?? "
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS active ?? "
                                  cl.sendMessage(msg.to, msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS not active ??  "
                                    else:
                                         msgs = "Anti JS not active ?? "
                                    cl.sendMessage(msg.to, msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)                                    

                        elif 'Allpro' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
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
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass

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
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"admin add done ??")
                                           ki.sendMessage(msg.to,"admin add done ??")
                                           kk.sendMessage(msg.to,"admin add done ??")
                                           kc.sendMessage(msg.to,"admin add done ??")
                                           ke.sendMessage(msg.to,"admin add done ??")
                                           cl1.sendMessage(msg.to,"admin add done ??")
                                           ki1.sendMessage(msg.to,"admin add done ??")
                                           kk1.sendMessage(msg.to,"admin add done ??")
                                           kc1.sendMessage(msg.to,"admin add done ??")
                                           ke1.sendMessage(msg.to,"admin add done ??")
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
                                           cl.sendMessage(msg.to,"staff add done ??")
                                           ki.sendMessage(msg.to,"staff add done ??")
                                           kk.sendMessage(msg.to,"staff add done ??")
                                           kc.sendMessage(msg.to,"staff add done ??")
                                           ke.sendMessage(msg.to,"staff add done ??")
                                           cl1.sendMessage(msg.to,"staff add done ??")
                                           ki1.sendMessage(msg.to,"staff add done ??")
                                           kk1.sendMessage(msg.to,"staff add done ??")
                                           kc1.sendMessage(msg.to,"staff add done ??")
                                           ke1.sendMessage(msg.to,"staff add done ??")
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
                                           cl.sendMessage(msg.to,"bot add done ??")
                                           ki.sendMessage(msg.to,"bot add done ??")
                                           kk.sendMessage(msg.to,"bot add done ??")
                                           kc.sendMessage(msg.to,"bot add done ??")
                                           ke.sendMessage(msg.to,"bot add done ??")
                                           cl1.sendMessage(msg.to,"bot add done ??")
                                           ki1.sendMessage(msg.to,"bot add done ??")
                                           kk1.sendMessage(msg.to,"bot add done ??")
                                           kc1.sendMessage(msg.to,"bot add done ??")
                                           ke1.sendMessage(msg.to,"bot add done ??")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in FunkZher:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"admin delete succes ?? ")
                                           ki.sendMessage(msg.to,"admin delete succes ?? ")
                                           kk.sendMessage(msg.to,"admin delete succes ?? ")
                                           kc.sendMessage(msg.to,"admin delete succes ?? ")
                                           ke.sendMessage(msg.to,"admin delete succes ?? ")
                                           cl1.sendMessage(msg.to,"admin delete succes ?? ")
                                           ki1.sendMessage(msg.to,"admin delete succes ?? ")
                                           kk1.sendMessage(msg.to,"admin delete succes ?? ")
                                           kc1.sendMessage(msg.to,"admin delete succes ?? ")
                                           ke1.sendMessage(msg.to,"admin delete succes ?? ")
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
                                   if target not in FunkZher:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"staff delete succes ?? ")
                                           ki.sendMessage(msg.to,"staff delete succes ?? ")
                                           kk.sendMessage(msg.to,"staff delete succes ?? ")
                                           kc.sendMessage(msg.to,"staff delete succes ?? ")
                                           ke.sendMessage(msg.to,"staff delete succes ?? ")
                                           cl1.sendMessage(msg.to,"staff delete succes ?? ")
                                           ki1.sendMessage(msg.to,"staff delete succes ?? ")
                                           kk1.sendMessage(msg.to,"staff delete succes ?? ")
                                           kc1.sendMessage(msg.to,"staff delete succes ?? ")
                                           ke1.sendMessage(msg.to,"staff delete succes ?? ")
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
                                   if target not in FunkZher:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"delete bot succes ?? ")
                                           ki.sendMessage(msg.to,"delete bot succes ?? ")
                                           kk.sendMessage(msg.to,"delete bot succes ?? ")
                                           kc.sendMessage(msg.to,"delete bot succes ?? ")
                                           ke.sendMessage(msg.to,"delete bot succes ?? ")
                                           cl1.sendMessage(msg.to,"delete bot succes ?? ")
                                           ki1.sendMessage(msg.to,"delete bot succes ?? ")
                                           kk1.sendMessage(msg.to,"delete bot succes ?? ")
                                           kc1.sendMessage(msg.to,"delete bot succes ?? ")
                                           ke1.sendMessage(msg.to,"delete bot succes ?? ")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"send contact")
                                ki.sendText(msg.to,"send contact")
                                kk.sendText(msg.to,"send contact")
                                kc.sendText(msg.to,"send contact")
                                ke.sendText(msg.to,"send contact")
                                cl1.sendText(msg.to,"send contact")
                                ki1.sendText(msg.to,"send contact")
                                kk1.sendText(msg.to,"send contact")
                                kc1.sendText(msg.to,"send contact")
                                ke1.sendText(msg.to,"send contact")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"send contact")
                                ki.sendText(msg.to,"send contact")
                                kk.sendText(msg.to,"send contact")
                                kc.sendText(msg.to,"send contact")
                                ke.sendText(msg.to,"send contact")
                                cl1.sendText(msg.to,"send contact")
                                ki1.sendText(msg.to,"send contact")
                                kk1.sendText(msg.to,"send contact")
                                kc1.sendText(msg.to,"send contact")
                                ke1.sendText(msg.to,"send contact")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"send contact")
                                ki.sendText(msg.to,"send contact")
                                kk.sendText(msg.to,"send contact")
                                kc.sendText(msg.to,"send contact")
                                ke.sendText(msg.to,"send contact")
                                cl1.sendText(msg.to,"send contact")
                                ki1.sendText(msg.to,"send contact")
                                kk1.sendText(msg.to,"send contact")
                                kc1.sendText(msg.to,"send contact")
                                ke1.sendText(msg.to,"send contact")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"send contact")
                                ki.sendText(msg.to,"send contact")
                                kk.sendText(msg.to,"send contact")
                                kc.sendText(msg.to,"send contact")
                                ke.sendText(msg.to,"send contact")
                                cl1.sendText(msg.to,"send contact")
                                ki1.sendText(msg.to,"send contact")
                                kk1.sendText(msg.to,"send contact")
                                kc1.sendText(msg.to,"send contact")
                                ke1.sendText(msg.to,"send contact")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"send contact")
                                ki.sendText(msg.to,"send contact")
                                kk.sendText(msg.to,"send contact")
                                kc.sendText(msg.to,"send contact")
                                ke.sendText(msg.to,"send contact")
                                cl1.sendText(msg.to,"send contact")
                                ki1.sendText(msg.to,"send contact")
                                kk1.sendText(msg.to,"send contact")
                                kc1.sendText(msg.to,"send contact")
                                ke1.sendText(msg.to,"send contact")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"send contact")
                                ki.sendText(msg.to,"send contact")
                                kk.sendText(msg.to,"send contact")
                                kc.sendText(msg.to,"send contact")
                                ke.sendText(msg.to,"send contact")
                                cl1.sendText(msg.to,"send contact")
                                ki1.sendText(msg.to,"send contact")
                                kk1.sendText(msg.to,"send contact")
                                kc1.sendText(msg.to,"send contact")
                                ke1.sendText(msg.to,"send contact")

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
                                cl.sendText(msg.to,"Refresh done")
                                ki.sendText(msg.to,"Refresh done")
                                kk.sendText(msg.to,"Refresh done")
                                kc.sendText(msg.to,"Refresh done")
                                ke.sendText(msg.to,"Refresh done")
                                cl1.sendText(msg.to,"Refresh done")
                                ki1.sendText(msg.to,"Refresh done")
                                kk1.sendText(msg.to,"Refresh done")
                                kc1.sendText(msg.to,"Refresh done")
                                ke1.sendText(msg.to,"Refresh done")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "read on" or text.lower() == 'autoread on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "read off" or text.lower() == 'autoread off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoRead"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Autojoin Tiket dinonaktifkan")

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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
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
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"send contact")

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
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
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
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"FunkZher Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"??FunkZher Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "?%i?User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses mengampuni para pendosa " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "?Pesan Msg?\nPesan Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "?Welcome Msg?\nWelcome Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "?Respon Msg?\nRespon Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["ARmessage1"] = spl
                                  cl.sendMessage(msg.to, "?Spam Msg?\nSpam Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "?Sider Msg?\nSider Msg diganti jadi :\n\n?{}?".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Pesan Msg?\nPesan Msg mu :\n\n? " + str(wait["message"]) + " ?")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Welcome Msg?\nWelcome Msg mu :\n\n? " + str(wait["welcome"]) + " ?")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Respon Msg?\nRespon Msg mu :\n\n? " + str(wait["Respontag"]) + " ?")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Spam Msg?\nSpam Msg mu :\n\n? " + str(Setmain["ARmessage1"]) + " ?")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "?Sider Msg?\nSider Msg mu :\n\n? " + str(wait["mention"]) + " ?")

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
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
