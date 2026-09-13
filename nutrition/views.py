from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum
from django.utils import timezone

from datetime import date

from .forms import NutritionEntryForm
from .models import NutritionEntry


@login_required
def nutrition_list(request):
    entries = NutritionEntry.objects.filter(
        user=request.user
    )

    today = timezone.localdate()

    today_entries = entries.filter(date=today)

    daily_total = (
        entries
        .filter(date=today)
        .aggregate(
            total_calories=Sum("calories"),
            total_protein=Sum("protein"),
            total_carbohydrates=Sum("carbohydrates"),
            total_fat=Sum("fat"),
        )
    )

    history_entries = entries.exclude(date=today)

    history_date = request.GET.get("history_date")

    if history_date:
        try:
            selected_date = date.fromisoformat(history_date)
            history_entries = history_entries.filter(
                date=selected_date
            )
        except ValueError:
            selected_date = None
    else:
        selected_date = None

    return render(
        request,
        "nutrition/nutrition_list.html",
        {
            "entries": entries,
            "today_entries": today_entries,
            "history_entries": history_entries,
            "daily_total": daily_total,
            "today": today,
            "selected_date": selected_date,
        },
    )


@login_required
def nutrition_create(request):
    if request.method == "POST":
        form = NutritionEntryForm(request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            return redirect("nutrition_list")

    else:
        form = NutritionEntryForm()

    return render(
        request,
        "nutrition/nutrition_form.html",
        {"form": form},
    )


@login_required
def nutrition_edit(request, entry_id):
    entry = get_object_or_404(
        NutritionEntry,
        id=entry_id,
        user=request.user,
    )

    if request.method == "POST":
        form = NutritionEntryForm(
            request.POST,
            instance=entry,
        )

        if form.is_valid():
            form.save()

            return redirect("nutrition_list")

    else:
        form = NutritionEntryForm(instance=entry)

    return render(
        request,
        "nutrition/nutrition_form.html",
        {
            "form": form,
            "entry": entry,
        },
    )


@login_required
def nutrition_delete(request, entry_id):
    entry = get_object_or_404(
        NutritionEntry,
        id=entry_id,
        user=request.user,
    )

    if request.method == "POST":
        entry.delete()

        return redirect("nutrition_list")

    return render(
        request,
        "nutrition/nutrition_confirm_delete.html",
        {"entry": entry},
    )