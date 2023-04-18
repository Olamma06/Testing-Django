from django.shortcuts import render

from django.http import HttpResponse, request 

# Create your views here.

def Attire(request):
    return render(request,'plug.html', {
        "blog":[
            {"title":"NATIVE ATTIRE",
            "body":"Your best plug",
            "price":5.0,
            "color":"Red",
            "date":"1-03-2021",
            "image": 'red.png'
            },

            {"title":"COOPERATE WEAR",
            "body":"Your best plug",
            "price":3.5,
            "color":"Cream",
            "date":"4-03-2021",
            "image": "cooperate.jpg"
            },

            {"title":"CASUAL WEAR",
            "body":"Your best plug",
            "color":"White & blue",
            "price":1.6,
            "date":"7-03-2021",
            "image":"casual.jpg"
            },

            {"title":"NATIVE ATTIRE",
            "body":"Your best plug",
            "price":5.0,
            "color":"Red",
            "date":"1-03-2021",
            "image": 'red.png'
            },

            {"title":"COOPERATE WEAR",
            "body":"Your best plug",
            "price":3.5,
            "color":"Cream",
            "date":"4-03-2021",
            "image": "cooperate.jpg"
            },

            {"title":"CASUAL WEAR",
            "body":"Your best plug",
            "color":"White & blue",
            "price":1.6,
            "date":"7-03-2021",
            "image":"casual.jpg"
            },

        ]
    })


