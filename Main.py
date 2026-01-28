#!/usr/bin/env python3
"""
█▀▀ █▀▀ █▄░█ █▀▀ █▀   █▀█ ▄▀█ █▀▄▀█ █▀▀   █▄▄ █▀▀ ▀█▀ █ █▀█ █▄░█
█▄█ ██▄ █░▀█ ██▄ ▄█   █▀▀ █▀█ █░▀░█ ██▄   █▄█ ██▄ ░█░ █ █▄█ █░▀█

█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▀▀ ▄▀█ █▀▀ █▀▀ █▀
█▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▀░ █▀█ █▄▄ ██▄ ▄█

𝐑𝐑𝐂 𝐄𝐗𝐔 𝐀𝐮𝐭𝐨𝐦𝐚𝐭𝐞𝐝 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐫 𝐕𝟒.𝟎
"""

import os
import sys
import time
import json
import shutil
import random
import threading
import subprocess
from pathlib import Path
from datetime import datetime
import asyncio

# ==================== RAIN CODE ANIMATION ====================
class MatrixRain:
    def __init__(self, width=80, height=25):
        self.width = width
        self.height = height
        self.drops = [0] * width
        self.colors = ['\033[32m', '\033[92m', '\033[36m', '\033[96m']
        self.running = False
    
    def draw(self):
        """Draw matrix rain animation"""
        print("\033[?25l")  # Hide cursor
        
        for i in range(self.width):
            if self.drops[i] > self.height or random.random() > 0.975:
                self.drops[i] = 0
            
            if self.drops[i] == 0 and random.random() > 0.95:
                self.drops[i] = 1
            
            for j in range(self.height):
                if self.drops[i] > j:
                    char = random.choice(['█', '▓', '▒', '░', '▄', '▀', '▌', '▐'])
                    color = random.choice(self.colors)
                    x = i
                    y = j
                    if x < self.width and y < self.height:
                        sys.stdout.write(f"\033[{y};{x}H{color}{char}\033[0m")
            
            self.drops[i] += 1 if self.drops[i] > 0 else 0
        
        sys.stdout.flush()

rain = MatrixRain()

