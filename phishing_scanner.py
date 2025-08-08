import re
from urllib.parse import urlparse

def is_https(url):
    return url.lower().startswith("https://")

def contains_suspicious_keywords(url):
    keywords = ['login', 'verify', 'update', 'secure', 'account', 'banking', 'free', 'bonus']
    return any(word in url.lower() for word in keywords)

def uses_ip_address(url):
    ip_pattern = r"(https?:\/\/)?(\d{1,3}\.){3}\d{1,3}"
    return re.match(ip_pattern, url)

def too_many_subdomains(url):
    try:
        parsed = urlparse(url)
        domain_parts = parsed.netloc.split('.')
        return len(domain_parts) > 3
    except:
        return False

def analyze_url(url):
    flags = []

    if not is_https(url):
        flags.append("Not HTTPS")
    if contains_suspicious_keywords(url):
        flags.append("Suspicious Keywords")
    if uses_ip_address(url):
        flags.append("Uses IP Address")
    if too_many_subdomains(url):
        flags.append("Too Many Subdomains")

    if flags:
        return f"\n[RESULT] 🚨 Suspicious URL Detected!\nReasons: {', '.join(flags)}"
    else:
        return "\n[RESULT] ✅ The URL appears safe."

def main():
    print("=== Phishing Link Scanner ===")
    url = input("Enter the URL to scan: ").strip()
    result = analyze_url(url)
    print(result)

if __name__ == "__main__":
    main()