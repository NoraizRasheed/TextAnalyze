from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def analyzed(request):
    #get the text
    pgtext=request.POST.get('text','default')
    #check checkbox value
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('lineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcounter = request.POST.get('charcounter','off')

    #check which box is on
    if removepunc=='on':
        punctuatuion = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyze =''
        for char in pgtext: 
            if char not in punctuatuion:
                analyze = analyze + char
        dict={'analyzetext':analyze,'purpose':'remove punctuations.'}
        pgtext = analyze
        #return render(request,'analyzed.html',dict)

    if(fullcaps =='on'):
        analyze =""
        for char in pgtext:
            analyze = analyze + char.upper()
        dict={'analyzetext':analyze,'purpose':'change to uppercase.'}
        pgtext = analyze
        #return render(request,'analyzed.html',dict)

    if(newlineremover =='on'):
        analyze=""
        for char in pgtext:
            if char !="\n" and char !="\r":
                analyze = analyze + char
        dict={'analyzetext':analyze,'purpose':'remove new line.'}
        pgtext = analyze
        #return render(request,'analyzed.html',dict)

    if(extraspaceremover == 'on'):
        analyze=""
        for index, char in enumerate(pgtext):
            if not(pgtext[index] ==' ' and pgtext[index+1] ==" "):
                analyze = analyze + char
        dict={'analyzetext':analyze,'purpose':'remove extra space.'}
        pgtext = analyze
        #return render(request,'analyzed.html',dict)

    if(charcounter =='on'):
        analyze = ""
        for char in pgtext:
            analyze = analyze + char#(pgtext.count(char))

        dict={'analyzetext':len(analyze),'purpose':'count characters.'}
        pgtext = len(analyze)
        #return render(request,'analyzed.html',dict)

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcounter!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request,'analyzed.html',dict)
