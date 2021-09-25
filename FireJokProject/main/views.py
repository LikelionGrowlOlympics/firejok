from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def getCarPrice(car):
    car_category={"BMW":7000, "BENZ":7000, "AUDI":10000, "TES":15000,
      " RAM":25000, "FERA":27000}
    
    return car_category[car]

def getAreaPrice(area):
    Area_category={"INCEON":36000, "KANGONE":20000, "SEJONG":55000, "BUSAN":33000,
      "KYEONPOOK":17000, "CHOONGNAM":22000, "DAEJEON":31000, "CHOONGPOOK":19000
      ,"JEONPOOK":20000, "JEONNAM":19000, "DAEGU":39000, "ULSAN":31000, "GWANGJU":31000}
    
    return Area_category[area]


def calcDday (request):
    month_pay= request.POST['salary']
    month_spend= request.POST['month_spend']
    car=request.POST['car']
    area=request.POST['area']
    goal= request.POST['goal']
    car_price=getCarPrice(car)
    area_price=getAreaPrice(area)
    total_price= car_price+area_price+goal
    leftMonth= total_price//(month_pay-month_spend)
    return render(request, 'result.html',{'leftMonth':leftMonth})

    
