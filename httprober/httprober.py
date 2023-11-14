#!/usr/bin/python3
import argparse
import httpx
import requests
import argparse
import os
import time as t 
from colorama import Fore,Style,Back 
import concurrent.futures 
import random
import sys


red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]

random_color = random.choice(colors)

storage = []

banner = '''

                           __  ____  __                   __             
                          / / / / /_/ /_____  _________  / /_  ___  _____
                         / /_/ / __/ __/ __ \/ ___/ __ \/ __ \/ _ \/ ___/
                        / __  / /_/ /_/ /_/ / /  / /_/ / /_/ /  __/ /    
                       /_/ /_/\__/\__/ .___/_/   \____/_.___/\___/_/     
                                    /_/                                  

                                    Author: D.Sanjai Kumar @CyberRevoltSecurititessssssssss

'''





parser = argparse.ArgumentParser(description=f"[{bold}{blue}INFO{reset}]: {bold}{white}A fast alive subdomains finder with new generation HTTPX client")

parser.add_argument("-f", "--filename", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}A filename that contains list of subdomains to probe and find alive subdomains", type=str)

parser.add_argument("-o", "--output",help=f"[{bold}{blue}INFO{reset}]: {bold}{white}File name to save the output",type=str)

parser.add_argument("-s", "--silent", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Switiching Silent flag will make the output to pipe", action="store_true")

parser.add_argument("-c", "--concurrency", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Concurrency level to make fast process", type=int, default=10)

parser.add_argument("-t", "--threads", help=f"[{blue}INFO{reset}]: {bold}{white}Threading level to make fast process", type=int, default=3)

parser.add_argument("-up", "--update", help=f"[{bold}{blue}INFO{reset}]: {bold}{white}Updated the Httprober to later version", action="store_true")

args = parser.parse_args()


def get_version():
    
    version = "v1.0.1"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Httprober/releases/latest"
    
    try:
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                
                print(f"[{blue}Version{reset}]: Httprober current version {version} ({green}latest{reset})")
                
                t.sleep(1)
                
            else:
                
                print(f"[{blue}Version{reset}]: Httprober current version {version} ({red}outdated{reset})")
                
                t.sleep(1)
                
        else:
            
            pass
        
        
    except KeyboardInterrupt as e:
        
        print(f"[{blue}INFO{reset}]: Httprober says BYE!")
        
        exit()
        
        
                
    except Exception as e:
        
        pass
    
def httpxer(url):
     
    try:
        
        with httpx.Client(verify=False) as requests:
            
            response = requests.get(url, timeout=10)

        status_code = response.status_code

        if status_code is not None:
         
            print(f"{url}")
            
            save(url)

        else:
            
            pass 
        
                          
    except httpx.TimeoutError as e:
         
        pass 
                          
                          
    except KeyboardInterrupt as e:
         
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Httprober says BYE!{reset}")
        
        exit()
          
        
    except Exception as e:
          
        pass
    
    
def save(url):
    
    try:
    
        if args.output:
            
            if os.path.isfile(args.output):
                
                filename = args.output
                
            elif os.path.isdir(args.output):
                
                filename = os.path.join(args.output, f"httprober_results.txt")
                
            else:
                
                filename = args.output
                
        if not args.output:
            
            filename = f"httprober_results.txt"
            
        
        with open(filename, "a") as w:
            
            w.write(url + '\n')
            
    except KeyboardInterrupt as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Httprober says BYE!{reset}")
        
        exit()
        
    except Exception as e:
        
        pass
    
def Im_here(storage):
    
    try:
        
        unique_storage = sorted(set(storage))
        

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.concurrency*args.threads) as executor:
            
         
           futures = [executor.submit(httpxer,url)for url in unique_storage]
           
           
        concurrent.futures.wait(futures)
        
           
    except KeyboardInterrupt as e:
        
        
        print(f"[{blue}INFO{reset}]: Httprober says BYE!")
        
        
        exit()

    except Exception as e:
        
         
        pass 
    
        

def main():
    
    try:
        
        if args.filename:
            
            if not args.silent:
        
                print(f"{random_color}{banner}{reset}")
        
                get_version()

            if args.filename and args.concurrency :
                
                if not args.silent:
                
                    print(f"[{blue}INFO{reset}]: User enabled the concurrecy with value of:  {args.concurrency}")
                
            if args.filename and not args.concurrency:
                
                pass
            
            if args.filename and args.threads :
                
                if not args.silent:
                
                    print(f"[{blue}INFO{reset}]: User enabled the Thread with value of:  {args.concurrency}")
                
            if args.filename and not args.threads :
                
                pass
            
            if args.filename and args.output :
                
                if not args.silent:
                
                    print(f"[{blue}INFO{reset}]: {bold}{white}Output will be saved in {args.output}")

            if args.filename and not args.output :
                
                if not args.silent:

                   print(f"[{red}INFO{reset}]: {bold}{white}Output file not given . Output will be saved automatically by Httprober{reset}")
               
               
            try:
                
                filename =  args.filename
                
                with open(filename, "r") as url :
                    
                    urls = url.read().splitlines()
                    
                    
                for url in urls:
                    
                    if url.startswith("https://") or url.startswith("http://"):
                          
                             storage.append(url)
                    else:
                         
                          new_url = f"https://{url}"
                          
                          new_http = f"http://{url}"
                          
                          storage.append(new_url)
                          
                          storage.append(new_http)
                          
                Im_here(storage)
                          
            except FileNotFoundError as e:
                
                print(f"[{red}INFO{reset}]: {bold}{white}{args.filename} not found. please check the file or file path exist or not!")
                
                exit()
              
        if args.update:
            
            version = "v1.0.1"
    
            url = f"https://api.github.com/repos/sanjai-AK47/Httprober/releases/latest"
    
            try:
        
        
              response = requests.get(url)
        
              if response.status_code == 200:
            
                data = response.json()
            
                latest = data.get('tag_name')
            
                if latest == version:
                
                
                    print(f"[{bold}{blue}Version{reset}]: {bold}{white}Httprober already in latest version don't worry :)")
                
                    exit()
                
                else:
                
                    print(f"[{bold}{blue}Update{reset}]: {bold}{white}Updating the Httprober{reset}")
                
                    t.sleep(1)
                    
                    os.system("pip install --upgrade httprober")
                    
                    print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Httprober Updated, Please check once for updated successfully or update it manually")
        
        
            except KeyboardInterrupt as e:
        
                print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Httprober says BYE!")
        
                exit()
                  
            except Exception as e:
        
                pass  
                exit()
                
                
        if not args.filename:
            
            try:
                
                for line in sys.stdin:
                      
                      url = line.strip()
                      
                      if url.startswith("https://") or url.startswith("http://"):
                          
                            storage.append(url)
                      else:
                         
                          new_url = f"https://{url}"
                          
                          new_http = f"http://{url}"
                          
                          storage.append(new_url)
                          
                          storage.append(new_http)
                          
                Im_here(storage) 
                          
            except KeyboardInterrupt as e:
                
                   print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Httprober says BYE!")
                   
                   exit()
                   
            except Exception as e:
                
                   print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Stdin Error occured for Httprober")
                   
                   exit()
                
                
    except KeyboardInterrupt as e:
        
        print(f"[{bold}{blue}INFO{reset}]: {bold}{white}Httprober says BYE!{reset}")
        
        exit()
        
    except Exception as e:
        
        pass
        
        
if __name__ == "__main__" :
    
    main()
    

                
