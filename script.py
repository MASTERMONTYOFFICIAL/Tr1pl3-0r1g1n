#!/usr/bin/python3
import argparse
import dns.resolver

def save_output(ip,output):
    with open(output,'a') as f:
        f.write("\n" + str(ip))

def resolve(sub,output):
    try:
        answer = dns.resolver.resolve(sub,'A')
        for ip in answer:
            save_output(ip,output)
            print(f"{sub} : {ip}")
    except Exception:
        pass

def main():
    try:
        parser = argparse.ArgumentParser(prog="Tr1pl3-0r1g1n",description="Find Origin IP behind subdomain via AAA records !!")
        parser.add_argument("-l","--list",help="list of subdomains ")
        parser.add_argument("-o","--output",help="Save the path of output")
        args = parser.parse_args()

        if not args.output:
            args.output = "Tr1pl3-0r1g1n_results.txt"
            print(f"[*] Default output file: {args.output}")

        if args.list and args.output:
            print(f"[*] Starting DNS resolution from file: {args.list}")
            print(f"[*] Saving IP addresses to file: {args.output}")
            with open(args.list,"r") as f:
                for sub in f:
                    if sub.startswith('https://'):
                        subdomain = sub.replace('https://','').strip()
                        resolve(subdomain , args.output)
                    elif sub.startswith('http://'):
                        subdomain = sub.replace('http://','').strip()
                        resolve(subdomain , args.output)
                    else:
                        subdomain = sub.strip()
                        resolve(subdomain,args.output)
    except KeyboardInterrupt:
        print("\n[!] Exit by User !!")
        exit(0)

if __name__ == "__main__":
    main()