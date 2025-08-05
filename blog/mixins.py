from django.http import HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import Group

class StaffRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden("Доступ лише для персоналу.")
        return super().dispatch(request, *args, **kwargs)

class AuthorRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            return HttpResponseForbidden("Ви не автор цього об'єкта.")
        return super().dispatch(request, *args, **kwargs)

class SuccessMessageMixin:
    success_message = "Операція виконана успішно!"

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

class RedirectIfAuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class AnonymousRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseForbidden("Сторінка доступна лише для гостей.")
        return super().dispatch(request, *args, **kwargs)

class OnlyGetMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.method != 'GET':
            return HttpResponseForbidden("Дозволено лише GET-запити.")
        return super().dispatch(request, *args, **kwargs)

class SaveAuthorMixin:
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UserOwnsObjectMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

class PageTitleMixin:
    page_title = "Сторінка"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context

class GroupRequiredMixin:
    required_group = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not Group.objects.filter(name=self.required_group, user=request.user).exists():
            return HttpResponseForbidden("Ви не в потрібній групі.")
        return super().dispatch(request, *args, **kwargs)
