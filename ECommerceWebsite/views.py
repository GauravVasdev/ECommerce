from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from ECommerceWebsite.models import PersonData
import pyodbc
import json
conn=pyodbc.connect('Driver={SQL server};'
                        r'Server=DESKTOP-I40FBR6\SQLEXPRESS;'
                        'Database=Ecommercedatabase;'
                        'Trusted_Connection=yes;')
cursor=conn.cursor()
def homepage(request):
    return render(request,"Homepageofecommerce.html")
def men_items(request):
        if(request.GET.get('name')):
            C_ID=request.GET.get('C_ID')
            customername=request.GET.get('name')
            cursor.execute("Select * from product_category where person_category_ID=1")
            result=cursor.fetchall()
            conn.commit()
            cursor.execute("Select * from product_details where product_category_Id=1")
            result_details=cursor.fetchall()
            conn.commit()
            cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
            no_of_items=cursor.fetchall()
            return render(request,"men_items/men_items.html",{'name':customername,'result':result,'result_details':result_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
        else:
            C_ID=request.GET.get('C_ID')
            cursor.execute("Select * from product_category where person_category_ID=1")
            result=cursor.fetchall()
            cursor.execute("Select * from product_details where product_category_Id=1")
            result_details=cursor.fetchall()
            cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
            no_of_items=cursor.fetchall()
            return render(request,"men_items/men_items.html",{'result':result,'result_details':result_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def women_items(request):
    if(request.GET.get('name')):
        C_ID=request.GET.get('C_ID')
        customername=request.GET.get('name')
        cursor.execute("Select * from product_category where person_category_ID=1")
        result=cursor.fetchall()
        cursor.execute("Select * from product_details where product_category_Id=1")
        result_details=cursor.fetchall()
        return render(request,"women_items/women_items.html",{'name':customername,'result':result,'result_details':result_details,'C_ID':C_ID})
    else:
        C_ID=request.GET.get('C_ID')
        cursor.execute("Select * from product_category where person_category_ID=2")
        result=cursor.fetchall()
        cursor.execute("Select * from product_details where product_category_Id=8")
        result_details=cursor.fetchall()
        cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
        no_of_items=cursor.fetchall()
    return render(request,"women_items/women_items.html",{'result':result,'result_details':result_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def loginforecommerce(request):
    if(request.POST.get('C_Name')):
        C_Name=request.POST.get('C_Name')
        C_Email=request.POST.get('C_Email')
        C_Password=request.POST.get('C_Password')
        cursor.execute("Select * from person_details where  CONVERT(VARCHAR,C_Name)= ? and  CONVERT(VARCHAR,C_EmailID)= ? and  CONVERT(VARCHAR,C_Password)= ? ",C_Name,C_Email,C_Password)
        result=cursor.fetchall()
        if(len(result)==0):
            return HttpResponse("No")
        else:
            return  HttpResponse(result[0])
    else:
        return render(request,'loginforecommerce.html')
def Registerforecommerce(request):
    if(request.POST.get('C_Name')):
        Person=PersonData()
        Person.C_Name=request.POST.get('C_Name')
        Person.C_EmailID=request.POST.get('C_Email')
        Person.C_Password=request.POST.get('C_Password')
        cursor.execute("insert into person_details values(?,?,?)",Person.C_Name,Person.C_EmailID,Person.C_Password)
        cursor.commit()
        return HttpResponse("Done")
    else:
        return render(request,'Registerforecommerce.html')
def mentshirtcollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=1")
    result=cursor.fetchall()
    conn.commit()
    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=2 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=2 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=2")
        product_details=cursor.fetchall()
        conn.commit()
    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'men_items/menTshirtCollection/menT-shirtcollection.html',{'result':result,'product_details':product_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def menshoescollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=1")
    result=cursor.fetchall()
    conn.commit()
    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=3 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=3 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=3")
        product_details=cursor.fetchall()
        conn.commit()
    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'men_items/menShoesCollection/menshoescollection.html',{'result':result,'product_details':product_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def menwatchcollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=1")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=4 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=4 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=4")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'men_items/menWatchCollection/menwatchescollection.html',{'result':result,'product_details':product_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def mensunglassescollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=1")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=5 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=5 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=5")
        product_details=cursor.fetchall()
        conn.commit()


    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'men_items/menSunglassesCollection/mensunglassescollection.html',{'result':result,'product_details':product_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def menjeanscollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=1")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=6 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=6 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=6")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'men_items/menjeansCollection/menjeanscollection.html',{'result':result,'product_details':product_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def menperfumecollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=1")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=7 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=7 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=7")
        product_details=cursor.fetchall()
        conn.commit()


    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'men_items/menPerfumeCollection/menperfumecollection.html',{'result':result,'product_details':product_details,'person_category_id':1,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def womentshirtcollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=2")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=9 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=9 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=9")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'Women_items/womentshirtcollection/womentshirtcollection.html',{'result':result,'product_details':product_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def womenshoescollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=2")
    result=cursor.fetchall()
    conn.commit()

    
    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=10 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=10 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=10")
        product_details=cursor.fetchall()
        conn.commit()


    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'Women_items/womenshoescollection/womenshoescollection.html',{'result':result,'product_details':product_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def womenwatchcollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=2")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=11 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=11 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=11")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'Women_items/womenwatchescollection/womenwatchescollection.html',{'result':result,'product_details':product_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def womensunglassescollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=2")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=12 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=12 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=12")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'Women_items/womensunglassescollection/womensunglassescollection.html',{'result':result,'product_details':product_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def womenjeanscollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=2")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=13 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=13 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=13")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'Women_items/womenjeanscollection/womenjeanscollection.html',{'result':result,'product_details':product_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def womenperfumecollection(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from product_category where person_category_ID=2")
    result=cursor.fetchall()
    conn.commit()

    if(request.GET.get('ListPrice')=='HTL'):
        cursor.execute("Select * from product_details where product_category_Id=14 order by product_cost Desc")
        product_details=cursor.fetchall()
        conn.commit()
    elif(request.GET.get('ListPrice')=='LTH'):
        cursor.execute("Select * from product_details where product_category_Id=14 order by product_cost")
        product_details=cursor.fetchall()
        conn.commit()
    else:
        cursor.execute("Select * from product_details where product_category_Id=14")
        product_details=cursor.fetchall()
        conn.commit()

    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return render(request,'Women_items/womenperfumecollection/womenperfumecollection.html',{'result':result,'product_details':product_details,'person_category_id':2,'C_ID':C_ID,'no_of_items':no_of_items[0][0]})
def Cartforecommerce(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from Order_details where C_ID=(?)",C_ID)
    order_details=cursor.fetchall()
    cursor.execute("Select sum(no_of_items),sum(order_product_cost) from Order_details where C_ID=(?)",C_ID)
    items_nd_cost=cursor.fetchall()
    return render(request,'Cartforecommerce.html',{'order_details':order_details,'items':items_nd_cost[0][0],'total_cost':items_nd_cost[0][1],'C_ID':C_ID})
def checkoutpageforecommerce(request):
    C_ID=request.GET.get('C_ID')
    cursor.execute("Select * from Order_details where C_ID=(?)",C_ID)
    order_details=cursor.fetchall()
    cursor.execute("Select sum(no_of_items),sum(order_product_cost) from Order_details where C_ID=(?)",C_ID)
    items_nd_cost=cursor.fetchall()
    return render(request,'checkoutpageforecommerce.html',{'order_details':order_details,'items':items_nd_cost[0][0],'total_cost':items_nd_cost[0][1],'C_ID':C_ID})
def addtocartajaxrequest(request):
    Product_Id=request.POST.get('Product_Id')
    if(request.POST.get('C_ID')!='None'):
        C_ID=request.POST.get('C_ID')
        cursor.execute("Select * from Order_details where product_Id=(?) and C_ID=(?)",Product_Id,C_ID)
        result=cursor.fetchall()
            #return HttpResponse(result)
        if(len(result)==0):
            cursor.execute("Select * from product_details where product_Id=(?)",Product_Id)
            product_details=cursor.fetchall()
            cursor.execute("insert into Order_details values(?,?,?,?,?,?)",C_ID,Product_Id,product_details[0][3],product_details[0][4],1,product_details[0][5])
            conn.commit()
        else:
            cursor.execute("Select no_of_items from Order_details where product_Id=(?) and C_ID=(?)",Product_Id,C_ID)
            res=cursor.fetchall()
            cursor.execute("Update Order_details set no_of_items=(?) where product_Id=(?) and C_ID=(?)",res[0][0]+1,Product_Id,C_ID)
            conn.commit()
        cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
        no_of_items=cursor.fetchall()
        return HttpResponse(no_of_items[0][0])
    else:
        return HttpResponse("No")
def downitembyajaxrequest(request):
    Product_Id=request.POST.get('Product_Id')
    C_ID=request.POST.get('C_ID')
    cursor.execute("Select no_of_items from Order_details where product_Id=(?) and C_ID=(?)",Product_Id,C_ID)
    res=cursor.fetchall()
    if((res[0][0]-1)==0):
        cursor.execute("delete from Order_details where product_Id=(?) and C_ID=(?)",Product_Id,C_ID)
        conn.commit()
    else:
        cursor.execute("Update Order_details set no_of_items=(?) where product_Id=(?) and C_ID=(?)",res[0][0]-1,Product_Id,C_ID)
        conn.commit()
    cursor.execute("select sum(no_of_items) from Order_details where C_ID=(?)",C_ID)
    no_of_items=cursor.fetchall()
    return HttpResponse(no_of_items[0][0])
def checkoutshippinginformation(request):
    C_ID=request.POST.get('C_ID')
    cust_adress=request.POST.get('cust_adress')
    cust_city=request.POST.get('cust_city')
    cust_state=request.POST.get('cust_state')
    cust_zipcode1=request.POST.get('cust_zipcode1')
    cus_zipcode2=request.POST.get('cus_zipcode2')
    cursor.execute('insert into shippinginformation values(?,?,?,?,?,?)',C_ID,cust_adress,cust_city,cust_state,cust_zipcode1,cus_zipcode2)
    conn.commit()
    return HttpResponse("Done")
