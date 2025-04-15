from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import MessageForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from .models import ChatRoom, Message
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'chat/home.html')

def about(request):
    return render(request, 'chat/about.html')

def login_view(request):
    return render(request, 'chat/login.html')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'chat/register.html'
    success_url = reverse_lazy('login')  
    
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/profile.html'

class RoomListView(ListView):
    model = ChatRoom
    template_name = 'chat/room_list.html'
    context_object_name = 'rooms'

class RoomDetailView(DetailView):
    model = ChatRoom
    template_name = 'chat/room_detail.html'
    context_object_name = 'room'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = self.object
            message.user = request.user if request.user.is_authenticated else None
            message.save()
            return redirect('room-detail', slug=self.object.slug)
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

    
class RoomCreateView(LoginRequiredMixin, CreateView):
    model = ChatRoom
    fields = ['name', 'slug']
    template_name = 'chat/room_form.html'
    success_url = reverse_lazy('room-list')
