from pyrogram.errors import FloodWait, Forbidden, UserIsBlocked, MessageNotModified, ChatWriteForbidden, SlowmodeWait, QueryIdInvalid, PeerIdInvalid, UserNotParticipant
from datetime import datetime
import time
import spotipy
from sys import executable
# from Script import script
import psutil, shutil
from pyrogram import filters, enums, StopPropagation
import os
# from utils import get_size
import asyncio
from asyncio import sleep
# from Script import script
from pyrogram.types import CallbackQuery, Message
# from database.users_chats_db import db as dib
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.raw.functions import Ping
from mbot import LOG_GROUP, OWNER_ID, SUDO_USERS, Mbot, AUTH_CHATS, BUG, F_SUB, paste, F_SUB_CHANNEL_ID
from os import execvp, sys, execl, environ, mkdir
from apscheduler.schedulers.background import BackgroundScheduler
import shutil
from fsub import Fsub
from spotipy.oauth2 import SpotifyClientCredentials
# from tg import get_readable_file_size, get_readable_time

botStartTime = time.time()
MAIN = bool(environ.get('MAIN', False))
SLEEP = bool(environ.get('SLEEP', False))
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
import time
import datetime
from random import randint
from pyrogram import filters
from mbot.utils.mainhelper import parse_spotify_url, fetch_spotify_track, download_songs, thumb_down, copy, forward
from mbot.utils.ytdl import getIds, ytdl_down, audio_opt
from shutil import rmtree
from mutagen import File
from mutagen.flac import FLAC, Picture
from lyricsgenius import Genius
# from database.database import Database

supported_link = ["www.deezer.com", "open.spotify.com", "deezer.com", "spotify.com"]

NOT_SUPPORT = [
    
]

NO_SPAM = [
    
]

# db = Database()
genius = Genius("api_key")

# @ScreenShotBot.on_callback_query()
# async def __(c, m):
#     await foo(c, m, cb=True)

##  & filters.private add this to respond only in private Chat
@Mbot.on_message(filters.incoming & filters.text, group=-2)
async def _(c, m):
    message = m
    Mbot = c
    try:
        user_id = message.from_user.id
    except:
        user_id = 5268375124
    if not m.text:
        return
    try:
        if F_SUB and F_SUB_CHANNEL_ID:
            if not str(F_SUB_CHANNEL_ID).startswith("-100"):
               print(f"Skiping F_Sub as Your Id Must Start With -100 We Got {F_SUB_CHANNEL_ID}")
            else:
               await Fsub(message, Mbot, user_id)
    except (StopPropagation, ChatWriteForbidden):
        raise StopPropagation
    if message.text.startswith('/'):
        return
    elif message.text.startswith('https:'):
        return
    elif message.text.startswith('http:'):
        return
    elif message.text.startswith(','):
        return
    elif message.text.startswith('.'):
        return
    elif message.text.startswith('🎧'):
        return
    elif int(message.chat.id) in NOT_SUPPORT:
        return
    elif int(message.chat.id) in NO_SPAM:
        return
    u = message.from_user.id
    K = await message.reply("⌛")
    query = m.text
    reply_markup = []
    try:
        results = sp.search(query, limit=10)
        index = 0
        for item in results['tracks']['items']:
            reply_markup.append([InlineKeyboardButton(f"{item['name']} - {item['artists'][0]['name']}", callback_data=f"search_{index}_{results['tracks']['items'][int(index)]['id']}")])
            index += 1
        reply_markup.append([InlineKeyboardButton("❌", callback_data="cancel")])
        await K.delete()
        await message.reply(f"🔎I Found 10 Results For {query}",
                            reply_markup=InlineKeyboardMarkup(reply_markup))
    except:
        pass
        await message.reply(f"No results found for your {query}")
        await K.delete()
    finally:
        await m.continue_propagation()

