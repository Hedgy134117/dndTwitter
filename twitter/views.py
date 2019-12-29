from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms

# Create your views here.
def tweetList(request):
    tweets = models.Tweet.objects.all()
    return render(request, 'tweetList.html', { 'tweets': tweets })

def tweetDetail(request, id):
    tweet = models.Tweet.objects.get(id=id)
    try:
        comments = models.Comment.objects.filter(tweet=tweet)
    except:
        comments = None
    return render(request, 'tweetDetail.html', { 'tweet': tweet, 'comments': comments })

def createTweet(request):
    if request.method == 'POST':
        form = forms.CreateTweet(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('list')
    else:
        form = forms.CreateTweet()
    return render(request, 'createTweet.html', { 'form': form })

def addComment(request, id):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.tweet = models.Tweet.objects.get(id=id)
            instance.save()
            return redirect('twitter:detail', id=id)
    else:
        form = forms.CreateComment()
    return render(request, 'addComment.html', { 'form': form, 'id': id })
    