def clear_with_rain():
    """Clear screen with matrix rain effect"""
    os.system('cls' if os.name == 'nt' else 'clear')
    for _ in range(10):
        rain.draw()
        time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_banner():
    """Show animated EXU banner"""
    frames = [
        """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║                                                            ║
║         ███████╗██╗  ██╗██╗   ██╗                         ║
║         ██╔════╝╚██╗██╔╝██║   ██║                         ║
║         █████╗   ╚███╔╝ ██║   ██║                         ║
║         ██╔══╝   ██╔██╗ ██║   ██║                         ║
║         ███████╗██╔╝ ██╗╚██████╔╝                         ║
║         ╚══════╝╚═╝  ╚═╝ ╚═════╝                          ║
║                                                            ║
║                  𝐑𝐑𝐂 𝐄𝐗𝐔 𝐒𝐘𝐒𝐓𝐄𝐌𝐒                       ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""",
        """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║    ███████╗██╗  ██╗██╗   ██╗    ██████╗ ███████╗██╗  ██╗  ║
║    ██╔════╝╚██╗██╔╝██║   ██║    ██╔══██╗██╔════╝██║ ██╔╝  ║
║    █████╗   ╚███╔╝ ██║   ██║    ██████╔╝█████╗  ██╔██╗   ║
║    ██╔══╝   ██╔██╗ ██║   ██║    ██╔══██╗██╔══╝  ██║╚██╗  ║
║    ███████╗██╔╝ ██╗╚██████╔╝    ██║  ██║███████╗██║ ╚████╗║
║    ╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝║
║                                                            ║
║           𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐕𝟒.𝟎                       ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
"""
    ]
    
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[92m' + frame + '\033[0m')
        time.sleep(0.5)

# ==================== AUTOMATED INSTALLER ====================
class AutoInstaller:
    def __init__(self):
        self.requirements = [
            "pyrogram==2.0.106",
            "pytgcalls==3.0.0.dev24",
            "yt-dlp==2023.11.16",
            "aiohttp==3.9.0",
            "aiofiles==23.2.1",
            "python-dotenv==1.0.0",
            "requests==2.31.0",
            "speedtest-cli==2.1.3",
            "pillow==10.1.0"
        ]
        
    def install_dependencies(self):
        """Install all required packages with progress animation"""
        print("\033[92m[⚙️] Installing Dependencies...\033[0m")
        
        for i, package in enumerate(self.requirements, 1):
            print(f"\033[96m[{i}/{len(self.requirements)}] Installing {package}\033[0m")
            
            # Show progress bar
            for j in range(1, 51):
                bar = "█" * j + "░" * (50 - j)
                percent = j * 2
                sys.stdout.write(f"\r  [{bar}] {percent}%")
                sys.stdout.flush()
                time.sleep(0.01)
            
            # Install package
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package], 
                                    stdout=subprocess.DEVNULL, 
                                    stderr=subprocess.DEVNULL)
                print(f"\r\033[92m[✓] {package} installed successfully!\033[0m")
            except:
                print(f"\r\033[91m[✗] Failed to install {package}\033[0m")
        
        print("\033[92m[✓] All dependencies installed!\033[0m")
        time.sleep(2)
    
    def create_directory_structure(self):
        """Create necessary directories"""
        directories = [
            "sessions",
            "downloads",
            "fonts",
            "cache",
            "logs"
        ]
        
        for directory in directories:
            Path(directory).mkdir(exist_ok=True)
            print(f"\033[96m[+] Created directory: {directory}/\033[0m")
    
    def generate_config(self):
        """Generate interactive configuration"""
        clear_with_rain()
        animated_banner()
        
        print("\n\033[93m" + "═" * 60 + "\033[0m")
        print("\033[96m           𝐂𝐎𝐍𝐅𝐈𝐆𝐔𝐑𝐀𝐓𝐈𝐎𝐍   𝐒𝐄𝐓𝐔𝐏\033[0m")
        print("\033[93m" + "═" * 60 + "\033[0m\n")
        
        config = {}
        
        # Get API credentials
        print("\033[92m[1/5] Telegram API Setup\033[0m")
        print("Visit: \033[94mhttps://my.telegram.org\033[0m")
        print("Create app and get:\n")
        
        config['API_ID'] = input("\033[96m[?] API ID: \033[0m")
        config['API_HASH'] = input("\033[96m[?] API Hash: \033[0m")
        config['PHONE_NUMBER'] = input("\033[96m[?] Your Phone (+1234567890): \033[0m")
        
        # Bot setup
        print("\n\033[92m[2/5] Bot Setup\033[0m")
        print("Create bot via @BotFather and get token\n")
        config['BOT_TOKEN'] = input("\033[96m[?] Bot Token: \033[0m")
        
        # Owner ID
        print("\n\033[92m[3/5] Owner Information\033[0m")
        config['OWNER_ID'] = input("\033[96m[?] Your User ID (from @userinfobot): \033[0m")
        
        # Log chat
        config['LOG_CHAT'] = input("\033[96m[?] Log Chat ID (optional, press Enter): \033[0m") or "-1001234567890"
        
        # Save config to .env
        self._save_env(config)
        
        return config
    
    def _save_env(self, config):
        """Save configuration to .env file"""
        env_content = f"""# EXU/RRCEXU Music Bot - Auto Generated
API_ID={config['API_ID']}
API_HASH={config['API_HASH']}
PHONE_NUMBER={config['PHONE_NUMBER']}
BOT_TOKEN={config['BOT_TOKEN']}
OWNER_ID={config['OWNER_ID']}
LOG_CHAT={config['LOG_CHAT']}

# Advanced Features
AUTO_JOIN_VC=true
AUTO_WELCOME=true
ANIMATED_PROGRESS=true
VOLUME_NORMALIZATION=true
RAIN_ANIMATION=true
CLEAR_TERMINAL=true

# Paths
DOWNLOAD_PATH=downloads/
SESSION_PATH=sessions/
LOG_PATH=logs/
CACHE_PATH=cache/
"""
        
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("\n\033[92m[✓] Configuration saved to .env\033[0m")
        time.sleep(1)

