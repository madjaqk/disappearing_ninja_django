from django.shortcuts import render
from django.http import HttpResponse

def index(request, data=None):
    turtles = {"red": "ninjas/raphael.jpg",
               "blue": "ninjas/leonardo.jpg",
               "orange": "ninjas/michelangelo.jpg",
               "purple": "ninjas/donatello.jpg",
               }
    if data:
        try:
            context = {"images": [turtles[data]]}
        except:
            context = {"images": ["ninjas/notapril.jpg"]}
    else:
        srcs = []
        for turtle in turtles:
            srcs.append(turtles[turtle])
        context = {"images": srcs}
    return render(request, "ninjas/index.html", context)
"""
def test(request, data):
    print("test")
    print(data)

    return render(request, "ninjas/index.html", context)
"""
