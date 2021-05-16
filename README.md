# dawgctf-2021

This is not a write-up, just a simple documentation.
My write-ups are on https://neptunian.medium.com/

## Dr. Hrabowskis

Very simple Flag inside HTML Code
DawgCTF{WeLoveTrueGrit}

## Just a Comment

I think the challenge would involve some analysis on the pcap file but...

strings justacomment.pcapng | grep -i dawg > flag.txt
DawgCTF{w3 h34r7 0ur 1r4d 734m}

## phriedmansystems

This was a lot of fun, but I wasn't used to osint challenges and I tought it was a web-only challenge.

via robots file, we got an interesting login page. It has a 2-step login, first validating the user and then validating the password.
The first part is a hash of the username, so we can confirm existing users in the employees page.

The password is a hash of username and password, holding secret data.

Unfortunately (for me) there was a REAL PHONE NUMBER working and you could change the user password and get the flag. I found this reading someones Write-up later.

I didn't make it, but it was interesting enough!