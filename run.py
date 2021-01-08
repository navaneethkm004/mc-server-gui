import os

settings = """
#Minecraft server properties
#Sat Apr 18 07:42:27 UTC 2020
view-distance=4
max-build-height=256
server-ip=
level-seed=
enable-command-block=false
gamemode=0
server-port=8080
allow-nether=true
enable-rcon=false
enable-query=false
op-permission-level=4
generator-settings=
resource-pack=
level-name=world
player-idle-timeout=0
motd=A Minecraft Server
announce-player-achievements=true
force-gamemode=false
hardcore=false
white-list=false
pvp=true
texture-pack=
spawn-npcs=true
generate-structures=true
spawn-animals=true
snooper-enabled=true
difficulty=1
network-compression-threshold=256
level-type=DEFAULT
spawn-monsters=true
max-tick-time=60000
max-players=20
use-native-transport=true
online-mode=false
allow-flight=false
resource-pack-hash=
max-world-size=29999984
"""

installed = True
def write(filename,content):
  f = open(filename,"a")
  f.write("")
  f.close()
  f = open(filename,"w")
  f.write(str(content))
  f.close()

try:
  f = open("server-is-installed")
  f.close
except:
  write("server-is-installed","If this file is here, the server is installed. If you want to reinstall the server, then delete this file.")
  installed = False
if installed == False:
  os.system("rm -r -f server")
  os.system("install-pkg openjdk-8-jre-headless")
  os.system("mkdir server")
  os.system("cp server.jar server/server.jar")
  os.chdir("server")
  os.system("java -jar paper.jar")
  os.system("rm eula.txt")
  write("eula.txt","eula=true")
  write("server.properties",settings)
  os.system("java -jar server.jar")
else:
  os.chdir("server")
  os.system("java -jar server.jar")