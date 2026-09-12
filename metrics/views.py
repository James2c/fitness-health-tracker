from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import WeightEntryForm
from .models import WeightEntry


@login_required
def weight_list(request):

    entries = WeightEntry.objects.filter(
        user=request.user
    )

    return render(
        request,
        "metrics/weight_list.html",
        {
            "entries": entries,
        },
    )


@login_required
def weight_create(request):

    if request.method == "POST":

        form = WeightEntryForm(request.POST)
        form.user = request.user

        if form.is_valid():

            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            return redirect("weight_list")

    else:

        form = WeightEntryForm()

    return render(
        request,
        "metrics/weight_form.html",
        {
            "form": form,
        },
    )


@login_required
def weight_edit(request, entry_id):

    entry = get_object_or_404(
        WeightEntry,
        id=entry_id,
        user=request.user,
    )

    if request.method == "POST":

        form = WeightEntryForm(
            request.POST,
            instance=entry,
        )

        form.user = request.user

        if form.is_valid():
            form.save()

            return redirect("weight_list")

    else:

        form = WeightEntryForm(
            instance=entry,
        )

    return render(
        request,
        "metrics/weight_form.html",
        {
            "form": form,
            "entry": entry,
        },
    )


@login_required
def weight_delete(request, entry_id):

    entry = get_object_or_404(
        WeightEntry,
        id=entry_id,
        user=request.user,
    )

    if request.method == "POST":
        entry.delete()

        return redirect("weight_list")

    return render(
        request,
        "metrics/weight_confirm_delete.html",
        {
            "entry": entry,
        },
    )