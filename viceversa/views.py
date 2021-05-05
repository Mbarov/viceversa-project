from django.shortcuts import render

def home(request):
    return render(request, 'home.html')



def reverse(request):
    user_text= request.GET['usertext']
    reversed_text= user_text[::-1]
    kvo=user_text.split()
    kvo2=len(kvo)
    return render(request,'reverse.html', {'usertext':user_text, 'reverse':reversed_text,'kvo':kvo2})