import sys
import argparse
import dns.resolver
import sys
import os
from colorama import Fore, Back, Style

os.system("clear")

# colors
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
magenta = Fore.MAGENTA
cyan = Fore.CYAN
white = Fore.WHITE

banner = f'''
   ███████╗██╗   ██╗██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
   ██╔════╝██║   ██║██╔══██╗██║  ██║██╔═══██╗██║   ██║████╗  ██║██╔══██╗
   ███████╗██║   ██║██████╔╝███████║██║   ██║██║   ██║██╔██╗ ██║██║  ██║
   ╚════██║██║   ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██║  ██║
   ███████║╚██████╔╝██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝   
   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝     
            
        {blue}    SubHound: Your Subdomain Enumeration Companion 
                    GitHub: @Vatsal-Shashwat                                                                    
'''

print(green + banner)
print(white + "")

def find_subdomains(domain, wordlist_file):
    try:
        with open(wordlist_file, 'r') as f:
            wordlist = f.read().splitlines()

        subdomains = set()

        for word in wordlist:
            subdomain = f"{word}.{domain}"
            try:
                answers = dns.resolver.resolve(subdomain, 'A')
                for answer in answers:
                    subdomains.add(subdomain)
                    print(f"{cyan}[+] Found subdomain: {subdomain}")
            except dns.resolver.NXDOMAIN:
                pass

        return subdomains

    except Exception as e:
        print(f"{red}\n[-] Error finding subdomains: \n\t{e}")
        return set()

def main():
    parser = argparse.ArgumentParser(description="Subdomain Finder")
    parser.add_argument("domain", help="Domain name to find subdomains for")
    parser.add_argument("wordlist", help="Path to wordlist file")
    args = parser.parse_args()

    domain = args.domain.strip()
    wordlist_file = args.wordlist.strip()

    subdomains = find_subdomains(domain, wordlist_file)

    print("\nSubdomains found:")
    for subdomain in subdomains:
        print(subdomain)

if __name__ == "__main__":
    main()

