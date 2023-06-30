import keyboard as kb


def multilineInput():

    kb.is_pressed('Shift')
    text = ""
    sentry = True
    while sentry:
        # Here so keyboard actually check for Shift press afterwards
        temp = input()
        text += temp
        sentry = kb.is_pressed("Shift")
        if sentry:
            text += '\n'
    return text


i = multilineInput()

print(i)
