import namespace.download.get_definition as api
import namespace.colors.colorit as colorit

colorit.init_colorit()

program_running = True

while program_running:
    w = input(
        colorit.color(
            "What word would you like to request? (type :quit to quit) ",
            colorit.Colors.green,
        )
    )
    if w != ":quit":
        w_inf = api.get_word(w)
        newline = "\n"
        if w_inf["return_type"] == "definitions":
            formatted_res = (
                f"{colorit.color('Word', colorit.Colors.blue)}: {w_inf['word']}{newline}"
                f"{colorit.color('Definitions', colorit.Colors.blue)}"
                f"{''.join([f'{newline}   {i+1}: {definition}' for i, definition in enumerate(w_inf['definitions'])])}"
            )
        elif w_inf["return_type"] == "options":
            if len(w_inf["options"]) > 0:
                formatted_res = (
                    f"{colorit.color('Word not found.', colorit.Colors.red)}{newline}"
                    f"Maybe you meant:"
                    f"{''.join([f'{newline}   {i}: {option}' for i, option in enumerate(w_inf['options'])])}"
                )
            elif len(w_inf["options"]) == 0:
                formatted_res = f"{colorit.color('Word not found. No similar words were found in the dictionary.', colorit.Colors.red)}{newline}"
        print(formatted_res)
    else:
        program_running = False
