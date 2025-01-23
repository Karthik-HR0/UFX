#!/usr/bin/env python3

import requests
import argparse
import sys
from urllib.parse import urlparse
from module.patterns import PatternLoader
from module.logo import Logo


class UFX:
    def __init__(self, domain, pattern_name, pattern_loader):
        self.domain = domain
        self.pattern_data = pattern_loader.load_pattern(pattern_name)

    def get_wayback_urls(self):
        """Fetch URLs from Wayback Machine."""
        wayback_url = "https://web.archive.org/cdx/search/cdx"
        params = {
            "url": f"*.{self.domain}/*",
            "collapse": "urlkey",
            "output": "text",
            "fl": "original",
            "limit": 50000
        }
        try:
            response = requests.get(wayback_url, params=params, timeout=30)
            response.raise_for_status()
            return list(set(url.strip() for url in response.text.splitlines() if url.strip()))
        except requests.RequestException as e:
            print(f"[!] Error fetching Wayback URLs: {e}")
            return []

    def get_alienvault_urls(self):
        """Fetch URLs using AlienVault OTX API."""
        url = f"https://otx.alienvault.com/api/v1/indicators/hostname/{self.domain}/url_list"
        params = {"limit": 500, "page": 1}
        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()
            return [entry["url"] for entry in data.get("url_list", [])]
        except requests.RequestException as e:
            print(f"[!] Error fetching AlienVault URLs: {e}")
            return []

    def filter_urls(self, url):
        """Filter URLs based on loaded patterns."""
        try:
            parsed_url = urlparse(url)
            query_params = parsed_url.query
            for pattern in self.pattern_data.get("patterns", []):
                if pattern in query_params:
                    return True
            return False
        except Exception:
            return False

    def run(self):
        """Main execution method."""
        print(f"[*] Scanning domain: {self.domain}")
        
        # Fetch URLs from various sources
        wayback_urls = self.get_wayback_urls()
        alienvault_urls = self.get_alienvault_urls()

        # Combine and deduplicate URLs
        all_urls = set(wayback_urls + alienvault_urls)
        print(f"[+] Total unique URLs fetched: {len(all_urls)}")
        
        # Filter URLs
        filtered_urls = [
            url for url in all_urls if self.filter_urls(url)
        ]
        return filtered_urls


def main():
    parser = argparse.ArgumentParser(
        description="UFX - Universal Filter Tool",
        epilog="Example: python3 ufx.py -d example.com -q xss -o results.txt"
    )
    parser.add_argument(
        "-d", "--domain", required=True, 
        help="Target domain to scan (e.g., example.com)"
    )
    parser.add_argument(
        "-q", "--pattern", required=True, 
        help="Pattern name to use (e.g., xss, sql_injection, lfi)"
    )
    parser.add_argument(
        "-o", "--output", type=str, 
        help="Save results to the specified output file"
    )
    
    args = parser.parse_args()
    
    # Display the logo/banner
    Logo.display()
    
    pattern_loader = PatternLoader()

    # List available patterns if invalid pattern is provided
    if args.pattern not in pattern_loader.list_patterns():
        print(f"[!] Invalid pattern '{args.pattern}'.")
        print("[*] Available patterns:")
        for pattern in pattern_loader.list_patterns():
            print(f"  - {pattern}")
        sys.exit(1)
    
    try:
        ufx = UFX(args.domain, args.pattern, pattern_loader)
        filtered_urls = ufx.run()
        
        if filtered_urls:
            print("[!] Filtered URLs:")
            for url in filtered_urls:
                print(url)
            
            # Save results to file if specified
            if args.output:
                with open(args.output, 'w') as f:
                    f.write("\n".join(filtered_urls))
                print(f"[+] Results saved to {args.output}")
        else:
            print("[*] No matching URLs found.")
    
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
