<div align="center">

<h3>
  <b>

  🪶 <kbd>[**UFX**](https://github.com/Karthik-HR0/UFX)</kbd>

  </b>
</h3>

<h6>Fetch historical URLs and scan them for vulnerabilities with ease</h6>


<h6 align="center">
  URLs for Exploit (UFX)
A modular and customizable vulnerability discovery tool that fetches historical URLs from the Wayback Machine and scans them for potential exploits, including XSS, SQL Injection, LFI, and more. Easily extensible with user-defined patterns, UFX is designed for security researchers and ethical hackers.
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

`` #Features ``
<kbd>
Historical URL Scanning: Fetch URLs from the Wayback Machine.

Customizable Pattern Matching: Scan for specific patterns like XSS, SQLi, LFI, etc.

Command Line Interface: Easy-to-use CLI to scan domains with a variety of options.

Extensible: Easily add new patterns to scan for by adding JSON configuration files or by using the -q flag for pattern selection.

Modular Pattern Support: Supports multiple pre-configured vulnerability patterns (XSS, SQLi, etc.) stored in a modular patterns directory.

Output to File: Save results to a file for later analysis.


</kbd>
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

<h6 align="center">
  Inbuilt patterns
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
<kbd>FOR SHOWING AVAILABLE PATTERNS</kbd>
</div>

<br>

```bash
python3 ufx.py -d domain.com -q pattern
```

<div align="center">
<kbd> FOR HELP </kbd>
</div>

<br>

```bash
python3 ufx.py -h

```


<br>



<br>
<br>
<br>

<h6 align="center">kindly for hackers</h6>


<div align="center">
  <a href="https://github.com/Karthik-HR0"><img src="https://img.icons8.com/material-outlined/20/808080/github.png" alt="GitHub"></a>
  
