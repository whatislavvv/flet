import flet as ft

def main_page(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    hello_text = ft.Text("Hello, world!")
    name_input = ft.TextField(label="Enter your name")
    eleveated_button = ft.ElevatedButton(text = 'Send',icon = ft.Icons.SEND)
    # text_button = ft.TextButton()
    # icon_button = ft.IconButton()
    page.add(hello_text,name_input, eleveated_button)# text_button,icon_button#)

ft.run(main_page, view=ft.AppView.WEB_BROWSER)
# ft.run(main_page)
