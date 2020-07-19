import namespace.download.get_definition as api
import namespace.colors.colorit as colorit

colorit.init_colorit()

program_running = True

while program_running:
    w = input(colorit.color("What word would you like to request? (type :quit to quit) ", colorit.Colors.green))
    if w != ":quit":
        w_inf = api.get_word(w)
        newline = '\n'
        formatted_inf = (
            f"{colorit.color('Word', colorit.Colors.blue)}: {w_inf['word']}{newline}"
            f"{colorit.color('Is Offensive', colorit.Colors.blue)}: {w_inf['offensive']}{newline}"
            f"{colorit.color('Definitions', colorit.Colors.blue)}"
            f"{''.join([f'{newline}   {i+1}: {definition}' for i, definition in enumerate(w_inf['definitions'])])}"
        )
        print(formatted_inf)
    else:
        program_running = False
