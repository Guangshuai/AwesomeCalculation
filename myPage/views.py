import csv

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render, redirect

from myService.LinearRegression import handle_uploaded_file_for_lr
from .forms import BookForm, UploadFileForm
from .models import Book


def home(request):
    return render(request, 'home.html')


def linear_regression_upload(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid() and request.FILES['lr_data_file'].name.endswith('.csv'):
            uploaded_file = request.FILES['lr_data_file']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            first_line = str(uploaded_file.readline(), 'utf-8').split(',')
            context['url'] = fs.url(name)
            context['name'] = name
            context['y_data'] = [first_line[1]]
            context['weight'] = [first_line[2]]
            context['x_data'] = first_line[3:]
    return render(request, "lr_upload.html", context)


def linear_regression_calculate(request):
    if request.is_ajax() and request.method == 'POST':
        x_data_col = request.POST['x_data']
        y_data_col = request.POST['y_data']
        theta = request.POST['theta']
        file_name = request.POST['file_name']
        f_object = FileSystemStorage().open(file_name)
        print(x_data_col)
        print(y_data_col)
        print(theta)
        handle_uploaded_file_for_lr(f_object, int(x_data_col), int(y_data_col), int(theta))
        context = {'theta': 1}
    return JsonResponse(context)


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, "upload.html", context)


def book_list(request):
    book = Book.objects.all()
    return render(request, 'book_list.html', {'books': book})


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })


# def upload_data(request):
#     return render(request, )

