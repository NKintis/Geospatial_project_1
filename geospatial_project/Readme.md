###Getting Started

**Building and Running with Docker**

**To build and run the project using Docker, follow these steps:**

**1. Clone the repository:**
Indented code
	git clone https://github.com/NKintis/Geospatial_project_1
	cd geospatial_project_1
	cd geospatial_project

**2. Build the Docker image:**
'''shell sudo docker build -t image1 -f dockerfile .'''

**3. Run the Docker container:**
'''shell'
docker run -p 8888:8888 -e USERNAME= -e PASSWORD= -e VAR1= -e VAR2= -e VAR3= -e VAR4= -e 		 VAR5= -e VAR6= image1
'''

**Fill the environment variables (USERNAME, PASSWORD, VAR1, etc.) with your desired values.**

VAR1=MIN_LONGITUDE // VAR2=MIN_LATITUDE // VAR3=MAX_LONGITUDE // VAR4=MAX_LATITUDE// VAR5=START_DATE // VAR6=END_DATE

Example:
'''shell
docker run -p 8893:8888 -e USERNAME=nkintis -e PASSWORD=Nikos1234 -e VAR1=22.792511 -e VAR2=38.462192 -e VAR3=23.041077 -e VAR4=38.550313 -e VAR5=2018-01-01 -e VAR6=2018-01-02 image1
'''

###Accessing JupyterLab

Open a web browser and navigate to http://localhost:8888/ or open the link provided after running the container.


