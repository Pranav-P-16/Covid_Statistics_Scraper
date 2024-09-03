import requests,datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PySimpleGUI import *
def e_r_alert(tx):
    theme("Topanga")
    lyt=[[Text("\t")]+[Text(tx,font=("Helvetica",15))]+[Text("\t")],
         [Button("Retry",button_color=("orange","black"),size=(10,1))]+[Button("Exit",button_color=("red","black"),size=(10,1))]]
    wnd=Window("Alert !!!",lyt,element_justification="c",keep_on_top=True)
    event,values=wnd.read()
    wnd.close()
    return event
def net_connection():
    try:
        urlopen('https://www.google.com',timeout=4)
        return True
    except:
        k=e_r_alert("NO INTERNET CONNECTION !")
        if k=="Retry":
            net_connection()
        else:
            exit()
def covid():
    theme("DarkBrown")
    t=datetime.datetime.now()
    lt=[[Text("\tCOVID STATISTICS\t",font=("Linux Libertine Initials O",20))],[Text()],[Text("Loading...",key="lastupdated",font=("Chilanka",20),text_color="green2")],[Text()],[Text("Loading...",key="tpr",font=("Chilanka",19),text_color="orange")],[Text()],
        [Text("Loading...",key="yr",text_color="yellow",font=("Chilanka",18))],[Text("Loading...",key="dy",text_color="red",font=("Chilanka",18))],[Text("Loading...",key="yre",text_color="green2",font=("Chilanka",18))],
        [Text("Loading...",key="acy",text_color="violet",font=("Chilanka",18))],[Text()],[Text("Loading...",key="tc",text_color="yellow",font=("Chilanka",18))],[Text("Loading...",key="tac",text_color="violet",font=("Chilanka",18))],
        [Text("Loading...",key="td",font=("Chilanka",18),text_color="red")],[Text("Loading...",key="tr",font=("Chilanka",18),text_color="green2")],
        [Text("* There is a spike in death counts from 22-10-2021 due to releasing pending appeal counts",text_color="red")],[Text()],[Text("Checked at "+str(t.hour)+":"+str(t.minute)+":"+str(t.second)+"\t"*6,key="cha")]+[Button("Refresh")]]
    wn=Window("Covid Statistics",lt)
    o=0
    while True:
        if o==0:
            e,v=wn.read(timeout=1000)
        else:
            e,v=wn.read()
        if e==None:
            exit()
        o+=1
        net_connection()
        url5="https://dashboard.kerala.gov.in/covid/"
        page5=requests.get(url5)
        soup5=BeautifulSoup(page5.content,"html.parser")
        results5=soup5.find(class_="small-box bg-info")
        results6=soup5.find(class_="small-box bg-danger")
        results7=soup5.find(class_="small-box bg-success")
        results8=soup5.find(class_="card-body pt-2 pb-3 pb-sm-0 pb-lg-0")
        results9=soup5.find(class_="row mb-2")
        results10=soup5.find(class_="small-box bg-warning")
        update=results9.find("ol",class_="breadcrumb float-sm-right")
        cc=results5.find_all("div",class_="inner")
        de=results6.find_all("div",class_="inner")
        reco=results7.find_all("div",class_="inner")
        tpr=results8.find_all("div",class_="col-md-7 col-12")
        tac=results10.find_all("div",class_="inner")
        update=str(update)
        update=update[74:]
        update=update[:-11]
        current_time = datetime.datetime.now()
        da=""
        if update[9]+update[10]==str(current_time.day):
            da="Today"
        else:
            da="Yesterday"
        print("*** Last",update,"***")
        wn.find_element("lastupdated").Update("*** Last "+update+" ***")
        for yy in tac:
            tact=yy.find(class_="my-0 my-lg-1")
        for yu in tpr:
            ttpr=yu.find(class_="mb-0")
        for t in cc:
            tcc=t.find(class_="my-0 my-lg-1")
        for z in de:
            tde=z.find(class_="my-0 my-lg-1")
        for y in reco:
            tre=y.find(class_="my-0 my-lg-1")
        tact=str(tact.text)
        ttpr=str(ttpr.text)
        tre=str(tre.text)
        tde=str(tde.text)
        cases=str(tcc.text)
        r0=""
        for i in tact:
            if i!="(":
                r0+=i
            else:
                break
        bracket0=tact.find("(")
        r=""
        for j in cases:
            if j!="(":
                r+=j
            else:
                break
        bracket=cases.find("(")
        r2=""
        for j in tde:
            if j!="(":
                r2+=j
            else:
                break
        
        td_e=tde.find("(")
        r3=""
        for j in tre:
            if j!="(":
                r3+=j
            else:
                break
        tre_1=tre.find("(")
        print()
        print("* "+da+"'s Test Positivity Rate :",ttpr,end="")
        wn.find_element("tpr").Update("* "+da+"'s Test Positivity Rate :"+str(ttpr)+"%")

        print("%")
        print()
        bracket=cases.find("(")
        kl1="* "+da+" Reported : "+cases[bracket+2 : -1]
        print(kl1)
        wn.find_element("yr").Update(kl1)
        kl2="* Death "+da+" : "+tde[td_e+2:-1]
        print(kl2)
        wn.find_element("dy").Update(kl2)
        kl3="* "+da+" Recovered : "+tre[tre_1+2:-1]
        print(kl3)
        wn.find_element("yre").Update(kl3)
        kl4="* Active Cases "+da+" : "+tact[bracket0+2:-1]
        print(kl4)
        wn.find_element("acy").Update(kl4)
        print()
        print("$ Total Confirmed :",r)
        wn.find_element("tc").Update("$ Total Confirmed : "+r)
        print("$ Total Active Cases :",r0)
        wn.find_element("tac").Update("$ Total Active Cases : "+r0)
        print("$ Total Death :",r2)
        wn.find_element("td").Update("$ Total Death : "+r2)
        print("$ Total Recovered :",r3)
        wn.find_element("tr").Update("$ Total Recovered : "+r3)
        t=datetime.datetime.now()
        wn.find_element("cha").Update("Checked at "+str(t.hour)+":"+str(t.minute)+":"+str(t.second)+"\t"*6)
covid()
