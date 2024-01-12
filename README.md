# Gener8-Llama2
Generate Kubernetes resource YAML manifests from a text prompt

Gener8-Llama2 is a simple Kubernetes resource YAML generator based on Meta's Llama-2 model

## Prerequisites

### Setup Llama2 Model

### Requesting access to Llama Models


### Converting Downloaded Model


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
