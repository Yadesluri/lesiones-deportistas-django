from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group


# ============================
# LOGIN
# ============================
def login_view(request):

    # Si ya inició sesión → envía al panel
    if request.user.is_authenticated:
        return redirect('panel')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Bienvenido {user.username}")
            return redirect('panel')  # Panel principal que detecta el rol
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "cuentas/login.html")



# ============================
# REGISTRO
# ============================
def registro(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        grupo = request.POST.get("grupo")  # entrenadores / kinesiologos

        # Validar usuario existente
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe.")
            return redirect("registro")

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Asignación correcta del grupo
        if grupo == "entrenadores":
            user.groups.add(Group.objects.get(name="Entrenadores"))
        elif grupo == "kinesiologos":
            user.groups.add(Group.objects.get(name="Kinesiologos"))
        else:
            messages.error(request, "Debes seleccionar un grupo válido.")
            return redirect("registro")

        user.save()

        messages.success(request, "Usuario registrado correctamente. Ahora puedes iniciar sesión.")
        return redirect("login")

    return render(request, "cuentas/registro.html")



# ============================
# LOGOUT
# ============================
def logout_view(request):
    logout(request)
    messages.info(request, "Sesión cerrada correctamente.")
    return redirect('login')



# ============================
# REDIRECCIÓN CENTRAL SEGÚN ROL
# ============================
@login_required
def login_redirect(request):
    user = request.user

    # Si pertenece al grupo Entrenadores
    if user.groups.filter(name="Entrenadores").exists():
        return redirect('panel_entrenador')

    # Si pertenece al grupo Kinesiologos
    if user.groups.filter(name="Kinesiologos").exists():
        return redirect('panel_kinesio')

    # Si no tiene grupo asignado
    messages.error(request, "Tu usuario no tiene un rol asignado. Contacta al administrador.")
    return redirect('logout')
