#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
# 
import time
from ..itchat import send
from ..itchat.content import *
from ..wechatRecord import *


def response(busyContent, msg, userName):
	if msg['Type'] in [SYSTEM, FRIENDS, NOTE]: return #不回复此类消息
	if msg["FromUserName"] == userName: return #不回复自己发送的消息
	busyContent = busyContent.split('|')
	for m in busyContent:
		send(m, msg["FromUserName"])
		recordUserConfig({"sendMsgCount" : 1}, "add") #发送消息数加一
		time.sleep(1)
	return