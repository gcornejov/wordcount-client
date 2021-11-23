# WordCount Client
Dockerized Python Client for WordCount API excercise.

## Pre-Requisites

Make sure you have [Docker](https://www.docker.com/) with Docker Compose installed on your machine.

## Installation

### Download git repositories

Download **this** and [wordcount-api](https://github.com/gcornejov/wordcount-api) repositories.

### Allocate repositories

Unzip if necessary, then set both directories in the same folder, the structure should look like this (**make sure the directory names are the same as they appear in the diagram bellow**):

```
	root_dir/ (Example name)
	├── wordcount-api/
	└── wordcount-client/
```

### Move docker-compose file

Inside wordcount-api is the docker-compose file called **wordcount-compose.yaml** for deploying the containers, once located, move it to the root_dir/. Then it should look like this:

```
	root_dir/ (Example name)
	├── wordcount-api/
	├── wordcount-client/
	└── wordcount-compose.yaml
```

### Deploy the containers

Open the shell and run de command bellow:

```sh
docker-compose -f wordcount-compose.yaml up
```

The container should be running and ready to use. ✌🏻

## Usage

To use the API you need to make a request from de Client terminal, as:

```python
python3 wordcount_client.py [--file | -f] <file_name>
```

Also, you need to have a plain-text file with the words to coun in the data-in/ directory.

So, create a file in the data-in/ directory:

```sh
touch data-in/document.txt
```

Then write some words on the file with (The image generated comes with nano app installed):

```sh
nano data-in/document.txt
```

Now you are set! 💪🏻 Let´s run the program and see the magic happen. ✨