import pandas as pd
from tkinter import messagebox as m
col_names=['cough','sneeze','mucus','pain','weakness','lightfever','highfever','breath','label']
pima=pd.read_csv("Doc&PPTs\\coronasymptoms.csv",names=col_names)
feature=['cough','sneeze','mucus','pain','weakness','lightfever','highfever','breath']
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

###########################################
a,i,c,d,y,f,g,h=0,0,0,0,0,0,0,0
def C():
  global a
  a=1
def K():
  global i
  i=1
def M():
  global c
  c=1
def P():
  global d
  d=1
def O():
  global y
  y=1
def L():
  global f
  f=1
def H():
  global g
  g=1
def B():
  global h
  h=1
###################################
def predict():
    global LOGREG
    global logaccuracy
    logreg()
    global a
    global i
    global c
    global d
    global y
    global f
    global g
    global h
    l=LOGREG.predict([[a,i,c,d,y,f,g,h]])
    model=LogisticRegression(solver='liblinear')
    if l==0:
        m.showinfo(title="Corona Prediction",message="You Are Fine Dude...\n Just Chill !!!")
    elif l==1:
        m.showinfo(title="Corona Prediction",message="It's Only Air Pollution")
    elif l==2:
        m.showinfo(title="Corona Prediction",message="You Have Common Cold")
    elif l==3:
        m.showinfo(title="Corona Prediction",message="You Have Flu")
    elif l==4:
        m.showinfo(title="Corona Prediction",message="Warning!!!\nCororna Detected!!!")
    else:
        m.showinfo(title="Corona Prediction",message="U Don't Have Any Symptom Of Corona\nOR\nAny Related Disease...")
##############################
from tkinter import *
w=Tk()
w.title("Corona Prediction System")
title=Label(w,text="Click On The Symptoms",font=('arial',20,'bold'))
title.grid(row=1,column=1,columnspan=4)
cough=Button(w,text="Dry\nCough",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=C)
cough.grid(row=2,column=1)
sneeze=Button(w,text="Sneeze\n ",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=K)
sneeze.grid(row=2,column=2)
mucus=Button(w,text="Mucus\n ",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=M)
mucus.grid(row=3,column=2)
pain=Button(w,text="Body\nPain",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=P)
pain.grid(row=4,column=1)
weakness=Button(w,text="Weakness\n ",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=O)
weakness.grid(row=3,column=1)
highfever=Button(w,text="High\nFever",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=H)
highfever.grid(row=5,column=1)
lightfever=Button(w,text="Light\nFever",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=L)
lightfever.grid(row=5,column=2)
breath=Button(w,text="Breathing\nDifficulty",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='red',command=B)
breath.grid(row=4,column=2)
btnpredict=Button(w,text="Predict",bg='yellow',width=10,relief='groove',font=('arial',20,'bold'),fg='green',command=predict)
btnpredict.grid(row=6,column=1)
w.mainloop()
