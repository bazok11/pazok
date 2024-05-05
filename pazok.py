# file: pazok.py
import os
import time
import telebot
from telebot import types
import threading
import requests






#- - - - - - - - - - - - - - -- - - - - - -- - - - - #
#دالة ارسال اليوزرات

def tl(token, id, username, developer_url=""):
    bot = telebot.TeleBot(token)
    
    formatted_message = f"""
    *User Telegram:* `{username}`
    
    [Tool developer]({developer_url})
    """
    bot.send_message(id, formatted_message, parse_mode='MarkdownV2')

# Example usage:
if __name__ == "__main__":
    def send_telegram_message(token, id, username):
        tl(token, id, username)



#pazok.tl(توكن البوت, ايدي التلي, متغير اليوزر, رابط قناتك )

#- - - - - - - - - - - - - - -- - - - - - -- - - - - #



#مهم
def love():
    print("- I love Mariam")





#- - - - - - - - - - - - - - -- - - - - - -- - - - - #

#دالة تلاشي النص

def ta(text):
    def b_azok_print(text):
        i = 232
        while i <= 255:
            b = f"\u001b[38;5;{i}m"
            p = '\x1b[1m'
            terminal_size = os.get_terminal_size()
            max_width = terminal_size.columns - 1
            padding_width = (max_width - len(text)) // 2
            centered_text = " " * padding_width + text + " " * padding_width
            print(p + b + centered_text, end='\r')
            time.sleep(0.07)
            i += 1
    b_azok_print(text)
if __name__ == "__main__":
    def print_with_pazok(text):
        ta(text)


#pazok.ta("النص المطلوب")

#- - - - - - - - - - - - - - -- - - - - - -- - - - - #
            
                
                    
                        
                                
                                
#- - - - - - - - - - - - - - - - - - - - -- - - - - #

# دالة الخيوط
        
def run_program():
    pass

def sb(func, num_threads):
    num_threads = int(num_threads)
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=func)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()

ss = 5 
        
#def txt():
    

#pazok.sb(اسم الداله, عدد الخيوط)


#- - - - - - - - - - - - - - -- - - - - - -- - - - - #







#- - - - - - - - - - - - - - -- - - - - - -- - - - - #
#دالة ارسال التلي العاديه

def tll(message, token, id):
    mesg = message
    requests.get("https://api.telegram.org/bot" + str(token) + "/sendMessage?chat_id=" + str(id) + "&text=" + str(mesg))

#token = ""
#id = ""
#pazok.tll("هذه رسالة اختبار", token, id)

#- - - - - - - - - - - - - - -- - - - - - -- - - - - #





#- - - - - - - - - - - - - - -- - - - - - -- - - - - #
#دالة طلب توكن وايدي مره وحده

def info_bot():
    try:
        import time, os
        from colorama import init, Fore, Back, Style
        from cfonts import render
    except ImportError:
        os.system('pip install colorama')
        os.system('pip install cfonts')

    b = "\u001b[38;5;14m"  # سمائي
    m = "\u001b[38;5;15m"  # ابيض
    F = '\033[2;32m'  # أخضر
    Z = '\033[1;31m'  # أحمر
    ee = "\033[0;90m"  # رمادي الداكن
    C = "\033[1;97m"  # أبيض
    p = '\x1b[1m'  # عريض
    X = '\033[1;33m'  # أصفر
    B = '\033[2;36m'  # أزرق
    E = "\u001b[38;5;8m"  # رمادي فاتح
    o = "\u001b[38;5;208m"  # برتقالي
    p = '\x1b[1m'  # عريض

    sev_amg=f"""
        
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣧⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀
        ⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀
        ⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀
        ⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀
        ⠀⢸⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⡇⠀
        ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
        ⠀⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀
        
         
{E}             𝗜𝗙 𝗬𝗢𝗨 𝗧𝗬𝗣𝗘 𝗬, 𝗜𝗡𝗙𝗢 𝗦𝗔𝗩𝗘𝗗 𝗙𝗢𝗥 𝗡𝗘𝗫𝗧 𝗧𝗜𝗠𝗘

"""
    
    try:
        with open('.bot_info.txt', 'r') as file:
            lines = file.readlines()
            token = lines[0].strip()
            id = lines[1].strip()
    except FileNotFoundError:
        text = "Token"
        font = "block"
        letter_spacing = 2
        colors = ["gray", "cyan", "red"]
        b_azokatext = render(text, font=font, colors=colors, align='center', letter_spacing=letter_spacing)
        print(b_azokatext)
        token = input(f" - {b}Enter Token : {ee}")
        os.system('clear')

        text1 = "Chat ID"
        font1 = "block"
        letter_spacing1 = 1
        colors1 = ["gray", "cyan", "red"]
        b_azokatext = render(text1, font=font1, colors=colors1, align='center', letter_spacing=letter_spacing1)
        print(b_azokatext)
        id = input(f" - {b}Enter ID : {ee}")
        os.system('clear')

        print(sev_amg)
        save_data = input(f"{ee}-{o} 𝗗𝗢 𝗬𝗢𝗨 𝗪𝗜𝗦𝗛 𝗧𝗢 𝗦𝗔𝗩𝗘 𝗥𝗘𝗚𝗜𝗦𝗧𝗥𝗔𝗧𝗜𝗢𝗡 𝗜𝗡𝗙𝗢   {E} ({F}Y{ee}/{Z}N{E}){o}:{ee} ")
        if save_data.upper() == "Y":
            os.system('clear')
            with open('.bot_info.txt', 'w') as file:
                file.write(f"{token}\n{id}")
        elif save_data.upper() == "N":
            os.system('clear')
            pass
        else:
            exit(f"{Z}Invalid input. Please enter 'Y' or 'N'.")

    return token, id



