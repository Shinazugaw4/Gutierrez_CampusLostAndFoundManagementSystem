from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

from .models import Item, Student, Claim


def home(request):
    message = ""

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "report":
            name = request.POST.get("name")
            description = request.POST.get("description")
            location = request.POST.get("location")

            Item.objects.create(
                name=name,
                description=description,
                location=location
            )

            message = "Item reported successfully"

        elif form_type == "claim":
            item_id = request.POST.get("item_id")
            student_id = request.POST.get("student_id")

            item = Item.objects.get(id=item_id)
            student = Student.objects.get(id=student_id)

            Claim.objects.create(item=item, student=student)

            item.status = "Claimed"
            item.save()

            message = "Claim request submitted successfully"

    items = Item.objects.exclude(status="Claimed")

    return render(request, "index.html", {
        "message": message,
        "items": items
    })


@csrf_exempt
def report_item(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Item.objects.create(
            name=data["name"],
            description=data["description"],
            location=data["location"]
        )

        return JsonResponse({"message": "Item reported successfully"})


def view_items(request):
    items = list(Item.objects.exclude(status="Claimed").values())
    return JsonResponse(items, safe=False)


@csrf_exempt
def claim_item(request):
    if request.method == "POST":
        data = json.loads(request.body)

        item = Item.objects.get(id=data["item_id"])
        student = Student.objects.get(id=data["student_id"])

        Claim.objects.create(item=item, student=student)

        item.status = "Claimed"
        item.save()

        return JsonResponse({"message": "Claim request submitted"})