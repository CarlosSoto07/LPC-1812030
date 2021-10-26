#!/bin/bash

function host_name(){
	var1=$(hostname -I)
	echo "hostname : " $var1
}

function if_config(){
	var2=$(curl ifconfig.me)
	echo "ip privada: " $var2
}

function nmap_ip(){
	var3=$(nmap 192.168.106.*)
	echo "nmap segmento de red privado: " $var3
}

function nmap_pag(){
	var4=$(nmap scanme.nmap.org)
	echo "nmap pagina nmap: " $var4
}

host_name
if_config
nmap_ip
nmap_pag
