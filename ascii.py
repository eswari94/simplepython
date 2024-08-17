from pyfiglet import Figlet

def generate_ascii_art(text, font_name='slant'):
    try:
        custom_fig = Figlet(font=font_name)
        ascii_art = custom_fig.renderText(text)
        return ascii_art
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    text = input("Enter the text you want to convert to ASCII art: ")
    print("\nAvailable Fonts:\n")
    
    # Display a list of available fonts
    available_fonts = Figlet().getFonts()
    print(", ".join(available_fonts))

    font_choice = input("\nEnter the font name you want to use (or press Enter to use default): ")
    font_choice = font_choice if font_choice in available_fonts else 'slant'
    
    art = generate_ascii_art(text, font_choice)
    print("\nGenerated ASCII Art:\n")
    print(art)

