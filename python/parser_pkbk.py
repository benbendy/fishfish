#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

cur_line = 0
cur_file_name = ""
in_function = False
bracket_num = 0
function_line = 0

def my_print(error):
    print error, "in " , cur_file_name, ":", cur_line

def clean_html(content):
    ls = content.split("<")
    result = ""
    for l in ls:
        s = l.find(">") 
        if s > 0:
            tmp = l[s+1:] 
        else:
            tmp = l
            if tmp.find("div") >= 0:
                tmp =""
        result = result + " " + tmp
    return result  

def out_put(key, value):
    key = key.replace("\t"," ")
    key = key.replace("\r","")
    key = key.replace("\n","")
    key = key.replace("&nbsp;","")
    value = value.replace("\t"," ")
    value = value.replace("\r","")
    value = value.replace("\r","")
    value = value.replace("\n","")
    value = value.replace("\n","")
    value = value.replace("&#8226;",".")
    value = value.replace("&#8226;",".")
    value = value.replace("&#8226;",".")
    out = "%s\t%s" % (key, value)
    print out

def get_middle(content, s, e):
    ss = content.find(s)
    if ss >= 0:
        ss = ss + len(s)
        ee = content.find(e, ss)
        if ee >= 0:
            return content[ss:ee]
    return ""

def process_line(l , status):
    #if len(l) > 80:
    #    my_print("length more than 80")      
    
    check_prefix_space(l) 
    check_big_brackets(l)
    check_point_and_refer(l)

fp = open(sys.argv[1])
content = fp.read();
data = get_middle(content, "mr5xx", "bdshare")
#print data 
ls = data.split("font class")
for l in ls:
    ll =  l.replace("\r\n"," ").replace("nbsp&","").replace("<!---->","")
    #print ll
    if ll.find("m5kbt")> 0:
        out_put("name", get_middle(ll,"<a>","</a>"))
    else: 
        out_put(get_middle(ll,">","：") ,get_middle(ll,"font>","<").replace("&nbsp;"," "))



data = get_middle(content, "ShowPictureBox\">", "ShowBig")
ls = data.split("src=")
ls = ls[1:]
img = ""
for l in ls:
    tmp = get_middle(l,"\"","\"")
    if tmp != "":
        img = img + "," + tmp
if img != "":
   out_put("img", img[1:])

data = get_middle(content, "mk2bt", "mr5k2")
#print data
data =  data.replace("<font>","").replace("</font>","")
k = get_middle(data,">","<")

v = "" 
c = data.split("rgb(")
c = c[1:]
for cc in c:
    tmp =  get_middle(cc,">","</span>")
    if tmp != "":
        v = v + tmp
if v == "":
    v = get_middle(data,"12px\">","</span>")
if v == "":
    data = clean_html(data)
    v = data[16:]
v = v.replace("\r"," ") 
v = v.replace("\n"," ") 
#v = get_middle(data,"rgb(127, 127, 127)","/span>")
#print v
#v = get_middle(v,">","<")
    
out_put(k, v)
#exit(0)
data = get_middle(content, "productDescriptionSource", "mr5bot")
#print data
 
i = 0
ls = data.split("rgb(247, 150, 70)")
if len(ls) == 1:
    ls = data.split("FONT-SIZE: 14px\"")
ls = ls[1:]
for l in ls:
    i=i+1
    ll =  l.replace("<font>","").replace("</font>","")
    #print i, ll
    k = get_middle(ll,">","<")
    #if get_middle(ll,">","<") != "插图":
    if k != "插图" and  k != "插画":
        #print ll
        value = "" 
        c = ll.split("ans-serif")
        if len(c) == 1:
            c = ll.split("FONT-SIZE: 12px")
        c = c[1:]
        for cc in c:
            tmp =  get_middle(cc,">","</span>")
            if tmp != "":
                value = value + tmp
        out_put(k, value)
    else:
        value = "" 
        total = len(ls)
        for j in range(i, total):
            ll = ll + " " + ls[j] 
        #print ll
        c = ll.split("src")
        for cc in c:
            tmp =  get_middle(cc,"\"","\"")
            if tmp[-3:] == "jpg":
                value = value + "," + tmp
        if value != "":
            value = value[1:] 
        out_put(k, value)
        break;

