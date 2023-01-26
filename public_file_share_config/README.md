# Fatboy Home Network wide public Folder

## Overview

Provides an always available file share available to any user connected to the physical fatboy home network. 

## Design Concept 

Use std windows file share configured to support anon access. Most of teh actual set and configuration of the file share will be done by the installer

## Implementation 

Turn on and configure various windows functions. Most of the action is in the installer (see the install section below)

## Installation 

1. Turn on the required windows components 
1. create the public directory - default `public` and `public\temporary`
2. Set config  to support 100% anon access 
4. Set the permissions for the directory to allow anon access

