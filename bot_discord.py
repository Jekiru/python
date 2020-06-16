#! /usr/bin/python3


import discord
import asyncio
import random
import os
from discord.ext import commands
from discord.utils import get
import youtube_dl

client = commands.Bot(command_prefix='!')#discord.Client()  # le bot sera appelé "client"
#bot = commands.Bot(command_prefix='!')
nom_role= "CSGO"
players = {}

@client.event
async def on_ready():
    print("Logged in as :", client.user.name)
    print("ID:", client.user.id)
    await client.change_presence(activity=discord.Game(name='En cours de création'))
    
@client.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.channels, name='général')
    await channel.send(f"Bienvenue sur {member.guild.name} , {member.mention}")
    role = get(member.guild.roles, name=nom_role)
    await member.add_roles(role)
    print(f"{member} a le role {role}")
    
@client.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.channels, name='général')
    await channel.send(f"{member.name} a quitté le serveur")

@client.command()

async def alix(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        fichier = random.choice(os.listdir("/home/pi/bot/ALIX"))
        print(fichier)
        await ctx.channel.send(file=discord.File("ALIX/" + fichier))
        print(ctx.author)
    else:
        await ctx.send("NON")

@client.command()

async def hugo(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        fichier = random.choice(os.listdir("/home/pi/bot/HUGO"))
        print(fichier)
        await ctx.channel.send(file=discord.File("HUGO/" + fichier))
    else:
        await ctx.send("NON")

@client.command()

async def thomas(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        fichier = random.choice(os.listdir("/home/pi/bot/THOMAS"))
        print(fichier)
        await ctx.channel.send(file=discord.File("THOMAS/" + fichier))
    else:
        await ctx.send("NON")

@client.command()

async def jeremy(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        fichier = random.choice(os.listdir("/home/pi/bot/JEREMY"))
        print(fichier)
        await ctx.channel.send(file=discord.File("JEREMY/" + fichier))
    else:
        await ctx.send("NON")

@client.command()

async def dorian(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        fichier = random.choice(os.listdir("/home/pi/bot/DORIAN"))
        print(fichier)
        await ctx.channel.send(file=discord.File("DORIAN/" + fichier))
    else:
        await ctx.send("NON")

@client.command()

async def leo(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        await ctx.channel.send(file=discord.File("leo.gif"))
    else:
        await ctx.send("NON")

@client.command()
async def blanco(ctx):
    auteur= ctx.author
    if get (auteur.roles, name="Droit bot"):
        fichier = random.choice(os.listdir("/home/pi/bot/Blanco"))
        print(fichier)
        await ctx.channel.send(file=discord.File("Blanco/" + fichier))
    else:
        await ctx.send("NON")

@client.command()

async def join(ctx):
    channel = ctx.message.author.voice.channel
    print(channel)
    voice = await channel.connect()



@client.command(pass_context=True, aliases=['p', 'pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Music playing")
        return

    await ctx.send("Video en cours de téléchargement")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 10

    nname = name.rsplit("-", 2)
    await ctx.send(f"En cours de lecture: {nname[0]}")
    print("playing\n")

@client.command()
async def prout(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    fichier = random.choice(os.listdir("/home/pi/bot/Prout"))
    print(fichier)
    voice.play(discord.FFmpegPCMAudio("Prout/"+ fichier), after=lambda e: print("Prout fini !"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 10

@client.command()

async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Musique en pause")
        voice.pause()
        await ctx.send("Musique en pause")
    else:
        print("Music not playing failed pause")
        await ctx.send("Aucune musique en cours")

@client.command()

async def suite(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Suite de la musique")
    else:
        print("Music is not paused")
        await ctx.send("La musique n'est pas en pause")


@client.command()

async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        print("Music stopped")
        voice.stop()
        await ctx.send("STOP")
    else:
        print("No music playing failed to stop")
        await ctx.send("Aucune musique en cours impossible de stop")
        
@client.command()

async def spam(ctx, nb):
    nb=int(nb)
    if nb > 10:
        await ctx.channel.send("Toi t'es vraiment un fdp à vouloir spammer")
    else:
        for i in range (0, nb):
            await ctx.channel.send("pls porngif")

@client.command()

async def test(ctx, url):
    serveur = ctx.guild
    channel = ctx.message.author.voice.channel
    voice_client = await client.join_voice_channel(channel)
    player = await voice_client.create_ytdl_player(url)
    players[serveur.id] = player
    player.start()
    
client.run("no token for U")

