import flet as ft
import os

def main(page: ft.Page):
    page.title = "Business AI App"
    page.add(ft.Text("Hello from Flet!"))

ft.app(
    target=main,
    port=int(os.environ.get("PORT", 8000)),
    view=ft.AppView.FLET_APP_WEB,
    assets_dir="assets"
)
