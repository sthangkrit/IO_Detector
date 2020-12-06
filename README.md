## Installation

### Quick start on your local PC

1) Clone the repository, create environment and install requirements
```sh
$ cd io_project
$ virtualenv venv && source venv/bin/activate
$ pip install -r requirements.txt
$ python io.py 
```
Open in your browser http://127.0.0.1:5000 login = admin, password = admin

### Compile and run with Docker 
1) Clone the repository

```
$ cd kubyk
$ docker build -t anyname/kubyk .
$ docker run -d --name kubyk -p 80:80 anyname/kubyk
```
Use it. 
