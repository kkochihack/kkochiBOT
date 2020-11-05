import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("봇이 잠에서 깼어요!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("네 반가워요")
    if message.content.startswith("도움말"):
        await message.channel.send("잠시만 기다려 주세요!")
    if message.content.startswith("도움말"):
            await message.channel.send("``안녕`` ``놀자`` ``봇 크레딧`` 입니다")
    if message.content.startswith("도움말"):
            await message.channel.send("잠시만 기다려 주세요!")
    if message.content.startswith("놀자"):
        await message.channel.send("그래요! ..하지만 귀찮아요:(")
    if message.content.startswith("봇 크레딧"):
        await message.channel.send("```제작 날짜 : 11-04```")
    if message.content.startswith("봇 크레딧"):
        await message.channel.send("```제작자 : 💎[ 𝕜𝕜𝕠𝕔𝕙𝕚 ] 꼬치💎#5412```")
    if message.content.startswith("봇 크레딧"):
        await message.channel.send("```버전 : 1.0```")


access = token = os.environ["BOT_TOKEN"]
client.run(access_token)
