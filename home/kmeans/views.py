from django.shortcuts import render
from django.http import HttpResponse
import requests
from sklearn.semi_supervised import SelfTrainingClassifier
from .forms  import UploadFileForm
from django.core.files.storage import default_storage
a=0
b=0
c=0

#from forms import UploadFileForm

def ahre(request):
    return render(request,'second.html')

def ahree(request):
    return render(request,'home.html')









                  
def button(request):
    return render(request,'home.html')



def upload_file(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST , request.FILES)
        file=request.FILES['file']
        #file = request.FILES['myfile']
        file_name = default_storage.save("data.csv", file)
        return render(request,'second.html')
    else:
        form=UploadFileForm()

    return render(request,'home.html',{'form': form})    

def upload_data(request):
    if request.method=='POST':
        a=request.POST["rooms"]
        b=request.POST["bathrooms"]
        c=request.POST["size"]
        print(a)
        print(c)
        print(b)
        print("done")
        
        return render(request,'second.html')
    else:
        form=UploadFileForm()

    return render(request,'home.html',{'form': form})    






def output(request):
    import pandas as pd
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    from sklearn.linear_model import LinearRegression



    if request.method=='POST':
        a=request.POST["rooms"]
        b=request.POST["bathrooms"]
        c=request.POST["size"]
    
    url = default_storage.path("data.csv")
    #url=UploadFileForm.file

    df2 = pd.read_csv(url)
    #os.remove(url)
    #print(df2)
    ar=df2.to_numpy()
    arr = np.transpose(ar)






    rooms = arr[0]
    bathrooms = arr[1]
    size = arr[2]
    rent = arr[3]



    # Create feature matrix X by combining the three features
    X = list(zip(rooms, size, bathrooms))

    # Create target variable y
    y = rent

    # Create and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict rent for a new home
    a=int(a)
    b=int(b)
    c=int(c)
    new_home = [(a,c,b)]

    predicted_rent = model.predict(new_home)
    print(a)
    print(c)
    print(b)
    #print("Predicted rent:", predicted_rent) 
    data=" Predicted rent : " +str(predicted_rent)  
    
   



    return render(request,'second.html',{'data':data})
