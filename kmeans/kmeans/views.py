from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms  import UploadFileForm
from django.core.files.storage import default_storage

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





def output(request):
    
    import pandas as pd
    import numpy as np
    import io
    import os
    import math
    import matplotlib.pyplot as plt
    data=''

    #from numpy.lib.function_base import append
    from mpl_toolkits.mplot3d import Axes3D

    url = default_storage.path("data.csv")
    #url=UploadFileForm.file

    df2 = pd.read_csv(url)
    print(df2)
    ar=df2.to_numpy()
    os.remove(url)
    

    def show(clster):
        i=0
        datap=''
        while(i<n):
            l=len(clster[i])
            l=l/co
            
            #print("\n\nThe number of tuple  in clster ",i+1,"is :",l) 
            datap=datap+'\n\nThe number of tuple  in Group '+str(i+1)+' is :'+str(l)

         
            i=i+1

        return datap

        
    
    #below function is used to see the clster value
    '''i=0
    while(i<n):
        print("\n\n\n\nThe data are in clster :",i+1)
        l=len(clster[i])
        #l=l/co
        r=0
        q=1
        pp=0
        while(r<l):
        print(clster[i][r],end=' ')
        if(q%co==0):
            print("\n")
            q=1
        else:
            q=q+1  
        r=r+1
        i=i+1'''

    #######################################################
    def update_mean(clster):
        mean2=[]
        for x in range(0,n):
            mean2.append([])

        i=0
        while(i<n):
            l=len(clster[i])
            q=0
            while(q<co):
                y=q
                e=q
                mt=0
                while(e<l):
                    mt=mt+clster[i][e]                   
                    e=e+co
                if(l==0):
                    mt=0
                else:
                    mt=mt/(l/co)  
                
                mean2[i].append(mt)
                q=q+1 
            i=i+1       
        return mean2    
        ##########################################################

    def check_mean(mean,mean2): 
        i=0
        while(i<n):
            pc=0
            while(pc<co):
                if(mean[i][pc]!=mean2[i][pc]):
                    return 0            
                pc=pc+1 
            i=(i+1)
        return 1

    ########################################################
    import statistics
    k=len (df2)
    co=len (df2.columns)
    
    #n=number of clster
    n=2

    mean=[]
    for x in range(0,n):
        mean.append(ar[x])

    #mean=[[144552912,9.354581,56.7411511,18.39748246],[144552912,9.3498486,56.7408757,17.05277157]]

    """
    i=0
    v=10
    while(i<n):
    p=0
    while(p<co):
        mean[i].append(float(input()))
        #mean[i].append(v)
        v=v+1
        p=p+1
    #mean[i].append(int(input()))
    i=(i+1)

    #print(mean[0][0],"\n\n\n")
    """
    ##################################################################################################################
    zz=10






    r=0

    while(1):
        r=r+1
        clster=[]
        for x in range(0,n):
            clster.append([])
        
        i=0
        while(i<k):
            distance =[] 
            x=0;
            while(x<n):
                p=0
                dis=0
                while(p<co):

                    dis=dis+((ar[i][p]-mean[x][p])*(ar[i][p]-mean[x][p]))
                    p=p+1
                dis=math.sqrt(dis)
                distance.append(dis) 
                dis=0    
                x=x+1
            
            index=0
            mini=1000000000000;
            x=0;

            while(x<n):

                if(distance[x]<mini):
                    mini=distance[x]
                    index=x
                x=x+1
            p=0
            ###need to fix after this line
            while(p<co):
                clster[index].append(ar[i][p])
                p=p+1  

            
            i=i+1
        flag=0
        y=0

        mean2=update_mean(clster)

        flag=check_mean(mean,mean2)

        if(flag==1):
            data=data+show(clster)
            break
        else:
            mean=mean2
            continue 

    data=data+'.\n   The final mean is '+str(mean[0])+' and '+ str(mean[1])
    co=len (df2.columns)        
    if(co>2):

        xx=[]
        yy=[]
        zz=[]

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #print(clster)
        i=0
        while(i<n):
            l=len(clster[i])
            xc=0
            while(xc<l):
                xx.append(clster[i][xc])
                xc=xc+co
            
            yc=1
            while(yc<l):
                yy.append(clster[i][yc])
                yc=yc+co

            zc=2
            while(zc<l):
                zz.append(clster[i][zc])
                zc=zc+co

            i=i+1
            color=[]
            colo = ['green','red','black','blue']

            ax.scatter(xx, yy, zz,color = colo[i])
            xx=[]
            yy=[]
            zz=[]
        
        

        ax.set_xlabel('Age')
        ax.set_ylabel('Annual Income')
        ax.set_zlabel('Spending Score')

        plt.show()

    elif co==2:
        xx=[]
        yy=[]


        fig = plt.figure()
        #  ax = fig.add_subplot(111, projection='3d')

        #print(clster)
        i=0
        while(i<n):
            l=len(clster[i])
            xc=0
            while(xc<l):
                xx.append(clster[i][xc])
                xc=xc+co
            
            yc=1
            while(yc<l):
                yy.append(clster[i][yc])
                yc=yc+co

            i=i+1
            color=[]
            color = ['green','red','black','blue']

            plt.scatter(xx, yy,color = color[i])
            xx=[]
            yy=[]

        plt.show()

    
    else:

    #print(clster)
        i=0
        while(i<n):
            l=len(clster[i])
            xc=0
            xx=[]
            while(xc<l):
                xx.append(clster[i][xc])
                xc=xc+co

            i=i+1
            color=[]
            color = ['green','red','black','blue']
            plt.plot(xx,len(xx)*[1],"x")
            
            xx=[]
            yy=[]

        plt.show()




    return render(request,'second.html',{'data':data})
