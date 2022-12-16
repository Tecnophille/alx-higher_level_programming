#!/bin/bash
# Take in URL, add header variable, displays "Hello Holberton School!"; Usage: ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
curl -s -H "X-School-User-Id":98 "$1"
