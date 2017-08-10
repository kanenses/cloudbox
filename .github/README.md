<img src="cloudbox-animated.gif" loop=infinite width="200" alt="Cloudbox">

Cloudbox is an Ansible playbook for deploying a cloud media server stack on an Ubuntu server with the use of Docker containers.

>This project is limited to specifically 16.04 Ubuntu LTS, designed for fresh systems. Do not install on an already setup server, or prepare for unintended consequences.


## Tools Installed


|                                                                 | Full | Feeder | Plex |
|:--------------------------------------------------------------- |:----:|:------:|:----:|
| [Docker][627bd283]                                              |  √   |   √    |  √   |
| [Plex][10952c53] ([docker][d369f92b])                           |  √   |        |  √   |
| [PlexPy][363c0adc] ([docker][cda70c13])                         |  √   |        |  √   |
| [Plex_AutoScan][96e27fd1]                                       |  √   |        |  √   |
| [Sonarr: develop][8ae81bb6] ([docker][fa005e4a])                         |  √   |   √    |      |
| [Radarr: nightly][8211f62c] ([docker][5f7edfff])                         |  √   |   √    |      |
| [NZBGet][2e2bad08] ([docker][a9b9645e])                         |  √   |   √    |      |
| [NZBHydra][a0cc8c46] ([docker][50ba3cbb])                       |  √   |   √    |      |
| [rTorrent][512b104c]/[ruTorrent][8d6ce857] ([docker][344a7c4b]) |  √   |   √    |      |
| [Jackett][1caa43a0] ([docker][cab1a251])                        |  √   |   √    |      |
| [Rclone][b4cef019]                                              |  √   |   √    |      |
| [Plexdrive][0367302f]                                           |  √   |   √    |  √   |
| [PlexRequests][458fc748] ([docker][0044f8e1])                   |  √   |        |  √   |
| [Organizr][d328b256] ([docker][1e468891])                       |  √   |   √    |  √   |
| [Portainer][726e0b6f]                                           |  √   |   √    |  √   |
| [UnionFS-Fuse][6e8f308f]                                        |  √   |   √    |  √   |
| [UnionFS_Cleaner][f20acc3e]                                     |  √   |   √    |      |
| [Watchtower][a98faaaf]                                          |  √   |   √    |  √   |
| Kernel, motd, sysctl, etc...                                    |  √   |   √    |  √   |

  [627bd283]: https://www.docker.com "Docker"
  [10952c53]: https://www.plex.tv "Plex"
  [d369f92b]: https://github.com/plexinc/pms-docker "Official Docker container for Plex Media Server"
  [363c0adc]: https://github.com/JonnyWong16/plexpy "PlexPy"
  [cda70c13]: https://github.com/linuxserver/docker-plexpy "linuxserver/plexpy"
  [96e27fd1]: https://github.com/l3uddz/plex_autoscan "Plex_AutoScan"
  [8ae81bb6]: https://sonarr.tv "Sonarr"
  [fa005e4a]: https://github.com/linuxserver/docker-sonarr "linuxserver/sonarr"
  [8211f62c]: https://radarr.video "Radarr"
  [5f7edfff]: https://github.com/hotio/docker-radarr "hotio/radarr"
  [2e2bad08]: https://nzbget.net "NZBGet"
  [a9b9645e]: https://github.com/linuxserver/docker-nzbget "linuxserver/nzbget"
  [a0cc8c46]: https://github.com/theotherp/nzbhydra "NZBHydra"
  [50ba3cbb]: https://github.com/linuxserver/docker-hydra "linuxserver/hydra"
  [512b104c]: https://github.com/rakshasa/rtorrent/wiki "rTorrent"
  [8d6ce857]: https://github.com/Novik/ruTorrent "ruTorrent"
  [344a7c4b]: https://github.com/linuxserver/docker-rutorrent "linuxserver/rutorrent"
  [1caa43a0]: https://github.com/Jackett/Jackett "Jackett"
  [cab1a251]: https://github.com/linuxserver/docker-jackett "linuxserver/jackett"
  [b4cef019]: https://rclone.org "Rclone"
  [0367302f]: https://github.com/dweidenfeld/plexdrive "Plexdrive"
  [6e8f308f]: http://manpages.ubuntu.com/manpages/zesty/man8/unionfs.8.html "UnionFS-Fuse"
  [f20acc3e]: https://github.com/l3uddz/unionfs_cleaner "UnionFS_Cleaner"
  [a98faaaf]: https://github.com/v2tec/watchtower "Watchtower"
  [458fc748]: https://github.com/lokenx/plexrequests-meteor "PlexRequests"
  [0044f8e1]: https://github.com/linuxserver/docker-plexrequests "linuxserver/plexrequests"
  [d328b256]: https://github.com/causefx/Organizr "Organizr"
  [1e468891]: https://github.com/linuxserver/docker-organizr "lsiocommunity/organizr"
  [726e0b6f]: https://portainer.io "Portainer"



## Installation

### Installing Ansible

Run the following command. Press `Y` when asked to confirm. 
```
sudo apt-get install python-pip && sudo pip install ansible==2.3.1.0
```
Note: Ansible v2.3.1.0 is the current stable version (v2.3.2.0 has a bug where docker_container state=stopped causes container to be removed).


### Cloning Git Project

1. Go to home folder:

  ```bash
  cd ~/
  ```

2. Clone project:

  ```bash
  git clone https://github.com/l3uddz/cloudbox
  ```

### Running the Ansible script

1. Go into cloudbox folder

  ```bash
  cd cloudbox
  ```

2. Decide on what type of Cloudbox you want: `full`,`feeder`, or `plex` .

3. Run the following Ansible command, with the preferred option from #2 (`--tag "option"`) - quotes not needed.

  Example:

  ```bash
  sudo ansible-playbook cloudbox.yml --tag full
  ```

## Customization

See wiki.

## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

TODO: Write history

## To Do

- simpler install method

## Credits

TODO: Write credits

## License

TODO: Write license
