import openai
import decrypter
from os import system, name


def cls():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


decoder = decrypter.Tokener()
openai.api_key = decoder.accessFile(decoder, "GepetKey.txt")

cls()
print("GPT READY", end='\n\n')

messages = []

print("User", end=': ')
message = input()

while message != "EXIT":
    messages.append({"role": "user", "content": message})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=messages,
                                              n=1, max_tokens=1000, top_p=1.0)

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

    for message in messages:
        match message["role"]:
            case "user":
                print("User", end=': ')
            case "assistant":
                print("GPT", end=': ')
            case "system":
                print("System", end=': ')
        print(message["content"])

    print("User", end=': ')
    message = input()

print("EXITED")
