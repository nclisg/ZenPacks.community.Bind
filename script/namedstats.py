#!/usr/bin/env python 

import sys
import datetime 

if len(sys.argv) < 2:
    print "CRITICAL - file not found"
    sys.exit(1) 

f = open (sys.argv[1], 'r') 

datatype = 0

incoming = { 
            'A':0,
            'A6':0,
            'AAAA':0,
            'AFSDB':0,
            'ANY':0,
            'AXFR':0,
            'CNAME':0,
            'DNAME':0,
            'DNSKEY':0,
            'DS':0,
            'EID':0,
            'HINFO':0,
            'IXFR':0,
            'LOC':0,
            'MAILB':0,
            'MX':0,
            'NAPTR':0,
            'NS':0,
            'NSEC':0,
            'NSEC3PARAM':0,
            'NULL':0,
            'Others':0,
            'PTR':0,
            'RESERVED0':0,
            'RRSIG':0,
            'SOA':0,
            'SPF':0,
            'SRV':0,
            'SSHFP':0,
            'TKEY':0,
            'TLSA':0,
            'TXT':0,
            'WKS':0
            }

outgoing = {
            'A':0,
            'AAAA':0,
            'AFSDB':0,
            'ANY':0,
            'CNAME':0,
            'DNSKEY':0,
            'DS':0,
            'HINFO':0,
            'MX':0,
            'NAPTR':0,
            'NS':0,
            'NULL':0,
            'Others':0,
            'PTR':0,
            'RESERVED0':0,
            'RRSIG':0,
            'SOA':0,
            'SPF':0,
            'SRV':0,
            'SSHFP':0,
            'TXT':0,
            'WKS':0
            }

serverstats = {
            'auth_queries_rejected':0,
            'duplicate_queries_received':0,
            'IPv4_requests_received':0,
            'other_query_failures':0,
            'queries_caused_recursion':0,
            'queries_dropped':0,
            'queries_resulted_in_authoritative_answer':0,
            'queries_resulted_in_non_authoritative_answer':0,
            'queries_resulted_in_NXDOMAIN':0,
            'queries_resulted_in_nxrrset':0,
            'queries_resulted_in_referral_answer':0,
            'queries_resulted_in_SERVFAIL':0,
            'queries_resulted_in_successful_answer':0,
            'recursive_queries_rejected':0,
            'requested_transfers_completed':0,
            'requests_with_EDNS(0)_received':0,
            'response_policy_zone_rewrites':0,
            'responses_sent':0,
            'responses_with_EDNS(0)_sent':0,
            'TCP_requests_received':0,
            'transfer_requests_rejected':0,
            'truncated_responses_sent':0,
            'update_requests_rejected':0
              }

start = 0

for index, line in enumerate(f):
    if line.startswith("+++ Statistics Dump +++"):
        start = index     

f.seek(start + 1)

for index, line in enumerate(f):

    if line.startswith("[View"):
        continue

    if line.startswith("++ Zone Maintenance Statistics ++"):
        datatype = 4
        continue

    if line.startswith("++ Incoming Queries ++"):
        datatype = 1
        continue
    elif line.startswith("++ Outgoing Queries ++"):
	datatype = 2
        continue
    elif line.startswith("++ Name Server Statistics ++"):
        datatype = 3
        continue
 
    if datatype == 1:
	fields = line.split()
        incoming[fields[1]] = fields[0]

    if datatype == 2:
        fields = line.split()
        outgoing[fields[1]] = fields[0]

    if datatype == 3:
        fields = line.split()
        title = "_".join(fields[1:])
        serverstats[title] = fields[0]

sys.stdout.write("OK|")

for label, data in incoming.iteritems():
    sys.stdout.write( "in." + label +"=" + str(data) + " ")

for label, data in outgoing.iteritems():
    sys.stdout.write( "out." + label +"=" + str(data) + " ")

for label, data in serverstats.iteritems():
    sys.stdout.write( "server." + label +"=" + str(data) + " ")







