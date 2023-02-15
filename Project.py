from tkinter import *
from datetime import datetime
import requests


root = Tk()

stations = 'หลักสอง บางแค ภาษีเจริญ เพชรเกษม48 บางไผ่ บางหว้า ท่าพระ อิสระภาพ สนามไชย สามยอด วัดมังกร หัวลำโพง สามย่าน สีลม ลุมพินี คลองเตย ศูนย์ประชุมแห่งชาติศิริกิติ์ สุขุมวิท เพชรบุรี พระราม9 ศูนย์วัฒนธรรมแห่งประเทศไทย ห้วยขวาง สุทธิสาร รัชดาภิเษก ลาดพร้าว พหลโยธิน สวนจตุจักร กำแพงเพชร บางซื่อ เตาปูน บางโพ บางอ้อ บางพลัด สิรินธร บางยี่ขัน บางขุนนนท์ ไฟฉาย จรัญฯ13'.split(' ')

headLabel = Label(text='MRT Blue line Station Board',bg='darkblue',fg='yellow')
headLabel.grid(row=0,columnspan=5,sticky=NSEW)

dttime = datetime.now().strftime('%H:%M:%S')
timeLabel = Label(text=dttime,bg='light yellow')
timeLabel.grid(row=1,columnspan=5,sticky=NSEW)
def tick():
    curtime = datetime.now().time()
    ftime = curtime.strftime('%H:%M:%S')

    timeLabel.config(text=ftime)
    timeLabel.after(1000,tick)
tick()

message = StringVar()
fromStation = StringVar()
toStation = StringVar()

mapPhoto = PhotoImage(file='map.png')
mapLabel = Label(anchor=N,image=mapPhoto)
mapLabel.grid(row=2,columnspan=5)

def line():
    url = 'https://notify-api.line.me/api/notify'
    token = 'gJ0UfDviOtfAhQLHysCucdYf0jJ7VV3gyHm4RvIlZuE'
    headers = {'Authorization':'Bearer '+token}

    requests.post(url=url,headers=headers,data={'message':message.get()})

sendButton = Button(root,text=f'ส่งข้อความ : {message.get()}',command=line,bg='papayawhip')
sendButton.grid(row=3,columnspan=10,sticky=NSEW)

def a(e):
    station = e.widget.cget('text')
    if fromStation.get() == '':
        if toStation.get() == station:
            toStation.set('')
            e.widget['bg'] = 'white'
        else:
            fromStation.set(station)
            e.widget['bg'] = 'green'
    elif fromStation.get() == station:
        fromStation.set('')
        e.widget['bg'] = 'white'
    elif toStation.get() == '':
        toStation.set(station)
        e.widget['bg'] = 'red'
    elif toStation.get() == station:
        toStation.set('')
        e.widget['bg'] = 'white' 

    if fromStation.get() != '' and toStation.get() != '':
        message.set(f'อยู่สถานี{fromStation.get()} กำลังไปสถานี{toStation.get()}')
    elif fromStation.get() == '' and toStation.get() == '':
        message.set('')
    elif fromStation.get() != '':
        message.set(f'อยู่สถานี{fromStation.get()}')
    elif toStation.get() != '':
        message.set(f'กำลังไปสถานี{toStation.get()}')
    sendButton.config(text=f'ส่งข้อความ : {message.get()}')

buttonList = []
for station in stations:
    buttonList.append(Button(root,text=station,bg='white'))
for i in range(len(buttonList)):
    buttonList[i].grid(row=4 + i//5,column=i%5,sticky=NSEW)
    buttonList[i].bind('<Button-1>',a)


root.mainloop()