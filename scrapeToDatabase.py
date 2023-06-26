import discord
import decrypter
import pyodbc

intents = discord.Intents.default()
client = discord.Client(intents=intents)

#Decoding the token
decoder = decrypter.Tokener()
token = decoder.accessFile(decoder, "TokenButHashedAlsoPrivateKey.txt")

#TestID 1021492127647154208
#GoodId 751861351378583562
channelId = int(751861351378583562)
notCheckStart = (':', '!', '*')
notCheckOverall = ('//', '<@')
conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=F:\Git\GepettoDiscordo\Database\Logs.accdb;')


cursor = conn.cursor()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    #Saving channel and server for something
    channel = client.get_channel(int(channelId))
    guild = channel.guild
    counter = 0
    #If the message is not empty or unimportant, save it into the database
    async for message in channel.history(limit = 2147483647, oldest_first = True):
        if message.content != '' and not any(x in message.content[0] for x in notCheckStart) and \
                not any(x in message.content for x in notCheckOverall) and not message.author.bot:
            #Change this to save into database
            #print(str(message.author))
            out = message.content.lower()
            insertToDatabase(str(message.author)[0: len(str(message.author))-5], out)
            #print(str(out) + '\n######################')
            counter +=1
            print(counter)

def insertToDatabase(author, message):
    sql = "insert into Messages (Author, Message) values (?, ?)"
    tuples = [(str(author), str(message))]
    cursor.executemany(sql, tuples)
    cursor.commit()

if __name__ == "__main__":
    client.run(token)