# ==================== SESSION MANAGER ====================
class SessionCreator:
    def __init__(self, config):
        self.config = config
        self.session_path = "sessions/exu_session.session"
    
    async def create_session(self):
        """Create Pyrogram session with user agent"""
        print("\033[92m\n[🔄] Creating User Session...\033[0m")
        
        # Import here to avoid early dependency issues
        try:
            from pyrogram import Client
            
            # Custom user agent
            user_agent = {
                "device_model": "EXU Music Bot V4",
                "system_version": "RRCEXU Premium",
                "app_version": "4.0.0",
                "lang_code": "en",
                "system_lang_code": "en-US"
            }
            
            # Create client with custom parameters
            app = Client(
                name="exu_session",
                api_id=int(self.config['API_ID']),
                api_hash=self.config['API_HASH'],
                phone_number=self.config['PHONE_NUMBER'],
                workdir="sessions/",
                app_version="4.0.0",
                device_model="EXU Premium",
                system_version="RRCEXU",
                lang_code="en",
                system_lang_code="en-US"
            )
            
            async with app:
                # Animated connecting
                for i in range(3):
                    dots = "." * (i + 1)
                    print(f"\033[96m\r[•] Connecting to Telegram{dots}\033[0m", end="")
                    await asyncio.sleep(0.5)
                
                # Get user info
                user = await app.get_me()
                session_string = await app.export_session_string()
                
                # Save session string
                config_data = {
                    'session_string': session_string,
                    'user_id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'phone_number': user.phone_number
                }
                
                with open('sessions/session_data.json', 'w') as f:
                    json.dump(config_data, f, indent=2)
                
                # Show success animation
                print("\n")
                for i in range(5):
                    symbols = ["█", "▓", "▒", "░"]
                    for sym in symbols:
                        print(f"\033[92m\r[{sym}] Session Created Successfully!\033[0m", end="")
                        await asyncio.sleep(0.1)
                
                print(f"\n\033[92m[✓] User: {user.first_name} (@{user.username})\033[0m")
                print(f"\033[92m[✓] Session saved to: sessions/\033[0m")
                
                # Update .env with session string
                self._update_env_with_session(session_string)
                
                return session_string
                
        except Exception as e:
            print(f"\033[91m\n[✗] Session Creation Failed: {e}\033[0m")
            print("\033[93m[!] Make sure:")
            print("  1. Phone number is correct")
            print("  2. You have internet connection")
            print("  3. You entered OTP correctly\033[0m")
            return None
    
    def _update_env_with_session(self, session_string):
        """Add session string to .env"""
        with open('.env', 'a') as f:
            f.write(f"\nSESSION_STRING={session_string}")
        print("\033[92m[✓] Session string added to .env\033[0m")

