# Fatboy Home Network Virtual Private Network (VPN) proxy Service 

## Overview 

### What is a VPN

provides encrypted communication between the Fatboy Home network and a network end point (web site, torrent peer, etc)
hides your real IP - your web page requests and torrent connections can only be traced back to the VP provider

Provides privacy for the 3Ps -  Porn, Piracy & Political Dissent.

At the OS level windows  provides the ability  to connect via  VPN (TODO ref ms do that shows how to connect to a VPN)
Which means all network calls made on that machine are routed via the VPN. 

### What is a proxy 

A proxy is a 

This is not always what you want

why is a proxy a usefule idea 

### Network VPN Proxy Service 


## Design Concept 

Connect one machine - the PROXY_SERVER to a VPN provides via std windows proxy setting (ref windows doco).

Any network connection made on that machine will be routed ia the VPN connection. 

Run a proxy service on PROXY_SERVER. Any call made via the proxy PROXY_SERVER is is routed via the network VPN connection. 

Run the torrent client on PROXY_SERVER or have the  torrent client use the VPN  proxy service. 

Connect a firefox via the PROXY_SERVER. This provides an always accessible protected / private browsing session. 


## Implementation 

Squid with an almost empty config file 

The machine running the proxy will always be connected via the VPN. Resulting VPN usage issues (see above). 

### Different install Configs

|Name | Description |
|---|---|
| Own Machine | One machine is designated PROXY_SERVER. This machine is connected via the VPN and runs the proxy service. |
| Share with torrent | One machine is designated PROXY_SERVER. This machine is connected via the VPN and runs the proxy service. The same machine also run the torrent client (the component doing torrent up/down load.) and the internal torrent web interface. |
| Common Server | The common server is connected via the VPN. The VPN proxy server is then run on the common server |


## Installation 

1. Squid std install
2. copy `.\src\squid.conf` to squid config folder