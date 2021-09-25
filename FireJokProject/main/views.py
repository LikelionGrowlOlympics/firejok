from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def getCarPrice(car):
    car_category={"BMW":70000000, "BENZ":70000000, "AUDI":100000000, "TES":150000000,
      " RAM":250000000, "FERA":270000000}
    
    return car_category[car]

def getAreaPrice(area):
    Area_category={"INCEON":360000000, "KANGONE":200000000, "SEJONG":550000000, "BUSAN":330000000,
      "KYEONPOOK":170000000, "CHOONGNAM":220000000, "DAEJEON":310000000, "CHOONGPOOK":190000000
      ,"JEONPOOK":200000000, "JEONNAM":190000000, "DAEGU":390000000, "ULSAN":310000000, "GWANGJU":310000000}
    
    return Area_category[area]

def calcDday (request):
    month_pay= request.POST['month_pay']
    month_spend= request.POST['month_spend']
    car=request.POST['car']
    area=request.POST['area']
    goal= request.POST['goal']
    
