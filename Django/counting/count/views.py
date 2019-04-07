from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    print(request)
    text = request.GET['fulltext']
    # textcount = len(text) 
    splitted_text = text.split(' ')
    wordcount = len(splitted_text)
    each_word_count = {}
    for i in splitted_text:
        try: each_word_count[i] += 1
        except: each_word_count[i] = 1
    
    return render(request, 'result.html', {
        'text' : text,
        # 'textcount' : textcount,
        # 'text2count' : text2count,
        'wordcount' : wordcount,
        'each_word_count' : each_word_count,
    })