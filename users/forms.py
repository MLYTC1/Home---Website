from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username','password']
        
    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = User 
        fields = (
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
            )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()

    # class UserProfileView(LoginRequiredMixin, CacheMixin , UpdateView):
    # template_name = 'users/profile.html'
    # form_class = ProfileForm
    # success_url = reverse_lazy('users:profile')

    # def get_object(self, queryset=None):
    #     return self.request.user

    # def form_valid(self, form):
    #     messages.success(self.request, "Профайл успешно обновлен")
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     messages.error(self.request, "Произошла ошибка")
    #     return super().form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Home - Кабинет'

    #     # Можно вынести сам запрос в отдельный метод этого класса контроллера
    #     orders = Order.objects.filter(user=self.request.user).prefetch_related(
    #             Prefetch(
    #                 "orderitem_set",
    #                 queryset=OrderItem.objects.select_related("product"),
    #             )
    #         ).order_by("-id")

    #     context['orders'] = self.set_get_cache(orders, f"user_{self.request.user.id}_orders", 60)
    #     return context

    # username = forms.CharField(
    #     label='Name',
    #     widget=forms.TextInput(attrs={  "autofocus": True,
    #                                     'class': 'form-control',
    #                                     'placeholder': "Input Username"}))
    # password = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput(attrs={  "autocomplete": "current-password",
    #                                         'class': 'form-control',
    #                                         'placeholder': "Input Password"}))
