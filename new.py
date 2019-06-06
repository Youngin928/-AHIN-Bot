import discord
import datetime


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    game = discord.Game('[ AHIN ] 아인서버 / *도움말 ')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("*정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith('*하이'):
        await message.channel.send('**```안녕하세요 !```**')

    if message.content.startswith('*하잉'):
        await message.channel.send('**안녕하세요 !**')

    if message.content.startswith('*빠이'):
        await message.channel.send('**잘가 !**')

    if message.content.startswith('*도움말'):
        await message.channel.send('****')

    if message.content.startswith('*잘강'):
        await message.channel.send('**잘가 !**')

    if message.content.startswith('*서버주소'):
        await message.channel.send('**영 인#1725에게 DM !**')

    if message.content.startswith('*영인'):
        await message.channel.send('**앙 영인띠 !**')

    if message.content.startswith('*시나'):
        embed = discord.Embed(color=0x10e110)
        embed.add_field(name="**[ AHIN ] Bot**", value="시나시나시나 ", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith('*어쩌라고'):
        await message.channel.send('**凸 !**')

    if message.content.startswith("*시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        embed = discord.Embed(color=0x10e110)
        embed.add_field(name="시간",value=str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 입니다 !",inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("*공지"):
        msg = message.content[4:]
        embed = discord.Embed(title=":loudspeaker: 공지",description=(msg),color=0x188bb4)
        embed.set_footer(text=" 공지 작성자 - " + (str(message.author.name)) + "#" + (str(message.author.discriminator)) + " [ 관리자 ] ")
        await message.channel.send(embed=embed)








client.run('NTg0Njc3OTczMzMyOTgzODA5.XPO_Qg.1KtSDiqtX8FrtzOrgUrstElvw-k')




