from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum
from django.utils import timezone
from django.core.paginator import Paginator

from datetime import date
from decimal import Decimal

from .forms import NutritionEntryForm, NutritionGoalForm
from .models import NutritionEntry, NutritionGoal



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

    nutrition_goal = NutritionGoal.objects.filter(
        user=request.user
    ).first()

    goal_percentages = {}

    if nutrition_goal:
        goal_percentages = {
            "calories": min(
                (
                    Decimal(daily_total["total_calories"] or 0)
                    / Decimal(nutrition_goal.daily_calories)
                ) * 100,
                Decimal("100"),
            ),
            "protein": min(
                (
                    Decimal(daily_total["total_protein"] or 0)
                    / nutrition_goal.daily_protein
                ) * 100,
                Decimal("100"),
            ),
            "carbohydrates": min(
                (
                    Decimal(daily_total["total_carbohydrates"] or 0)
                    / nutrition_goal.daily_carbohydrates
                ) * 100,
                Decimal("100"),
            ),
            "fat": min(
                (
                    Decimal(daily_total["total_fat"] or 0)
                    / nutrition_goal.daily_fat
                ) * 100,
                Decimal("100"),
            ),
        }

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

    paginator = Paginator(history_entries, 10)

    page_number = request.GET.get("page")

    history_entries = paginator.get_page(page_number)

    return render(
        request,
        "nutrition/nutrition_list.html",
        {
            "entries": entries,
            "today_entries": today_entries,
            "history_entries": history_entries,
            "daily_total": daily_total,
            "nutrition_goal": nutrition_goal,
            "goal_percentages": goal_percentages,
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


@login_required
def nutrition_goals(request):
    goal, created = NutritionGoal.objects.get_or_create(
        user=request.user,
        defaults={
            "daily_calories": 2000,
            "daily_protein": 150,
            "daily_carbohydrates": 250,
            "daily_fat": 65,
        },
    )

    if request.method == "POST":
        form = NutritionGoalForm(
            request.POST,
            instance=goal,
        )

        if form.is_valid():
            form.save()
            return redirect("nutrition_goals")

    else:
        form = NutritionGoalForm(instance=goal)

    return render(
        request,
        "nutrition/nutrition_goals.html",
        {
            "form": form,
        },
    )