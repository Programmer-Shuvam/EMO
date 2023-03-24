import pandas as pd
from tkinter import messagebox as m
col_names=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']
pima=pd.read_csv("Doc&PPTs\\pima.csv",names=col_names)
feature=['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age']
median_bmi = pima['bmi'].median()
pima['bmi'] = pima['bmi'].replace(to_replace=0, value=median_bmi)
median_bp = pima['bp'].median()
pima['bp'] = pima['bp'].replace(to_replace=0, value=median_bp)
median_glucose = pima['glucose'].median()
pima['glucose'] = pima['glucose'].replace(to_replace=0, value=median_glucose)
median_skin=pima['skin'].median()
pima['skin'] = pima['skin'].replace(to_replace=0, value=median_skin)
median_insulin=pima['insulin'].median()
pima['insulin'] = pima['insulin'].replace(to_replace=0, value=median_insulin)
X=pima[feature]
Y=pima.label
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=5)
from sklearn.linear_model import LogisticRegression
logaccuracy=0
global LOGREG
LOGREG=LogisticRegression()
def logreg():
    global logaccuracy
    LOGREG.fit(X_train,Y_train)
    Y_pred=LOGREG.predict(X_test)
    from sklearn import metrics
    confusion=metrics.confusion_matrix(Y_test,Y_pred)
    TP=confusion[1,1]
    TN=confusion[0,0]
    FP=confusion[0,1]
    FN=confusion[1,0]
    sensitivity=TP/(TP+FN)                      
    specificity=TN/(TN+FP)
    logaccuracy=round(((TP+TN)/(TP+TN+FP+FN)),2)*100
from tkinter import *
w=Tk()
w.geometry("550x450")
w.title("Diabetes Prediction System")
w.resizable(0,0)
vpreg=StringVar()
vglucose=StringVar()
vbp=StringVar()
vskin=StringVar()
vinsulin=StringVar()
vbmi=StringVar()
vpedegree=StringVar()
vage=StringVar()
def predict():
    global LOGREG
    global logaccuracy
    logreg()
    try:
        a=float(vpreg.get())
        b=float(vglucose.get())
        c=float(vbp.get())
        d=float(vskin.get())
        e=float(vinsulin.get())
        f=float(vbmi.get())
        g=float(vpedegree.get())
        h=float(vage.get())  
    except:
        reset()
    l=LOGREG.predict([[a,b,c,d,e,f,g,h]])
    model=LogisticRegression(solver='liblinear')
    if l==0:
        m.showinfo(title="Diabetes Prediction",message="You Have No Diabetes")
    else:
        m.showinfo(title="Diabetes Prediction",message="You have Diabetes or may get soon")     
def reset():
    vpreg.set("")
    vglucose.set("")
    vbp.set("")
    vskin.set("")
    vinsulin.set("")
    vbmi.set("")
    vpedegree.set("")
    vage.set("")
labeltitle=Label(w,text="Enter Your Details!!!!",fg='red',font=('arial',20,'bold'))
labeltitle.grid(row=1,column=2,columnspan=2)
labelpreg=Label(w,text="Pregnant",font=('arial',20,'bold'))
labelpreg.grid(row=2,column=2)
entrypreg=Entry(w,font=('arial',20,'bold'),textvariable=vpreg)
entrypreg.grid(row=2,column=3)
labelglucose=Label(w,text="Glucose",font=('arial',20,'bold'))
labelglucose.grid(row=3,column=2)
entryglucose=Entry(w,font=('arial',20,'bold'),textvariable=vglucose)
entryglucose.grid(row=3,column=3)
labelbp=Label(w,text="Blood Pressure",font=('arial',20,'bold'))
labelbp.grid(row=4,column=2)
entrybp=Entry(w,font=('arial',20,'bold'),textvariable=vbp)
entrybp.grid(row=4,column=3)
labelskin=Label(w,text="Skin",font=('arial',20,'bold'))
labelskin.grid(row=5,column=2)
entryskin=Entry(w,font=('arial',20,'bold'),textvariable=vskin)
entryskin.grid(row=5,column=3)
labelinsulin=Label(w,text="Insulin",font=('arial',20,'bold'))
labelinsulin.grid(row=6,column=2)
entryinsulin=Entry(w,font=('arial',20,'bold'),textvariable=vinsulin)
entryinsulin.grid(row=6,column=3)
labelbmi=Label(w,text="Body Mass Index",font=('arial',20,'bold'))
labelbmi.grid(row=7,column=2)
entrybmi=Entry(w,font=('arial',20,'bold'),textvariable=vbmi)
entrybmi.grid(row=7,column=3)
labelpedegree=Label(w,text="Pedegree",font=('arial',20,'bold'))
labelpedegree.grid(row=8,column=2)
entrypedegree=Entry(w,font=('arial',20,'bold'),textvariable=vpedegree)
entrypedegree.grid(row=8,column=3)
labelage=Label(w,text="Age",font=('arial',20,'bold'))
labelage.grid(row=9,column=2)
entryage=Entry(w,font=('arial',20,'bold'),textvariable=vage)
entryage.grid(row=9,column=3)
btnpredict=Button(w,text="Predict",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='green',command=predict)
btnpredict.grid(row=10,column=2)
btnreset=Button(w,text="Reset",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='green',command=reset)
btnreset.grid(row=10,column=3)
w.mainloop()
