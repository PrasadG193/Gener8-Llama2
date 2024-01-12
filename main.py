import os
import json
import subprocess
from pathlib import Path
from flask import request, make_response

def gener8(request):
  req_prompt = request.data.decode("utf-8") 
  if len(req_prompt) == 0:
    return build_response("Bad request!", 400)

  # Request model
  response = subprocess.run(["./main", "-m", "./models/7B/ggml-model-q4_0.bin", "-n", "1024", "--repeat_penalty", "1.0", "-p", "give me kubernetes resource yaml specs for "+req_prompt+" with no explaination", "--log-disable"],
                        capture_output = True,
                        text = True
                    )
  return build_response(response.stdout, 200)

def build_response(result, status_code):
  response = make_response(str(result), status_code)
  response.mimetype = "text/plain"
  response.headers.add("Access-Control-Allow-Origin", "*")
  response.headers.add("Access-Control-Allow-Headers", "Content-Type")
  return response
