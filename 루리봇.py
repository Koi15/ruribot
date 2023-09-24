import discord
from discord.ext import commands

# 봇의 설정
token = 'MTE1NTM2NzAwMzg5MzI2ODU2MA.G7DIK5.fmo_lzgw4TCH5vFVz8lcsjTqL3lL2TFBZY0RS4'
prefix = '!'

# 봇 생성
bot = commands.Bot(command_prefix=prefix)

# 봇이 준비되었을 때 실행되는 이벤트 핸들러
@bot.event
async def on_ready():
    print(f'{bot.user.name}이(가) 성공적으로 로그인했습니다.')

# 멘션에 대한 응답 처리
@bot.event
async def on_message(message):
    # 봇 자신의 메시지는 무시
    if message.author == bot.user:
        return

    # 사용자가 봇을 멘션한 경우
    if bot.user.mentioned_in(message):
        embed = discord.Embed(description='사용할 코드를 보내주세요')
        await message.channel.send(embed=embed)

    # RURI 단어가 포함된 메시지인 경우
    if 'RURI' in message.content:
        embed = discord.Embed(description='코드 사용이 완료되었습니다. 관리자를 멘션하세요.')
        await message.channel.send(embed=embed)

    await bot.process_commands(message)

# 봇 실행
bot.run(token)
