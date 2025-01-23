<div align="center">

<h3>
  <b>

  🛸 <kbd>[**UFX**](https://github.com/Karthik-HR0/UFX)</kbd>

  </b>
</h3>

<h6>Fetch historical URLs and scan them for vulnerabilities with ease</h6>


<h6 align="center">
  URLs for Exploit (UFX)
A modular and customizable vulnerability discovery tool that fetches historical URLs from the Wayback Machine,otx vault and scanable for potential exploits, including XSS, SQL Injection, LFI, and more. Easily extensible with user-defined patterns, UFX is designed for security researchers and ethical hackers.
</h6>

</div>

<br>
<br>
<br>

> [!Important]
> **_UFX is designed for security researchers. It may include false positives, so always verify results manually!._**

<br>
<br>
<br>

<h1 align="center">

  Features

</h1>

<div align="center">

| Category              | Core Capabilities                                  | Advanced Functionality                              | Intelligent Automation                               |
|-----------------------|----------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| **Historical URL Fetching** | • _`Wayback Machine Integration`_ <br>• _`Fetch up to 50,000 URLs`_ | • _`Duplicate URL Filtering`_ <br>• _`Domain-wide Coverage`_ | • _`Error Handling for Network Issues`_ <br>• _`Efficient URL Parsing`_ |
| **Pattern Matching**   | • _`Predefined Patterns for XSS, SQLi, LFI`_ <br>• _`Custom Pattern Support`_ | • _`Dynamic Query Analysis`_ <br>• _`Heuristic-based Matching`_ | • _`Automatic Parameter Detection`_ <br>• _`Multi-pattern Scanning`_ |
| **Ease of Use**        | • _`Command-Line Interface (CLI)`_ <br>• _`Single-command Execution`_ | • _`Optional Output File Generation`_ <br>• _`Quick Pattern Listing`_ | • _`Simplified Workflow`_ <br>• _`Auto Pattern Detection Based on -q Input`_ |
| **Extensibility**      | • _`Modular Design with Pattern Management`_ <br>• _`Python Package Installation`_ | • _`Easily Extendable for New Vulnerabilities`_ <br>• _`Centralized Pattern Module`_ | • _`Continuous Tool Updates`_ <br>• _`Custom Integration for Unique Patterns`_ |

</div>
<br>
<br>

<h6 align="center">Install</h6>

```bash
git clone https://github.com/Karthik-HR0/UFX
cd UFX
pip install -r requirements.txt
```

<br>
<br>
<details>
<summary> <h6 align="center">
  Inbuilt patterns :↓
</h6> </summary>
<h6 align="center">
  AVAILABLE INBUILT PATTERNS 
</h6>

<pre>
  <i>
Allin1gf

allparam

api-keys

asymmetric-keys_secrets

auth

aws-keys

aws-keys_secrets

aws-mws-key

aws-s3_secrets

aws-secret-key

badwords

base64

blacklist

bufferoverflow

ccode

cors

crypto

debug-pages

debug_logic

domxss

endpoints

execs

facebook-access-token

facebook-oauth

facebook-oauth_secrets

facebook-token_secrets

firebase.json

firebase_secrets

fw

github

github_secrets

go-functions

google-keys_secrets

google-oauth_secrets

google-service-account_secrets

google-token_secrets

heroku-keys_secrets

http-auth

idor

img-traversal

insubs

interestingEXT

interestingparams

interestingsubs

inurls

ip

js-interesting

js-sinks

json-sec

jsvar

jwt

Ifi

mailchimp-keys_secrets

mailgun-keys_secrets

meg-headers

or

parsers

paypal-token_secrets

php-callbacks

php-codeexec

php-commandexec

php-curl

php-errors

php-informationdisclosure

php-open-filesystem-handler

php-read-filesystem

php-serialized

php-sinks

php-sources

php-write-filesystem

picatic-keys_secrets

rce-2

rce

redirect

s3-buckets

sec

secret-ext

secret-urls

secrets

serial

servers

slack-token

slack-token_secrets

slack-webhook

slack-webhook_secrets

sqli-error

sqli

square-keys_secrets

square-secret

ssrf
    
ssti

strings

stripe-keys_secrets

swearwords

takeovers

truffle

twilio-key

twilio-keys_secrets

twitter-oauth

twitter-oauth_secrets

twitter-secret

twitter-token_secrets

typos

upload-fields

urlparams
    
urls

urls_params

xml

xpath

xss

xxe

    </details>
    
  </i>
</pre>

<br>
<br>
<br>

<h6 align="center">
  example commands
</h6>


```bash
python3 ufx.py -d testphp.vulnweb.com -q xss
# For finding hidden target urls for xss 
```

<div align="center">
<kbd>FOR SHOWING AVAILABLE PATTERNS :↓</kbd>
</div>

<br>

```bash
python3 ufx.py -d domain.com -q pattern
```

<div align="center">
<kbd> FOR HELP :↓ </kbd>
</div>


<br>

```bash
python3 ufx.py -h

```
<div align="center">
<kbd> OUTPUT OF XSS PATTERN</kbd>

``` ufx -d example.com -q xss

[*] Scanning domain: example.com
[*] Using pattern: XSS
[+] Found 12,345 historical URLs.

https://example.com/search?q=sub
https://example.com/page.php?lang=en
https://example.com/login?redirect=101
https://example.com/query?keyword=words



```

<div align="center">
<kbd> OUTPUT OF LFI PATTERN</kbd>

```
ufx -d example.com -q lfi

[*] Scanning domain: example.com
[*] Using pattern: LFI
[+] Found 10,000 historical URLs.

https://example.com/view.php?file=../../../../etc/passwd
https://example.com/download.php?path=/var/log/apache2/access.log
https://example.com/index.php?dir=../../../../


```

</div>

<br>



<br>
<br>
<br>

<h6 align="center">kindly for hackers</h6>


<div align="center">
  <a href="https://github.com/Karthik-HR0"><img src="https://img.icons8.com/material-outlined/20/808080/github.png" alt="GitHub"></a>
  