@Mbot.on_callback_query(filters.regex(r"search"))
async def search(Mbot: Mbot, query: CallbackQuery):
    ind, index, track = query.data.split("_")
    try:
        message = query.message
        await query.message.delete()
        client = sp
        song = await fetch_spotify_track(client, track)
        item = sp.track(track_id=track)
        thumbnail = await thumb_down(item['album']['images'][0]['url'], song.get('deezer_id'))
        PForCopy = await query.message.reply_photo(thumbnail, caption=f"🎧 Title : `{song['name']}­­`\n🎤 Artist : `{song['artist']}`­\n💽 Album : `{song['album']}`\n🗓 Release Year: `{song['year']}`\n❗️Is Local:`{item['is_local']}`\n 🌐ISRC: `{item['external_ids']['isrc']}`\n\n[IMAGE]({item['album']['images'][0]['url']})\nTrack id:`{song['deezer_id']}`",
                                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="❌", callback_data="cancel")]]))
        randomdir = f"/tmp/{str(randint(1, 100000000))}"
        mkdir(randomdir)
        run = True
        if run == True:
            try:
                path = await download_songs(item, randomdir)
            except Exception as e:
                pass
                # optional you can clear this or add this by using #
                await message.reply(e)
                # await Mbot.send_message(BUG,e)
                await query.message.reply_text(f"[{song.get('name')} - {song.get('artist')}](https://open.spotify.com/track/{song.get('deezer_id')}) Track Not Found ⚠️")
                # await message.reply_text(f"try `/saavn {song.get('name')} - {song.get('artist')}`")
            try:
                await sleep(0.6)
                audio = FLAC(path)
                audio["TITLE"] = f" {song.get('name')}"
                audio["ORIGINALYEAR"] = song.get('year')
                audio["YEAR_OF_RELEASE"] = song.get('year')
                audio["WEBSITE"] = "https://t.me/spotify_downloa_bot"
                audio["GEEK_SCORE"] = "9"
                audio["ARTIST"] = song.get('artist')
                audio["ALBUM"] = song.get('album')
                audio["DATE"] = song.get('year')
                audio["DISCNUMBER"] = f" {item['disc_number']}"
                audio["TRACKNUMBER"] = f" {item['track_number']}"
                try:
                    audio["ISRC"] = item['external_ids']['isrc']
                except:
                    pass
                try:
                    songGenius = genius.search_song(song('name'), song('artist'))
                    audio["LYRICS"] = (songGenius.lyrics)
                except:
                    pass
                audio.save()
                audi = File(path)
                image = Picture()
                image.type = 3
                if thumbnail.endswith('png'):
                    mime = 'image/png'
                else:
                    mime = 'image/jpeg'
                image.desc = 'front cover'
                with open(thumbnail, 'rb') as f:  # better than open(albumart, 'rb').read() ?
                    image.data = f.read()

                audi.add_picture(image)
                audi.save()
            except:
                pass
            try:
                dForChat = await message.reply_chat_action(enums.ChatAction.UPLOAD_AUDIO)
                # sleep(1)
                AForCopy = await query.message.reply_audio(path, performer=f"{song.get('artist')}­", title=f"{song.get('name')} - {song.get('artist')}", caption=f"[{song.get('name')}](https://open.spotify.com/track/{song.get('deezer_id')}) | {song.get('album')} - {song.get('artist')}", thumb=thumbnail, parse_mode=enums.ParseMode.MARKDOWN, quote=True,
                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="❌", callback_data="cancel")]]))
                await forward(PForCopy, AForCopy)
            except Exception as e:
                pass
                # await Mbot.send_message(BUG,e)
    except NameError as e:
        pass
        await Mbot.send_message(BUG, e)
        await query.answer("Your Query Is Too Old ❌")
    except UserIsBlocked:
        pass
    except (FileNotFoundError, OSError):
        pass
        await query.answer('Sorry, We Are Unable To Procced It 🤕❣️')
    except FloodWait as e:
        pass
        await sleep(e.value)
        await query.answer(f"Telegram says: [420 FLOOD_WAIT_X] - A wait of {e.value} seconds is required !")
    except SlowmodeWait as e:
        pass
        await sleep(e.value)
    except RPCError:
        pass
        await query.answer(f"telegram says 500 error, so please try again later.❣️")
    except Exception as e:
        pass
        await query.answer("Sorry, We Are Unable To Procced It 🤕❣️")
    #   await Mbot.send_message(BUG,f"Query Raised Erorr {e} On {query.message.chat.id} {query.message.from_user.mention}")
    finally: 
        await sleep(2.0)
        try:
            rmtree(randomdir)
        except:
            pass
        try:
            await query.message.reply_text(f"Done✅",   
         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Feedback", callback_data="feed")]]))
        except:
            pass     

@Mbot.on_callback_query(filters.regex(r"refresh"))
async def refresh(Mbot, query):
      try:
          try:
              user_id = query.from_user.id
          except Exception:
             return 
          try:
              get_member = await Mbot.get_chat_member(chat_id=F_SUB_CHANNEL_ID,user_id=user_id)
          except UserNotParticipant:
              try:
                  await query.answer("Please Join The Channel",show_alert=True)
              except QueryIdInvalid:
                  await query.message.reply("Please Join The Channel :)")
              await query.message.stop_propagation()
          except PeerIdInvalid:
              try:
                  await Mbot.send_chat_action(chat_id=user_id,action=enums.ChatAction.TYPING)
                  get_member = await Mbot.get_chat_member(chat_id=F_SUB_CHANNEL_ID,user_id=user_id)
              except PeerIdInvalid:
                  pass
              except UserIsBlocked:
                  pass
              except UserNotParticipant:
                  await query.answer("Please Join The Channel",show_alert=True)
                  await query.message.stop_propagation()
          await query.message.delete()
          try:
              await query.answer("Congratulations You Are  Unlocked 🤝 ",show_alert=True)
          except:
               pass
          await query.message.reply("Congratulations You Had Unlocked Go Ahead 🤝 Keep The Bond With Us❣️")
      except (StopPropagation,AttributeError):
          pass
      except Exception as e:
          await Mbot.send_message(BUG, f"#Fsub refresh module Exception Raised {e}\n {paste(traceback.format_exc())}")
          await query.message.reply('503: Sorry, We Are Unable To Procced It 🤕❣️')     
      for var in list(locals()):
        if var != '__name__' and var != '__doc__':
            del locals()[var]