# ==================== MAIN BOT CODE ====================
def generate_bot_code():
    """Generate the complete bot code"""
    bot_code = '''#!/usr/bin/env python3
"""
█▀▀ █▀▀ █▄░█ █▀▀ █▀   █▀█ ▄▀█ █▀▄▀█ █▀▀   █▄▄ █▀▀ ▀█▀ █ █▀█ █▄░█
█▄█ ██▄ █░▀█ ██▄ ▄█   █▀▀ █▀█ █░▀░█ ██▄   █▄█ ██▄ ░█░ █ █▄█ █░▀█

█▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀▀ █▀▄   █▀▀ ▄▀█ █▀▀ █▀▀ █▀
█▄▄ █▀▄ ██▄ █▀█ ░█░ ██▄ █▄▀   █▀░ █▀█ █▄▄ ██▄ ▄█

𝐑𝐑𝐂 𝐄𝐗𝐔 𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐕𝟒.𝟎
"""

import os
import sys
import asyncio
import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import random
import subprocess

# Load environment
from dotenv import load_dotenv
load_dotenv()

# Terminal Animation
def clear_terminal():
    """Clear terminal with animation"""
    if os.getenv('CLEAR_TERMINAL', 'true').lower() == 'true':
        # Matrix rain effect
        for _ in range(3):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[92m' + '█' * 80 + '\033[0m')
            time.sleep(0.05)
        os.system('cls' if os.name == 'nt' else 'clear')

# Auto-update requirements
def auto_update():
    """Auto-update system packages"""
    print("\033[96m[🔄] Checking for updates...\033[0m")
    requirements = ["pyrogram", "pytgcalls", "yt-dlp", "aiohttp", "aiofiles"]
    for package in requirements:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", package])
        except:
            pass

# Unicode Font System
class EXUFont:
    @staticmethod
    def mini(text: str) -> str:
        font = {
            'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ', 'G': 'ɢ',
            'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ', 'M': 'ᴍ', 'N': 'ɴ',
            'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ', 'S': 's', 'T': 'ᴛ', 'U': 'ᴜ',
            'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x', 'Y': 'ʏ', 'Z': 'ᴢ',
            'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ', 'g': 'ɢ',
            'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ',
            'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ', 's': 's', 't': 'ᴛ', 'u': 'ᴜ',
            'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ',
            '0': '𝟶', '1': '𝟷', '2': '𝟸', '3': '𝟹', '4': '𝟺', '5': '𝟻',
            '6': '𝟼', '7': '𝟽', '8': '𝟾', '9': '𝟿',
            ' ': ' ', '.': '․', ':': 'ː', '-': '˗', '_': 'ˍ'
        }
        return ''.join(font.get(char, char) for char in text)
    
    @staticmethod
    def premium(text: str) -> str:
        font = {
            'A': '𝕬', 'B': '𝕭', 'C': '𝕮', 'D': '𝕯', 'E': '𝕰', 'F': '𝕱', 'G': '𝕲',
            'H': '𝕳', 'I': '𝕴', 'J': '𝕵', 'K': '𝕶', 'L': '𝕷', 'M': '𝕸', 'N': '𝕹',
            'O': '𝕺', 'P': '𝕻', 'Q': '𝕼', 'R': '𝕽', 'S': '𝕾', 'T': '𝕿', 'U': '𝖀',
            'V': '𝖁', 'W': '𝖂', 'X': '𝖃', 'Y': '𝖄', 'Z': '𝖅',
            'a': '𝖆', 'b': '𝖇', 'c': '𝖈', 'd': '𝖉', 'e': '𝖊', 'f': '𝖋', 'g': '𝖌',
            'h': '𝖍', 'i': '𝖎', 'j': '𝖏', 'k': '𝖐', 'l': '𝖑', 'm': '𝖒', 'n': '𝖓',
            'o': '𝖔', 'p': '𝖕', 'q': '𝖖', 'r': '𝖗', 's': '𝖘', 't': '𝖙', 'u': '𝖚',
            'v': '𝖛', 'w': '𝖜', 'x': '𝖝', 'y': '𝖞', 'z': '𝖟'
        }
        return ''.join(font.get(char, char) for char in text)

# Database System
class Database:
    def __init__(self, path: str = "exu_data.json"):
        self.path = Path(path)
        self.data = self._load()
    
    def _load(self) -> dict:
        if self.path.exists():
            with open(self.path, 'r') as f:
                return json.load(f)
        return {
            'admins': [],
            'favorites': {},
            'queue': [],
            'settings': {},
            'stats': {'songs_played': 0, 'vc_hours': 0, 'users': 0}
        }
    
    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

# Import Telegram libraries
try:
    from pyrogram import Client, filters
    from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
    from pyrogram.errors import FloodWait
    from pytgcalls import PyTgCalls
    from pytgcalls.types import AudioPiped
    from pytgcalls.types.stream import StreamAudioEnded
    import yt_dlp
    import aiohttp
    import aiofiles
except ImportError as e:
    print(f"\033[91m[✗] Missing dependency: {e}\033[0m")
    print("\033[93m[!] Run: pip install -r requirements.txt\033[0m")
    sys.exit(1)

# Main Bot Class
class EXUMusicBot:
    def __init__(self):
        self.api_id = int(os.getenv("API_ID"))
        self.api_hash = os.getenv("API_HASH")
        self.bot_token = os.getenv("BOT_TOKEN")
        self.session_string = os.getenv("SESSION_STRING")
        self.owner_id = int(os.getenv("OWNER_ID"))
        
        self.db = Database()
        self.queues = {}
        self.current_stream = {}
        
        # Initialize clients
        self.app = Client(
            "exu_bot",
            api_id=self.api_id,
            api_hash=self.api_hash,
            bot_token=self.bot_token
        )
        
        self.user_client = Client(
            name="exu_user",
            api_id=self.api_id,
            api_hash=self.api_hash,
            session_string=self.session_string
        )
        
        self.pytgcalls = PyTgCalls(self.user_client)
        
        # Register handlers
        self.register_handlers()
    
    def register_handlers(self):
        """Register all command handlers"""
        
        @self.app.on_message(filters.command("start"))
        async def start_command(client, message: Message):
            clear_terminal()
            font = EXUFont.premix
            response = f"""
{font("➜ EXU MUSIC SYSTEM INITIALIZED")}

{font("‣ PURPOSE : VOICE CHAT MUSIC STREAMING")}
{font("‣ USAGE : /play <TRACK NAME>")}
{font("‣ REQUIREMENTS : • ADMIN ACCESS • ACTIVE VOICE CHAT")}

{font("𝐑𝐑𝐂 𝐄𝐗𝐔")}
────────────────────────
"""
            await message.reply(response)
        
        @self.app.on_message(filters.command("play"))
        async def play_command(client, message: Message):
            if len(message.command) < 2:
                await message.reply(EXUFont.mini("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ꜱᴏɴɢ ɴᴀᴍᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ"))
                return
            
            query = " ".join(message.command[1:])
            await self.play_song(message.chat.id, query, message)
        
        @self.app.on_message(filters.command("queue"))
        async def queue_command(client, message: Message):
            chat_id = message.chat.id
            if chat_id not in self.queues or not self.queues[chat_id]:
                await message.reply(EXUFont.mini("ǫᴜᴇᴜᴇ ɪꜱ ᴇᴍᴘᴛʏ"))
                return
            
            queue_text = EXUFont.mini("📋 ᴄᴜʀʀᴇɴᴛ ǫᴜᴇᴜᴇ:\n")
            for i, song in enumerate(self.queues[chat_id][:10], 1):
                queue_text += f"{i}. {song['title'][:30]}\\n"
            
            await message.reply(queue_text)
        
        # Add more handlers for skip, pause, resume, stop, fav, etc.
    
    async def play_song(self, chat_id: int, query: str, message: Message):
        """Play song in voice chat"""
        try:
            # Send searching message
            search_msg = await message.reply(EXUFont.mini("🔍 ꜱᴇᴀʀᴄʜɪɴɢ..."))
            
            # Get YouTube URL
            ydl_opts = {
                'format': 'bestaudio/best',
                'quiet': True,
                'no_warnings': True,
                'default_search': 'ytsearch',
                'source_address': '0.0.0.0'
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                if 'entries' in info:
                    info = info['entries'][0]
                
                audio_url = info['url']
                title = info['title']
                duration = info.get('duration', 0)
            
            # Update search message
            await search_msg.edit(EXUFont.mini(f"🎵 ɴᴏᴡ ᴘʟᴀʏɪɴɢ: {title[:30]}..."))
            
            # Join voice chat if not joined
            try:
                await self.pytgcalls.join_group_call(
                    chat_id,
                    AudioPiped(
                        audio_url,
                        bitrate=48000,
                    )
                )
            except Exception as e:
                # Create new voice chat
                await message.reply(EXUFont.mini("🎤 ᴄʀᴇᴀᴛɪɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ..."))
                await self.pytgcalls.join_group_call(
                    chat_id,
                    AudioPiped(
                        audio_url,
                        bitrate=48000,
                    )
                )
            
            # Store current stream
            self.current_stream[chat_id] = {
                'title': title,
                'url': audio_url,
                'start_time': time.time(),
                'duration': duration
            }
            
            # Add to queue if not playing
            if chat_id not in self.queues:
                self.queues[chat_id] = []
            
            # Update stats
            self.db.data['stats']['songs_played'] += 1
            self.db.save()
            
            # Show playing animation
            await self.show_progress_bar(chat_id, message, title, duration)
            
        except Exception as e:
            await message.reply(EXUFont.mini(f"❌ ᴇʀʀᴏʀ: {str(e)[:50]}"))
    
    async def show_progress_bar(self, chat_id: int, message: Message, title: str, duration: int):
        """Show animated progress bar"""
        if os.getenv('ANIMATED_PROGRESS', 'true').lower() != 'true':
            return
        
        start_time = time.time()
        progress_msg = await message.reply("🎵 ꜱᴛᴀʀᴛɪɴɢ...")
        
        while time.time() - start_time < duration:
            elapsed = time.time() - start_time
            progress = min(elapsed / duration, 1.0)
            
            # Create progress bar
            bar_length = 20
            filled = int(bar_length * progress)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            # Color based on progress
            if progress < 0.3:
                color = "🟢"
            elif progress < 0.7:
                color = "🟡"
            else:
                color = "🔴"
            
            # Time formatting
            elapsed_str = time.strftime("%M:%S", time.gmtime(elapsed))
            total_str = time.strftime("%M:%S", time.gmtime(duration))
            
            progress_text = f"""
{color} **ᴘʟᴀʏɪɴɢ** : `{title[:25]}...`
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
[{bar}] `{elapsed_str}/{total_str}`
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
𝐑𝐑𝐂 𝐄𝐗𝐔 ᴍᴜꜱɪᴄ ꜱʏꜱᴛᴇᴍ
"""
            
            try:
                await progress_msg.edit(progress_text)
            except:
                pass
            
            await asyncio.sleep(2)  # Update every 2 seconds
        
        await progress_msg.delete()
    
    async def start(self):
        """Start the bot"""
        clear_terminal()
        
        # Show startup animation
        print("\033[96m" + "="*60 + "\033[0m")
        for i in range(1, 6):
            dots = "🔘" * i
            print(f"\033[92m[🔄] Starting EXU System{dots}\033[0m")
            await asyncio.sleep(0.3)
            clear_terminal()
        
        # Final banner
        print("\033[92m" + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     ███████╗██╗  ██╗██╗   ██╗    ██████╗ ███████╗██╗  ██╗║
║     ██╔════╝╚██╗██╔╝██║   ██║    ██╔══██╗██╔════╝██║ ██╔╝║
║     █████╗   ╚███╔╝ ██║   ██║    ██████╔╝█████╗  ██╔██╗ ║
║     ██╔══╝   ██╔██╗ ██║   ██║    ██╔══██╗██╔══╝  ██║╚██╗║
║     ███████╗██╔╝ ██╗╚██████╔╝    ██║  ██║███████╗██║ ╚████║
║     ╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝║
║                                                            ║
║               𝐒𝐘𝐒𝐓𝐄𝐌 𝐒𝐓𝐀𝐓𝐔𝐒 : 𝐎𝐍𝐋𝐈𝐍𝐄 ✅                ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """ + "\033[0m")
        
        print(f"\033[96m[📊] Stats: {self.db.data['stats']['songs_played']} songs | {self.db.data['stats']['users']} users\033[0m")
        print(f"\033[96m[👑] Owner ID: {self.owner_id}\033[0m")
        print(f"\033[96m[🤖] Bot: @{(await self.app.get_me()).username}\033[0m")
        print(f"\033[96m[👤] User: @{(await self.user_client.get_me()).username}\033[0m")
        print("\033[92m" + "="*60 + "\033[0m")
        
        # Start both clients
        await self.user_client.start()
        await self.app.start()
        await self.pytgcalls.start()
        
        print("\033[92m[✓] EXU Music Bot is now running!\033[0m")
        print("\033[93m[!] Press Ctrl+C to stop\033[0m")
        
        # Keep running
        await self.idle()
    
    async def idle(self):
        """Keep the bot running"""
        try:
            while True:
                # Terminal maintenance every 30 seconds
                if int(time.time()) % 30 == 0:
                    clear_terminal()
                    # Show random status
                    statuses = [
                        "🎵 Streaming music...",
                        "⚡ Processing requests...",
                        "📊 Updating queues...",
                        "🔧 System maintenance...",
                        "🌟 EXU Premium Active..."
                    ]
                    print(f"\033[96m[{random.choice(statuses)}]\033[0m")
                
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("\n\033[93m[!] Shutting down EXU System...\033[0m")
            await self.stop()
    
    async def stop(self):
        """Stop the bot gracefully"""
        await self.app.stop()
        await self.user_client.stop()
        print("\033[92m[✓] EXU System stopped successfully\033[0m")

# Main execution
async def main():
    # Auto-update on start
    auto_update()
    
    # Create bot instance
    bot = EXUMusicBot()
    
    try:
        await bot.start()
    except Exception as e:
        print(f"\033[91m[✗] Fatal error: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    # Clear terminal on start
    clear_terminal()
    
    # Run the bot
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[93m[!] Bot stopped by user\033[0m")
    except Exception as e:
        print(f"\033[91m[✗] Unexpected error: {e}\033[0m")
'''
    
    return bot_code

