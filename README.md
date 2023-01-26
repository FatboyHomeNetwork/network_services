# Fatboy Home Network Services

A core support component of the Fatboy Home Network. Provides some basic network services like DNS and file shares, as well as some home network focus like a torrent and VPN proxy service. 

The following network services are provided: 

1. Network wide DNS for all servers a non network admin user will use [network_dns_config](.\network_dns_config\README.md)
2. Network wide VPN proxy service [network_vpn_proxy](.\network_vpn_proxy\README.md)
3. A xxx standard Torrent Service accessible via web interface and available to all users within the network [torrent_service_wrapper](.\torrent_service_wrapper\README.md)
5. Network wide file share: \Public, & \Public\Temporary available to all users within the network [public_file_share_config](.\public_file_share_config\README.md)
6. Network user home directory creating and hosting. Create  home directory. Migrating from local to network home directory. configure windows security to  control access. [network_home_dir](.\network_home_dir\README.md)
4. Network wide off site back up services. Schedule backups of folders within the network. Recovery in place. Recovery from disaster. [off_site_backup_config](.\off_site_backup_config\README.md)

