from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    print(request)
    text = request.GET['fulltext']
    textcount = len(text)
    splitted_text = text.split()
    wordcount={char: 0 for char in splitted_text}
    for word in splitted_text:
        wordcount[word] += 1
      
    textcount = sum(wordcount.values())
    return render(request, 'result.html', {
        'text':text,
        'textcount':textcount,
        'wordcount':wordcount,
        'totaltext':text,
    })