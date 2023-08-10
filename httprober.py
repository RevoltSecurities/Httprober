import argparse
import httpx
import requests
import argparse
import os
import time as t 
from colorama import Fore,Style,Back 
from concurrent.futures import ThreadPoolExecutor

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Style.RESET_ALL

storage = []

banner = '''

                           __  ____  __                   __             
                          / / / / /_/ /_____  _________  / /_  ___  _____
                         / /_/ / __/ __/ __ \/ ___/ __ \/ __ \/ _ \/ ___/
                        / __  / /_/ /_/ /_/ / /  / /_/ / /_/ /  __/ /    
                       /_/ /_/\__/\__/ .___/_/   \____/_.___/\___/_/     
                                    /_/                                  

                                    Author: D.Sanjai Kumar

'''





parser = argparse.ArgumentParser(description=f"[{blue}INFO{reset}]: A fast alive subdomains finder with new generation HTTPX client")

parser.add_argument("-l", "--list", help=f"[{blue}INFO{reset}]: File that contains list of subdomain to find alive subdomain", type=str, required=True)
parser.add_argument("-o", "--output",help=f"[{blue}INFO{reset}]: File name to save the output",type=str)
parser.add_argument("-c", "--concurrency", help=f"[{blue}INFO{reset}]: Concurrency level to make fast process", type=int, default=10)
parser.add_argument("-t", "--threads", help=f"[{blue}INFO{reset}]: Threading level to make fast process", type=int, default=3)
args = parser.parse_args()


def get_version():
    
    version = "v1.0.0"
    
    url = f"https://api.github.com/repos/sanjai-AK47/Httprober/releases/latest"
    
    try:
        
        
        response = requests.get(url)
        
        if response.status_code == 200:
            
            data = response.json()
            
            latest = data.get('tag_name')
            
            if latest == version:
                
                message = "latest"
                
                print(f"[{blue}Version{reset}]: Httprober current version {version} ({green}latest{reset})")
                
                t.sleep(1)
                
            else:
                
                message ="outdated"
                
                print(f"[{blue}Version{reset}]: Httprober current version {version} ({red}outdated{reset})")
                
                t.sleep(1)
                
        else:
            
            pass
                
    except Exception as e:
        
        pass


def essential_check():


    
    print(f"{blue}{banner}{reset}")

    get_version()

    if not args.list:

        print(f"[{red}INFO{reset}]: File not found that contains list of subdomains")


    elif args.list:

        try:


            with open(args.list, "r") as r:

                pass 

            print(f"[{blue}INFO{reset}]: File  found in {args.list}")

        except Exception as e:

            print(f"[{red}INFO{reset}]: File not found that contains list of subdomains")

            exit()


    else:

        print(f"[{red}INFO{reset}]: File not found that contains list of subdomains")

        exit()

    
    if args.output:

        print(f"[{blue}INFO{reset}]: Output will be saved in {args.output}")

    else:

        print(f"[{red}INFO{reset}]: Output file not given . Output will be saved automatically by Httprober")


    if args.concurrency:
         
         print(f"[{blue}INFO{reset}]: User enabled the concurrecy with value of {args.concurrency}")



         if args.concurrency > 50:
              
              print(f"[{red}ICAUTION{reset}]: User concurrency is {args.concurrency} which is more than 50 these may can cause overconsuming the resource in your machiene")

         else:
         
           pass
    else:
         
         print(f"[{blue}INFO{reset}]: User not enabled concurrency so continuing with default value {args.concurrency}")

    if args.threads:
         
         print(f"[{blue}INFO{reset}]: User enabled the Threads with value of {args.threads}")



         if args.threads > 7:
              
              print(f"[{red}ICAUTION{reset}]: User Threads is {args.threads} which is more than 7 these may can cause overconsuming the resource in your machiene")

         else:
         
           pass
    else:
         
         print(f"[{blue}INFO{reset}]: User not enabled Threads so continuing with default value {args.threads}")


def load_it():

    try:


            with open(args.list, "r") as r:

                subdomains = r.read().splitlines()
                for subdomain in subdomains:

                    http_url =f"http://{subdomain}" 

                    https_url = f"https://{subdomain}"

                    storage.append(http_url.strip())

                    storage.append(https_url.strip())

    except Exception as e:

            print(f"[{red}INFO{reset}]: File not found that contains list of subdomains")

            print(e)

            exit()


    


def httpxer(url):
     
     try:
        
        with httpx.Client() as client:
            
            response = client.get(url, timeout=10)

            status_code = response.status_code

        if status_code is not None:
         
             print(url)

             if args.output:
                 
                 with open(args.output, "a") as w: 

                     w.write(f"{url}\n") 

             else:
                 
                 
                 with open("httprober_results.txt", "a") as w: 

                     w.write(f"{url}\n") 

        else:
             
             pass
        

     except httpx.HTTPError as http_err:
                
                if 'certificate has expired' in str(http_err):

                    status_code = response.status_code

                    print(url)

                    if args.output:
                 
                       with open(args.output, "a") as w: 

                          w.write(f"{url}\n") 

                    else:
                 
                 
                        with open("httprober_results.txt", "a") as w: 

                          w.write(f"{url}\n") 
        
        
     except Exception as e:
          
          pass


def main():

    essential_check()

    load_it()

    try:

        with ThreadPoolExecutor(max_workers=args.concurrency*args.threads) as executor:
         
           futures = [executor.submit(httpxer,url)for url in storage]

    except Exception as e:
         
         print(f"[{red}INFO{reset}]: Error in concurrency and threading values")

if __name__ == "__main__":

    main()

            