# from django.http.response import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def count(request):
    user_text = request.GET['textarea']
    total_count = len(user_text)

    word_dict = {}

    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    # 字典本身不是可迭代对象，用items将他变成可迭代对对象
    sorted_dict = sorted(word_dict.items(), key=lambda w: w[1], reverse=True)

    return render(request, 'count.html',
                  {'count': total_count, 'text': user_text,
                   'dict': word_dict, 'sorted': sorted_dict})

