import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tkinter import messagebox as m
# for column name refer to readme.docx
col_names=['sr','rr','bt','lmr','bo','em','sh','hr','sl']
pima=pd.read_csv("Doc&PPTs\\SaYoPillow.csv",names=col_names)
feature=['sr','rr','bt','lmr','bo','em','sh','hr']
median_sr = pima['sr'].median()
pima['sr'] = pima['sr'].replace(to_replace=0, value=median_sr)
median_rr = pima['rr'].median()
pima['rr'] = pima['rr'].replace(to_replace=0, value=median_rr)
median_bt = pima['bt'].median()
pima['bt'] = pima['bt'].replace(to_replace=0, value=median_bt)
median_lmr=pima['lmr'].median()
pima['lmr'] = pima['lmr'].replace(to_replace=0, value=median_lmr)
median_bo=pima['bo'].median()
pima['bo'] = pima['bo'].replace(to_replace=0, value=median_bo)
median_em=pima['em'].median()
pima['em'] = pima['em'].replace(to_replace=0, value=median_em)
median_sh=pima['sh'].median()
pima['sh'] = pima['sh'].replace(to_replace=0, value=median_sh)
median_hr=pima['hr'].median()
pima['hr'] = pima['hr'].replace(to_replace=0, value=median_hr)
X=pima[feature]
Y=pima.sl

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
global LOGREG
LOGREG=LogisticRegression(C=10, penalty='l1',solver='saga',multi_class='multinomial',max_iter=1000)

global Y_pred
LOGREG.fit(X_train,Y_train)
Y_pred=LOGREG.predict(X_test)

from tkinter import *
w=Tk()
w.geometry("550x450")
w.title("Stress Monitoring System")
w.resizable(0,0)
vsr=StringVar()
vrr=StringVar()
vbt=StringVar()
vlmr=StringVar()
vbo=StringVar()
vem=StringVar()
vsh=StringVar()
vhr=StringVar()

def predict():
    try:
        a=float(vsr.get())
        b=float(vrr.get())
        c=float(vbt.get())
        d=float(vlmr.get())
        e=float(vbo.get())
        f=float(vem.get())
        g=float(vsh.get())
        h=float(vhr.get())  
    except:
        reset()
    l=LOGREG.predict([[a,c,b,d,e,f,g,h]])
    if l==0:
        m.showinfo(title="Stress Monitor",message="Stress Level Between 0-20%\nYou don't have anxiety issues.")
    elif l==1:
        m.showinfo(title="Stress Monitor",message="Stress Level Between 21-40%\nYou are having mild anxiety.")
    elif l==2:
        m.showinfo(title="Stress Monitor",message="Stress Level Between 41-60%\nYou are having mild anxiety, you should drink more water.")
    elif l==3:
        m.showinfo(title="Stress Monitor",message="Stress Level Between 61-80%\nYou are having moderate anxiety, you should drink more water.")
    elif l==4:
        m.showinfo(title="Stress Monitor",message="Stress Level Between 81-100%\nYou are having severe anxiety, you should consult with therapist or doctor and do yoga.")

def reset():
    vsr.set("")
    vbt.set("")
    vrr.set("")
    vlmr.set("")
    vbo.set("")
    vem.set("")
    vsh.set("")
    vhr.set("")

labeltitle=Label(w,text="Enter Your Details!!!!",fg='red',font=('arial',20,'bold'))
labeltitle.grid(row=1,column=2,columnspan=2)
labelsr=Label(w,text="Snoring Range",font=('arial',20,'bold'))
labelsr.grid(row=2,column=2)
entrysr=Entry(w,font=('arial',20,'bold'),textvariable=vsr)
entrysr.grid(row=2,column=3)
labelbt=Label(w,text="Body Temperature",font=('arial',20,'bold'))
labelbt.grid(row=3,column=2)
entrybt=Entry(w,font=('arial',20,'bold'),textvariable=vbt)
entrybt.grid(row=3,column=3)
labelrr=Label(w,text="Respiration Rate",font=('arial',20,'bold'))
labelrr.grid(row=4,column=2)
entryrr=Entry(w,font=('arial',20,'bold'),textvariable=vrr)
entryrr.grid(row=4,column=3)
labellmr=Label(w,text="Limb Movement Rate",font=('arial',20,'bold'))
labellmr.grid(row=5,column=2)
entrylmr=Entry(w,font=('arial',20,'bold'),textvariable=vlmr)
entrylmr.grid(row=5,column=3)
labelbo=Label(w,text="Blood Oxygen Levels",font=('arial',20,'bold'))
labelbo.grid(row=6,column=2)
entrybo=Entry(w,font=('arial',20,'bold'),textvariable=vbo)
entrybo.grid(row=6,column=3)
labelem=Label(w,text="Eye Movement",font=('arial',20,'bold'))
labelem.grid(row=7,column=2)
entryem=Entry(w,font=('arial',20,'bold'),textvariable=vem)
entryem.grid(row=7,column=3)
labelsh=Label(w,text="Sleeping Hours",font=('arial',20,'bold'))
labelsh.grid(row=8,column=2)
entrysh=Entry(w,font=('arial',20,'bold'),textvariable=vsh)
entrysh.grid(row=8,column=3)
labelhr=Label(w,text="Heart Rate",font=('arial',20,'bold'))
labelhr.grid(row=9,column=2)
entryhr=Entry(w,font=('arial',20,'bold'),textvariable=vhr)
entryhr.grid(row=9,column=3)
btnpredict=Button(w,text="Predict",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='green',command=predict)
btnpredict.grid(row=10,column=2)
btnreset=Button(w,text="Reset",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='green',command=reset)
btnreset.grid(row=10,column=3)
w.mainloop()