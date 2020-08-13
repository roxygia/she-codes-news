from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Category
from .forms import StoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'news/categoryList.html'

    def get_queryset(self):
        '''Return all categories.'''
        return Category.objects.all()

class CategoryStoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/categoryStories.html'
    slug_field = 'category'

    context_object_name = "stories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stories'] = NewsStory.objects.filter(category__title=self.kwargs.get('slug'))
        return context

class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
