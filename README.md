# ZenPacks.community.Bind

This zenpack uses rndc to generate statics for bind.  The stats are parsed via a python script executed from a command data source.

Setup steps:

- Configure the server for rndc 
    (https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/s2-bind-rndc.html)
- Setup a cronjob to run rndc stats every 5 minutes
- Copy the script/namedstats.py to the server you want to montior (I use puppet for this)
- Update the Bind monitoring template to point to where the script resides and the path to the named.stats file
- Set the command username and password of an account with sufficient privildeges to read the named.stats file -  I used an account which is in the named group
