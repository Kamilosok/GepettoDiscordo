import openai
import decrypter

decoder = decrypter.Tokener()
openai.api_key = decoder.accessFile(decoder, "GepetKey.txt")

#for i in range(len(models.data)):
#    print(models.data[i].id)

print("GPT READY\n")

message = input()

messages = [
    {"role": "user", "content": message}
]
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301", messages=messages, n=1)

messages.append(completion.choices[0].message)
print(messages[1])