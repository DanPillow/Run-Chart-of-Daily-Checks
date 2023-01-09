# Libraries/Modues Import
import glob
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askdirectory


#file paths with glob
path = askdirectory(title='Select Folder') # shows dialog box and return the path
#path=r'C:\Users\d.pillow\Desktop\25-May\Daily Checks'
all_files=glob.glob(path + r"/*.csv")

#Variables:
li=[]
KeyData=['Date','IONMAX','ION','IOFFMEDIAN','VT']

#loop to combine all CSV files within the specified folder to list (li)
for filename in all_files:
    df=pd.read_csv(filename, header=1)
    df.insert(0, "Date", (datetime.strptime(str(filename[-14:-4]), '%d-%m-%Y').date()), allow_duplicates = True)
    li.append(df)

#Converts the list (li) to a Data Frame (df)
df=pd.concat(li,axis=0, ignore_index=False)

#Extract the key variables (as declared within 'KeyData' variable) and converts it to CSV file:
tmpdata = df[KeyData].sort_values(["Date"], ascending=False)
tmpdata=tmpdata[(tmpdata["ION"]>0)]
tmpdata=tmpdata.sort_values(["Date"], ascending=False)
tmpdata=tmpdata[(tmpdata["ION"]>0)]


#Displays graph:

plt.subplot(211)#1
plt.plot(tmpdata["Date"],tmpdata["ION"], color='green',linestyle='--')
plt.title("Ion Variation")
plt.xlabel("Date")
plt.ylabel("Ion (A)")
plt.grid(True)


plt.subplot(212)#2
plt.plot(tmpdata["Date"],tmpdata["IOFFMEDIAN"], color='green',linestyle='--')
plt.title("Ioff Variation")
plt.xlabel("Date")
plt.ylabel("Ioff (A)")
plt.grid(True)

plt.subplots_adjust(hspace=0.8)
plt.show()

#plt.figure()    #3 
plt.plot(tmpdata["Date"],tmpdata["VT"], color='green',linestyle='--')
plt.title("VT Variation")
plt.xlabel("Date")
plt.ylabel("VT (V)")
plt.grid(True)

plt.show()

#Converts data to CSV
tmpdata[(tmpdata["ION"]>0)].to_csv("Daily Checks Subset.csv", encoding='utf-8', index=False)



#Confirms completion:
print("Combine Complete")

