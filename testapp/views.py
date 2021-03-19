from django.shortcuts import render,redirect
from . models import AddBook
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'testapp/index.html')

def add(request):
    msg=""
    if request.method=='POST':
        bookid=request.POST.get('bookid')
        booktitle=request.POST.get('booktitle')
        bookauth=request.POST.get('bookauth')
        bookaval=request.POST.get('bookaval')
        books_list=AddBook(bookid=bookid,booktitle=booktitle,bookauth=bookauth,bookaval=bookaval)
        books_list.save()
        msg="book added sucesfully"
        return render(request,'testapp/add.html',{'msg':msg})
    else:
        
        return render(request,'testapp/add.html')

def view(request):
    books=AddBook.objects.all()
    return render(request,'testapp/view.html',{'books':books})


def delet(request):
    msg=""
    if request.method=='POST':
        bookid_delete=request.POST.get('bookid_delete')
        books=AddBook.objects.filter(bookid=bookid_delete)
        for book in books:
            newbookid = book.bookid
            if newbookid == bookid_delete:
                msg="no record found"
            else:
                books.delete()
                msg="book deleted sucesfully"
                return render(request,'testapp/delet.html',{'msg':msg})
        msg="no record found"
        return render(request,'testapp/delet.html',{'msg':msg})
        
    return render(request,'testapp/delet.html',{'msg':msg})

def issue(request):
    msg=""
    if request.method=='POST':
        bookaval="Issued"
        bookid_issue = request.POST.get('bookid')
        books=AddBook.objects.filter(bookid=bookid_issue)
        for book in books:
            newbookid = book.bookid
            if newbookid==bookid_issue:
                msg="no record found"
                return render(request,'testapp/issue.html',{'msg':msg})
            else:
                books.update(bookaval=bookaval)
                msg="book issued sucesfully"
                return render(request,'testapp/issue.html',{'msg':msg})
            msg="no record found"
            return render(request,'testapp/issue.html',{'msg':msg})
        msg="no record found"
        return render(request,'testapp/issue.html',{'msg':msg})
    return render(request,'testapp/issue.html')

def returnbook(request):
    msg=""
    if request.method=='POST':
        bookaval="available"
        bookid_return = request.POST.get('bookid')
        books=AddBook.objects.filter(bookid=bookid_return)
        for book in books:
            newbookid = book.bookid
            if newbookid==bookid_return:
                msg="no record found"
                return render(request,'testapp/return.html',{'msg':msg})
            else:
                books.update(bookaval=bookaval)
                msg="book returned sucesfully"
                return render(request,'testapp/return.html',{'msg':msg})
            msg="no record found"
            return render(request,'testapp/issue.html',{'msg':msg})
        msg="no record found"
        return render(request,'testapp/issue.html',{'msg':msg})
    return render(request,'testapp/return.html')