#token, id = pazok.info_bot()



#- - - - - - - - - - - - - - -- - - - - - -- - - - - #

#الطباعه مع اشكال مكتبة rich

import time
from rich.console import Console

def pazok_rich(text, spinner, duration):
    console = Console()
    spinner_instance = console.status(text, spinner=spinner)
    spinner_instance.start()
    time.sleep(duration)
    spinner_instance.stop()

#pazok.pazok_rich("النص المطلوب", "النمط", الوقت)


#اسماء الانماط
def name_rich():
    rich_list = [
        "arrow",
        "christmas",
        "circle",
        "clock",
        "hearts",
        "moon",
        "pong",
        "runner",
        "star",
        "weather"
    ]

    for index, pattern in enumerate(rich_list, start=1):
        print(f"{index}. {pattern}")
        
#print(pazok.name_rich())

#- - - - - - - - - - - - - - -- - - - - - -- - - - - #

#الطباعه مع اشكال مكتبة halo

from halo import Halo
import time


def pazok_halo(text, spinner, duration):
    spinner_instance = Halo(text=text, spinner=spinner)
    spinner_instance.start()
    time.sleep(duration)
    spinner_instance.stop_and_persist(symbol='', text='')
    print(' ' * len(text), end='\r')

#pazok.pazok_halo("النص المطلوب", "النمط", الوقت)


#اسماء الانماط
def name_halo():
    halo_list = [
        "dots",
        "dots2",
        "dots3",
        "dots4",
        "dots5",
        "dots6",
        "dots7",
        "dots8",
        "dots9",
        "dots10",
        "dots11",
        "dots12",
        "line",
        "line2",
        "pipe",
        "simpleDots",
        "simpleDotsScrolling",
        "star",
        "star2",
        "flip",
        "hamburger",
        "growVertical",
        "growHorizontal",
        "balloon",
        "balloon2",
        "noise",
        "bounce",
        "boxBounce",
        "boxBounce2",
        "triangle",
        "arc",
        "circle",
        "square",
        "circleQuarters",
        "circleHalves",
        "squish",
        "toggle",
        "toggle2",
        "toggle3",
        "toggle4",
        "toggle5",
        "toggle6",
        "toggle7",
        "toggle8",
        "toggle9",
        "toggle10",
        "toggle11",
        "toggle12",
        "toggle13",
        "arrow",
        "arrow2",
        "arrow3",
        "bouncingBar",
        "bouncingBall",
        "smiley",
        "monkey",
        "hearts",
        "clock",
        "earth",
        "moon",
        "runner",
        "pong",
        "shark",
        "dqpb"
    ]

    for index, pattern in enumerate(halo_list, start=1):
        print(f"{index}. {pattern}")

#print(pazok.name_halo())


#- - - - - - - - - - - - - - -- - - - - - -- - - - - #

#تخويل الصور الى نقاط


def picture(image_path, height=20):
    import os
    from PIL import Image, ImageOps
    from picharsso import new_drawer
    
    pkg = ["picharsso"]
    for lib in pkg:
        try:
            __import__(lib)
            pass
        except ImportError:
            print(" جاري تثبيت المكاتب ،⬇️")
            os.system(f"pip install {lib}")

    try:
        image = Image.open(image_path)
        image = ImageOps.invert(image)
        drawer = new_drawer("braille", height=height)
        return drawer(image)
    except FileNotFoundError:
        print("المسار غير صحيح:", image_path)

#x="/storage/emulated/0/DCIM/100PINT/المنشورات/dbb76dbc7436ebe6defa7cd206103780.jpg"
#z=30

#jj=pazok.picture(x,z)
#print(jj)