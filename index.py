import flet as ft
import re

def main(page: ft.Page):
    page.title = "Sami's Secure Vault"
    page.window_width = 400
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # UI Elements
    title = ft.Text("Password Strength Checker", size=25, weight="bold", color="blue400")
    
    password_input = ft.TextField(
        label="Enter Password",
        password=True,
        can_reveal_password=True,
        border_radius=15,
        on_change=lambda e: check_strength(e)
    )

    strength_bar = ft.ProgressBar(value=0, width=300, color="red", bgcolor="#333333")
    strength_text = ft.Text("Strength: Too Weak", color="red")
    
    # Logic for Strength
    def check_strength(e):
        pwd = password_input.value
        score = 0
        
        if len(pwd) >= 8: score += 0.25
        if re.search(r"[A-Z]", pwd): score += 0.25
        if re.search(r"[0-9]", pwd): score += 0.25
        if re.search(r"[@$!%*?&#]", pwd): score += 0.25
        
        strength_bar.value = score
        
        if score <= 0.25:
            strength_bar.color = "red"
            strength_text.value = "Strength: Weak ❌"
            strength_text.color = "red"
        elif score <= 0.50:
            strength_bar.color = "orange"
            strength_text.value = "Strength: Medium ⚠️"
            strength_text.color = "orange"
        elif score <= 0.75:
            strength_bar.color = "yellow"
            strength_text.value = "Strength: Good 👍"
            strength_text.color = "yellow"
        else:
            strength_bar.color = "green"
            strength_text.value = "Strength: Very Strong 💪"
            strength_text.color = "green"
            
        page.update()

    # Layout construction
    card = ft.Container(
        content=ft.Column([
            title,
            ft.Divider(height=20, color="transparent"),
            password_input,
            ft.Text("Security Level:", size=12),
            strength_bar,
            strength_text,
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=30,
        bgcolor="#1E1E1E",
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=15, color="black")
    )

    page.add(card)

ft.app(target=main)