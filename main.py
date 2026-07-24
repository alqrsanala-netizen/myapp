
import flet as ft
import requests
import socket
import os

def main(page: ft.Page):
    page.title = "علاء المنشدي - Cyber Dashboard"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.scroll = "auto"

    result_text = ft.Text(
        value="الحالة: مستعد للعمل ونظيف بالكامل...", 
        size=14, 
        color="white", 
        text_align=ft.TextAlign.CENTER
    )

    def check_url(e):
        target = url_entry.value
        if not target:
            result_text.value = "⚠️ الرجاء إدخال رابط أولاً!"
            page.update()
            return
        if not target.startswith("http"): target = "https://" + target
        try:
            response = requests.get(target, timeout=5)
            result_text.value = f"✅ الحالة: {response.status_code}"
            result_text.color = "green"
        except:
            result_text.value = "❌ فشل الاتصال!"
            result_text.color = "red"
        page.update()

    def get_local_ip(e):
        try:
            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            result_text.value = f"🌐 IP: {local_ip}"
            result_text.color = "green"
        except:
            result_text.value = "❌ خطأ في جلب IP"
        page.update()

    url_entry = ft.TextField(hint_text="أدخل رابط الموقع المطلوب فحص حالته...", width=340, color="white")

    base_path = os.path.dirname(os.path.abspath(__file__))
    my_photo_path = os.path.join(base_path, "assets", "background.jpg")
    kali_logo_path = os.path.join(base_path, "assets", "kali_logo.png")

    # جلب الصور أو أيقونات احتياطية نصية مستقرة
    my_photo = ft.Image(src=my_photo_path, width=110, height=110, border_radius=55) if os.path.exists(my_photo_path) else ft.Icon(name="person", size=100, color="blue")
    kali_logo = ft.Image(src=kali_logo_path, width=50, height=50) if os.path.exists(kali_logo_path) else ft.Icon(name="shield", size=40, color="green")

    page.add(
        # عرض الشعار والصورة بجانب بعض بشكل متناسق مع مسافة عرضية (width)
        ft.Row(
            alignment="center", 
            controls=[
                kali_logo, 
                ft.Container(width=15), # مسافة أمان عرضية صحيحة
                my_photo
            ]
        ),
        ft.Container(height=15), # مسافة رأسية آمنة ومستقرة بدلاً من الفاصل الرأسي المخالف
        ft.Text("علاء المنشدي", size=32, weight=ft.FontWeight.BOLD, color="white"),
        ft.Text("لوحة التحكم الأمنية والهندسية للهواتف", size=14, color="blue", italic=True),
        ft.Divider(height=20, color="white"),
        url_entry,
        ft.Container(height=10),
        ft.Row(alignment="center", controls=[
            ft.ElevatedButton("فحص الرابط", on_click=check_url, bgcolor="blue", color="white"),
            ft.ElevatedButton("IP الجهاز", on_click=get_local_ip, bgcolor="green", color="white"),
        ]),
        ft.Container(height=15),
        ft.Container(content=result_text, bgcolor="black", padding=15, border_radius=10, width=340)
    )

ft.app(target=main)
