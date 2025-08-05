from django.views.generic import CreateView, DetailView, ListView
from .models import Post
from .mixins import StaffRequiredMixin, SaveAuthorMixin, SuccessMessageMixin

class PostCreateView(SaveAuthorMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.htm'
    success_url = '/'
    success_message = "Пост успішно створено."

class PostDetailView(StaffRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.htm'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.htm'
