from django.db.models import Q

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
from .models import Product

from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):

    products = (
        Product.objects
        .filter(is_active=True)
        .order_by("order")[:6]
    )

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            contact = form.save()

            try:

                send_mail(

                    subject=f"Yangi murojaat: {contact.subject}",

                    message=f"""
Ism: {contact.name}

Email: {contact.email}

Telefon: {contact.phone}

Mavzu: {contact.subject}

Xabar:

{contact.message}
""",

                    from_email=settings.DEFAULT_FROM_EMAIL,

                    recipient_list=[
                        settings.DEFAULT_FROM_EMAIL
                    ],

                    fail_silently=True,

                )

            except Exception:
                pass

            messages.success(
                request,
                "Xabaringiz muvaffaqiyatli yuborildi. Tez orada siz bilan bog'lanamiz."
            )

            form = ContactForm()

    else:

        form = ContactForm()

    context = {

        "products": products,

        "form": form,

    }

    return render(request, "home.html", context)


def products(request):

    search = request.GET.get("q", "")

    products = Product.objects.filter(
        is_active=True
    )

    if search:

        products = products.filter(

            Q(name__icontains=search) |
            Q(short_description__icontains=search) |
            Q(description__icontains=search)

        )

    products = products.order_by("order", "name")

    context = {

        "products": products,
        "search": search,

    }

    return render(request, "products.html", context)


def product_detail(request, slug):
    """Mahsulot sahifasi"""

    product = get_object_or_404(
        Product,
        slug=slug,
        is_active=True,
    )

    related_products = (
        Product.objects
        .filter(
            category=product.category,
            is_active=True,
        )
        .exclude(id=product.id)[:3]
    )

    context = {
        "product": product,
        "related_products": related_products,
    }

    return render(request, "product_detail.html", context)