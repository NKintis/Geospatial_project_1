## Getting Started
**Download Docker.**

Docker Desktop for Windows:
```shell
curl -fsSL https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe -o DockerDesktopInstaller.exe
start DockerDesktopInstaller.exe
```

Docker Desktop for Mac (Apple):
```shell
curl -fsSL https://desktop.docker.com/mac/stable/Docker%20Desktop%20Installer.dmg -o DockerDesktopInstaller.dmg
hdiutil attach DockerDesktopInstaller.dmg
cp -R /Volumes/Docker\ Desktop/Docker\ Desktop.app /Applications
hdiutil detach /Volumes/Docker\ Desktop
```

Docker Engine for Linux:
```shell
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```


**Building and Running with Docker.**

**To build and run the project using Docker, follow these steps:**

**1. Clone the repository:**
```shell
	git clone https://github.com/NKintis/Geospatial_project_1
	cd Geospatial_project_1
	cd geospatial_project
```

**2. Build the Docker image:**
```shell
docker build -t image1 -f dockerfile .
```

**3. Run the Docker container:**
```shell
docker run -p 8888:8888 -e USERNAME= -e PASSWORD= -e VAR1= -e VAR2= -e VAR3= -e VAR4= -e 		 VAR5= -e VAR6= image1
```

Fill the environment variables (USERNAME, PASSWORD, VAR1, etc.) with your desired values.
* VAR1=MIN_LONGITUDE 
* VAR2=MIN_LATITUDE 
* VAR3=MAX_LONGITUDE
* VAR4=MAX_LATITUDE
* VAR5=START_DATE
* VAR6=END_DATE

Example:
```shell
docker run -p 8893:8888 -e USERNAME=nkintis -e PASSWORD=Nikos1234 -e VAR1=22.792511 -e VAR2=38.462192 -e VAR3=23.041077 -e VAR4=38.550313 -e VAR5=2018-01-01 -e VAR6=2018-01-02 image1
```

### Accessing JupyterLab

Open the link provided after running the container to access the processed data on Jupyterlab.

docker run -p 8888:8888 -e USERNAME=thanasisdrivas -e PASSWORD=Nopassaran123 -e VAR1=22.1508722196129 -e VAR2=38.7551983381184 -e VAR3=23.447884976054 -e VAR4=39.7244518411376 -e VAR5=2019-01-01 -e VAR6=2019-01-10 image1

