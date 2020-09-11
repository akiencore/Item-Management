from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url
from django.conf import settings

from .models import Container, Item
from .forms import ContainerForm, ItemForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)


def container_detail_view(request, container_id, *args, **kwargs):
    data = {
        "id": container_id,
    }
    status = 200

    try:
        obj = Container.objects.get(id=container_id)
        data["id"] = container_id
        data["what"] = "container"
        data["name"] = obj.name
        data["length"] = obj.length
        data["width"] = obj.width
        data["height"] = obj.height
        data["color"] = obj.color
        data["purpose"] = obj.purpose
        data["note"] = obj.note

    except:  # if cannot get the object
        data["message"] = "not found"
        status = 404

    # return JsonResponse(data, status=status)
    return render(request, 'components/detail.html', context={"data": data}, status=status)


def container_list_view(request, *args, **kwargs):
    qs = Container.objects.all()  
    container_list = [
        {"id": x.id, "name": x.name, "color": x.color} for x in qs]
    data = {
        "response": container_list
    }
    return JsonResponse(data)


def container_create_view(request, *args, **kwargs):
    form = ContainerForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = ContainerForm()
    return render(request, 'components/form.html', context={"form": form, "what": "container"})



def item_detail_view(request, item_id, *args, **kwargs):
    data = {
        "id": item_id,
    }
    status = 200

    try:
        obj = Item.objects.get(id=item_id)
        data["id"] = item_id
        data["what"] = "item"
        data["name"] = obj.name
        data["length"] = obj.length
        data["width"] = obj.width
        data["height"] = obj.height
        data["color"] = obj.color
        data["category"] = obj.category
        data["in_container"] = obj.in_container
        data["purpose"] = obj.purpose
        data["note"] = obj.note

    except:  # if cannot get the object
        data["message"] = "not found"
        status = 404

    # return JsonResponse(data, status=status)
    return render(request, 'components/detail.html', context={"data": data}, status=status)


def item_list_view(request, *args, **kwargs):
    qs = Item.objects.all()  
    item_list = [
        {"id": x.id, "name": x.name, "color": x.color, "in_container": x.in_container} for x in qs]
    data = {
        "response": item_list
    }
    return JsonResponse(data)

def item_in_list_view(request, container_id, *args, **kwargs):
    qs = Item.objects.all().filter(in_container = container_id)
    item_list = [
        {"id": x.id, "name": x.name, "color": x.color, "in_container": x.in_container} for x in qs]
    data = {
        "response": item_list
    }
    return JsonResponse(data)

def item_create_view(request, *args, **kwargs):
    form = ItemForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = ItemForm()
    return render(request, 'components/form.html', context={"form": form, "what": "item"})