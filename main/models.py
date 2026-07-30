from django.db import models
from django.urls import reverse


class Product(models.Model):

    CATEGORY_CHOICES = [
        ("cellulose", "Sellyuloza efiri"),
        ("polymer", "Polimer qo'shimchalari"),
        ("titanium", "Titanium dioksid"),
        ("chemical", "Kimyoviy qo'shimchalar"),
        ("mineral", "Mineral to'ldirgichlar"),
    ]

    name = models.CharField(
        "Mahsulot nomi",
        max_length=200
    )

    slug = models.SlugField(
        "Slug",
        max_length=220,
        unique=True
    )

    category = models.CharField(
        "Kategoriya",
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    short_description = models.CharField(
        "Qisqa tavsif",
        max_length=250
    )

    description = models.TextField(
        "To'liq tavsif"
    )

    image = models.ImageField(
        "Asosiy rasm",
        upload_to="products/",
        blank=False,
        null=False
    )

    is_featured = models.BooleanField(
        "Asosiy mahsulot",
        default=False
    )

    is_active = models.BooleanField(
        "Faol",
        default=True
    )

    order = models.PositiveIntegerField(
        "Tartib",
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name = "Mahsulot"

        verbose_name_plural = "Mahsulotlar"

        ordering = ["order", "name"]

        indexes = [

            models.Index(fields=["slug"]),

            models.Index(fields=["category"]),

            models.Index(fields=["is_active"]),

            models.Index(fields=["is_featured"]),

        ]

    def __str__(self):

        return self.name

    def get_absolute_url(self):

        return reverse(

            "main:product_detail",

            kwargs={

                "slug": self.slug

            }

        )
    class Contact(models.Model):

    name = models.CharField(
        "Ism",
        max_length=100
    )

    email = models.EmailField(
        "Email"
    )

    phone = models.CharField(
        "Telefon",
        max_length=20,
        blank=True
    )

    subject = models.CharField(
        "Mavzu",
        max_length=200,
        blank=True
    )

    message = models.TextField(
        "Xabar"
    )

    is_read = models.BooleanField(
        "O'qilgan",
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        verbose_name = "Xabar"

        verbose_name_plural = "Xabarlar"

        ordering = ["-created_at"]

        indexes = [

            models.Index(fields=["is_read"]),

            models.Index(fields=["created_at"]),

        ]

    def __str__(self):

        return f"{self.name} - {self.email}"
    