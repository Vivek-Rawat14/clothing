from django.urls import path
from django.shortcuts import render,redirect
import json
from .models import clothes,users
# View functions
def homepage(req):
    if not req.session['user']:
        redirect("/login")
    db = clothes.objects.filter(clothescat='shirtm').values()
    cd = list(db)
    bb = clothes.objects.filter(clothescat='printtshirtw').values()
    cc = list(bb)
    dd = clothes.objects.filter(clothescat='rings').values()
    vd = list(dd)
    b = clothes.objects.filter(clothescat='bags').values()
    d = list(b)
    return render(req, 'index.html',context={'data':cd,'wtsh':cc,'watch':vd,'bags':d})

def mencollection(req):
    return render(req, 'mencollection.html')


def womencollection(req):
    return render(req, 'womencollection.html')


def accessories(req):
    return render(req, 'accessoires.html')

def tshirt(req):
    db = clothes.objects.filter(clothescat='printtshirtm').values()
    cd = list(db)
    return render(req, 'tshirt.html',context={'data':cd})

def shirtm(req):
    db = clothes.objects.filter(clothescat='shirtm').values()
    cd = list(db)
    return render(req, 'shirtm.html',context={'data':cd})


def full(req):
    db = clothes.objects.filter(clothescat='fullm').values()
    cd = list(db)
    return render(req, 'full.html',context={'data':cd})

def jeansm(req):
    db = clothes.objects.filter(clothescat='jeansm').values()
    cd = list(db)
    return render(req, 'jeansm.html',context={'data':cd})

def cargom(req):
    db = clothes.objects.filter(clothescat='cargom').values()
    cd = list(db)
    return render(req, 'cargom.html',context={'data':cd})

def baggym(req):
    db = clothes.objects.filter(clothescat='baggym').values()
    cd = list(db)
    return render(req, 'baggym.html',context={'data':cd})

def printtshirtw(req):
    db = clothes.objects.filter(clothescat='printtshirtw').values()
    cd = list(db)
    return render(req, 'printtshirtw.html',context={'data':cd})

def hoodies(req):
    db = clothes.objects.filter(clothescat='hoodies').values()
    cd = list(db)
    return render(req, 'hoodies.html',context={'data':cd})

def shirtw(req):
    db = clothes.objects.filter(clothescat='shirtw').values()
    cd = list(db)
    return render(req, 'shirtw.html',context={'data':cd})

def kurta(req):
    db = clothes.objects.filter(clothescat='kurta').values()
    cd = list(db)
    return render(req, 'kurta.html',context={'data':cd})

def cargow(req):
    db = clothes.objects.filter(clothescat='cargow').values()
    cd = list(db)
    return render(req, 'cargow.html',context={'data':cd})

def sareew(req):
    db = clothes.objects.filter(clothescat='sareesw').values()
    cd = list(db)
    return render(req, 'sareew.html', context={'data': cd})

def braclets(req):
    db = clothes.objects.filter(clothescat='braclets').values()
    cd = list(db)
    return render(req, 'braclets.html',context={'data':cd})

def necklace(req):
    db = clothes.objects.filter(clothescat='necklace').values()
    cd = list(db)
    return render(req, 'necklace.html', context={'data': cd})

def caps(req):
    db = clothes.objects.filter(clothescat='caps').values()
    cd = list(db)
    return render(req, 'caps.html', context={'data': cd})

def rings(req):
    db = clothes.objects.filter(clothescat='rings').values()
    cd = list(db)
    return render(req, 'rings.html', context={'data': cd})

def sunglasses(req):
    db = clothes.objects.filter(clothescat='sunglasses').values()
    cd = list(db)
    return render(req, 'sunglasses.html', context={'data': cd})

def bags(req):
    db = clothes.objects.filter(clothescat='bags').values()
    cd = list(db)
    return render(req, 'bags.html', context={'data': cd})

def watchm(req):
    db = clothes.objects.filter(clothescat='watchm').values()
    cd = list(db)
    return render(req, 'watchm.html', context={'data': cd})

def watchw(req):
    db = clothes.objects.filter(clothescat='watchw').values()
    cd = list(db)
    return render(req, 'watchw.html', context={'data': cd})

def shoes(req):
    db = clothes.objects.filter(clothescat='shoes').values()
    cd = list(db)
    return render(req, 'shoes.html', context={'data': cd})

def shoesw(req):
    db = clothes.objects.filter(clothescat='shoesw').values()
    cd = list(db)
    return render(req, 'shoesw.html', context={'data': cd})

def shoescoll(req):
    return render(req,'shoescoll.html')

def watchcoll(req):
    return render(req,'watchcoll.html')

def productshow(req,Id):
    db = clothes.objects.filter(id=Id).values()
    cd = list(db)
    return render(req,'productshow.html',context={'data':cd})

def productshoes(req,Id):
    db = clothes.objects.filter(id=Id).values()
    cd = list(db)
    return render(req,'productshoes.html',context={'data':cd})

def product(req,Id):
    db = clothes.objects.filter(id=Id).values()
    cd = list(db)
    return render(req,'product.html',context={'data':cd})

def login(req):
    req.session.set_test_cookie()

    if req.method == 'POST':
        phonenumber = req.POST['phone']
        passwordl = req.POST['password']
        try:
            s =users.objects.get(phone = phonenumber,password = passwordl)
            if(s):
                req.session['user'] = json.loads(s)
                return redirect('/')
        except Exception as e:
            return render(req, 'login.html', context={"error": "Something went wrong, try again"})
    return render(req, 'login.html')

def signup(req):
    if req.method=='POST':
        name = req.POST['name']
        email = req.POST['email']
        password = req.POST['password']
        repassword = req.POST['re_password']
        state = req.POST['state']
        city = req.POST['city']
        pincode = req.POST['pincode']
        address = req.POST['address']
        phone  = req.POST['phone']

        users.objects.create(username = name,password=password,email=email,phone =phone,address= address,city=city,pincode=pincode,state=state,repassword=repassword  )
        return redirect('/login')
    
    return render(req,'signup.html')

def userss(req):
    db  = users.objects.all()
    cd = list(db)
    return render(req,'users.html',context={"userde":db})

def logout(req):
    return redirect('/login')

def carts(req):
    return render(req,'carts.html')

def like(req):
    return render(req,'like.html')