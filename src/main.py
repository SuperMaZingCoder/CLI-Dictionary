import namespace.download.get_definition as api
import namespace.colors.colorit as colorit

colorit.init_colorit()

program_running = True

while program_running:
    w = input("What word would you like to request? (type :quit to quit) ")
    if w != ":quit":
        w_inf = api.get_word(w)
        formatted_inf = """
{colored_word}: {word}
{colored_offensive}: {offensive}
{colored_definitions}: \n{definitions}""".format(
            colored_word=colorit.color("Word", colorit.Colors.blue),
            colored_offensive=colorit.color("Is Offensive", colorit.Colors.blue),
            colored_definitions=colorit.color("Definitions", colorit.Colors.blue),
            word=w_inf["word"],
            offensive=w_inf["offensive"],
            definitions="".join(
                [
                    f"   {i+1}: {definition} \n"
                    for i, definition in enumerate(w_inf["definitions"])
                ]
            ),
        )
        print(formatted_inf)
    else:
        program_running = False
