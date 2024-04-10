import discord
from discord.ext import commands
from settings import settings
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We logged in as {bot.user}')
  
@bot.command()
async def quiz(ctx):
    questions = [
        {
            "question": "Jaki jest główny gaz cieplarniany emitowany przez działalność człowieka?",
            "answers": ["a) Dwutlenek węgla", "b) Metan", "c) Podtlenek azotu"],
            "correct_answer": "a"
        },
        {
            "question": "Który z poniższych materiałów nie nadaje się do recyklingu?",
            "answers": ["a) Papier", "b) Plastik", "c) Szkło", "d) Żywność"],
            "correct_answer": "d"
        },
        {
            "question": "Jaki jest najskuteczniejszy sposób na ograniczenie emisji zanieczyszczeń powietrza z pojazdów?",
            "answers": ["a) Używanie katalizatorów", "b) Jazda na rowerze lub chodzenie zamiast jazdy samochodem", "c) Stosowanie paliwa o niskiej zawartości siarki"],
            "correct_answer": "b"
        },
        {
            "question": "Który z poniższych gatunków jest najbardziej zagrożony wyginięciem?",
            "answers": ["a) Tygrys syberyjski", "b) Panda wielka", "c) Słoń afrykański"],
            "correct_answer": "a"
        },
        {
            "question": "Jaki jest cel protokołu z Kioto?",
            "answers": ["a) Ograniczenie emisji gazów cieplarnianych", "b) Ochrona bioróżnorodności", "c) Zwiększenie wykorzystania energii odnawialnej"],
            "correct_answer": "a"
        }
    ]

    score = 0

    for question in questions:
        await ctx.send(question["question"])
        for answer in question["answers"]:
            await ctx.send(answer)
        user_answer = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
        if user_answer.content == question["correct_answer"]:
            score += 1
            await ctx.send("Poprawna odpowiedź!")
        else:
            await ctx.send("Niepoprawna odpowiedź. Prawidłowa odpowiedź to **" + question["correct_answer"] + "**.")

    await ctx.send("**Twój wynik to:** " + str(score) + "/" + str(len(questions)))


bot.run(settings)
