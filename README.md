# Gener8-Llama2
Generate Kubernetes resource YAML manifests from a text prompt

Gener8-Llama2 is a simple Kubernetes resource YAML generator based on Meta's Llama-2 model

## Architecture

![image](https://github.com/rutu-k/Gener8-Llama2/assets/25836028/410311c5-599b-4bdd-b1e3-cf3f7aacdc15)


## Prerequisites

Please make you have Python 3.8.X or higher version

### Requesting access to Llama Models
1. Request for accessing Llama models [here](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)
![image](https://github.com/PrasadG193/Gener8-Llama2/assets/25836028/17f92fa9-db87-41f0-ac82-7c9ad818f2fb)

You will receive a mail with the URL to download the model which we will use later.
![image](https://github.com/PrasadG193/Gener8-Llama2/assets/25836028/86e123ea-36d8-4604-a61f-5f163d665f15)

### Setup Llama2 Model
Make sure you have all the repos downloaded: `llama`, and `llama.cpp`

First download the `llama-2–7b-chat` model from llama.
   ```sh
   $ cd llama/
   $ /bin/bash ./download.sh
     Enter the URL from email: https://download.llamameta.net/*?XXXXXXXXXXXXX
     Enter the list of models to download without spaces (7B,13B,70B,7B-chat,13B-chat,70B-chat), or press Enter for all: 7B-chat
   ```
   
### Converting and Quantizing Downloaded Model
Now we have to convert the downloaded model to f16 format and quantize it to reduce its size.

1. Build llama.cpp project
    ```
    $ cd llama.cpp
    $ make
    
2. First activate a virtual env and install all the requirements
   ```sh
   $ python3 -m venv llama2
   $ source llama2/bin/activate
   $ python3 -m pip install -r requirements.txt
   ```

3. Then convert the model into f16 format and quantize it
   ```sh
   $ python3 convert.py --outfile models/7B-chat/ggml-model-f16.bin --outtype f16 ../../llama2/llama/llama-2-7b-chat --vocab-dir ../../llama2/llama
   $ ./quantize  ./models/7B-chat/ggml-model-f16.bin ./models/7B-chat/ggml-model-q4_0.bin q4_0
   ```
3. Make sure you change the `vocab_size` in llama/llama-2-7b-chat/params.json to 32000
   ```sh
   $ cat llama/llama-2-7b-chat/params.json
   {"dim": 4096, "multiple_of": 256, "n_heads": 32, "n_layers": 32, "norm_eps": 1e-06, "vocab_size": 32000}
   ```

## Build

Before proceeding further, please make sure you have setup the Llama2 model using the steps given in Prerequisites section

1. Run python server
```
$ python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
```

2. Use Curl or Webapp to send query to server
To query using webapp, open `/PATH/TO/REPO/Gener8-Llama2/frontend/index.html` in your browser
and enter the description of the K8s resource you want to generate specs for

  ![Screenshot 2024-01-12 at 11 43 10 AM](https://github.com/PrasadG193/Gener8-Llama2/assets/7098659/43bde8e0-ed6f-4b47-b4b6-a7199f69b010)



## Contributing

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:
- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
