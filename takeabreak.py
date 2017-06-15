import webbrowser
import time

count=0;
print ("This program started on " +time.ctime())
while(count<3):
    time.sleep(10)
    webbrowser.open("http://gaana.com/album/despacito-remix");
    count= count+1


print ("This program ended on " +time.ctime())