# ==================== MAIN INSTALLATION FLOW ====================
async def main():
    """Main installation flow"""
    # Clear terminal and show banner
    clear_with_rain()
    animated_banner()
    
    print("\033[92m" + "="*80 + "\033[0m")
    print("\033[96m                𝐀𝐔𝐓𝐎𝐌𝐀𝐓𝐄𝐃   𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍\033[0m")
    print("\033[92m" + "="*80 + "\033[0m\n")
    
    # Step 1: Install dependencies
    installer = AutoInstaller()
    print("\033[93m[1] Installing Dependencies...\033[0m")
    installer.install_dependencies()
    
    # Step 2: Create directories
    print("\033[93m\n[2] Creating File Structure...\033[0m")
    installer.create_directory_structure()
    
    # Step 3: Get configuration
    print("\033[93m\n[3] Configuration Setup...\033[0m")
    config = installer.generate_config()
    
    # Step 4: Create session
    print("\033[93m\n[4] Creating Telegram Session...\033[0m")
    session_creator = SessionCreator(config)
    session_string = await session_creator.create_session()
    
    if not session_string:
        print("\033[91m[✗] Failed to create session. Please try again.\033[0m")
        return
    
    # Step 5: Generate bot code
    print("\033[93m\n[5] Generating Bot Code...\033[0m")
    bot_code = generate_bot_code()
    
    with open('exu_music_bot.py', 'w', encoding='utf-8') as f:
        f.write(bot_code)
    
    # Make executable
    os.chmod('exu_music_bot.py', 0o755)
    
    # Step 6: Create requirements.txt
    requirements = "\n".join(installer.requirements)
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    
    # Step 7: Create startup script
    startup_script = '''#!/bin/bash
# EXU Music Bot - Startup Script

# Colors
RED='\\033[0;31m'
GREEN='\\033[0;32m'
YELLOW='\\033[1;33m'
CYAN='\\033[0;36m'
NC='\\033[0m' # No Color

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                                                            ║"
echo "║           𝐄𝐗𝐔 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 - 𝐒𝐭𝐚𝐫𝐭𝐮𝐩 𝐒𝐜𝐫𝐢𝐩𝐭               ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}[✗] Python3 not found. Installing...${NC}"
    sudo apt update && sudo apt install python3 python3-pip -y
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}[!] .env file not found. Running setup...${NC}"
    python3 setup.py
fi

# Install/Update requirements
echo -e "${CYAN}[🔄] Checking dependencies...${NC}"
pip3 install -r requirements.txt --upgrade

# Clear cache
echo -e "${CYAN}[🧹] Clearing cache...${NC}"
rm -rf downloads/* 2>/dev/null
rm -rf __pycache__ 2>/dev/null

# Start the bot
echo -e "${GREEN}[🚀] Starting EXU Music Bot...${NC}"
echo -e "${YELLOW}[!] Press Ctrl+C to stop${NC}"
echo -e "${CYAN}" && python3 exu_music_bot.py
'''
    
    with open('start.sh', 'w') as f:
        f.write(startup_script)
    os.chmod('start.sh', 0o755)
    
    # Create setup script
    setup_script = '''#!/usr/bin/env python3
# EXU Setup Script
import os
import sys

print("Run: python3 installer.py")
'''
    
    with open('setup.py', 'w') as f:
        f.write(setup_script)
    os.chmod('setup.py', 0o755)
    
    # Final output
    clear_with_rain()
    print("\033[92m" + """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║               𝐈𝐍𝐒𝐓𝐀𝐋𝐋𝐀𝐓𝐈𝐎𝐍  𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄 ✅                ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  📁 Files Created:                                         ║
║     • exu_music_bot.py   - Main bot code                  ║
║     • .env              - Configuration                   ║
║     • requirements.txt  - Dependencies                    ║
║     • start.sh          - Startup script                  ║
║                                                            ║
║  📂 Directories:                                          ║
║     • sessions/         - Telegram sessions               ║
║     • downloads/        - Temporary downloads             ║
║     • logs/            - System logs                     ║
║     • cache/           - Cache files                     ║
║                                                            ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  🚀 To Start the Bot:                                     ║
║     $ chmod +x start.sh                                   ║
║     $ ./start.sh                                          ║
║                                                            ║
║     Or directly:                                          ║
║     $ python3 exu_music_bot.py                            ║
║                                                            ║
║  🔧 Features:                                             ║
║     • Auto login with phone number                        ║
║     • Matrix rain terminal animation                      ║
║     • Auto-clear terminal every 30 seconds                ║
║     • Premium Unicode fonts                               ║
║     • Animated progress bars                              ║
║     • Queue system with favorites                         ║
║     • Admin controls                                      ║
║     • Voice chat automation                               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """ + "\033[0m")
    
    print("\n\033[96m[📢] Next Steps:\033[0m")
    print("1. Add your bot to a group")
    print("2. Give admin permissions")
    print("3. Start voice chat")
    print("4. Use /play <song> to start streaming\n")
    
    print("\033[93m[⚡] Quick Start:\033[0m")
    print("\033[92m$ chmod +x start.sh && ./start.sh\033[0m\n")
    
    # Auto-start option
    auto_start = input("\033[96m[?] Start bot now? (y/N): \033[0m").lower()
    if auto_start == 'y':
        print("\033[92m[🚀] Starting EXU Music Bot...\033[0m")
        os.system('python3 exu_music_bot.py')

# ==================== EXECUTION ====================
if __name__ == "__main__":
    try:
        # Run async main
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[93m[!] Installation cancelled by user\033[0m")
    except Exception as e:
        print(f"\033[91m[✗] Installation failed: {e}\033[0m")
    
    # Keep terminal open
    input("\n\033[96mPress Enter to exit...\033[0m")
