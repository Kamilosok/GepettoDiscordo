import decrypter

from os import system, name

import openai

import keyboard as kb


def cls():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


def multilineInput():

    # Here so keyboard actually check for Shift press afterwards
    kb.is_pressed('Shift')
    text = ""
    sentry = True
    while sentry:
        temp = input()
        text += temp
        sentry = kb.is_pressed("Shift")
        if sentry:
            text += '\n'
    return text


decrypter = decrypter.Tokener()
openai.api_key = decrypter.accessFile(decrypter, "GepetKey.txt")

cls()
print("GPT READY", end='\n\n')

messages = []

print("User", end=': ')
message = multilineInput()


while message != "EXIT":
    messages.append({"role": "user", "content": message})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=messages,
                                              n=1, max_tokens=1000, top_p=0.8)

    if len(completion.choices) == 1:
        oneChoice = completion.choices[0]
        if oneChoice.finish_reason == "stop":
            messages.append(oneChoice.message)
        else:
            print(oneChoice.finish_reason)

    else:
        # Pick a choice somehow and branch it out, for now add all responses to the messages list
        for choice in completion.choices:
            if choice.finish_reason == "stop":
                messages.append(choice.message)
            else:
                print(choice.finish_reason)

    cls()

    choiceNum = 0
    for message in messages:
        match message["role"]:
            case "user":
                choiceNum = 0
                print("User", end=': ')
            case "assistant":
                choiceNum += 1
                print(f"GPT, {choiceNum}", end=': ')
            case "system":
                choiceNum = 0
                print("System", end=': ')
        print(message["content"])

    print("User", end=': ')
    message = multilineInput()

print("EXITED")
