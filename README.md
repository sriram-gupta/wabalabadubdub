# wabalabadubdub

This is a python project. Here we will write a python web server , 
and we will be deploying it after dockerisng the application 

Steps 
<ul>
    <li>Create a virtual Environment [python3 -m venv myenv] </li>
    <li> Activate Virtual Env : [source myenv/bin/activate ]</li>
    <li> Install dependencies [ fastapi , uvicorn ] </li>
    <li> curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore </li>
    <li> Created main.py</li>
    <li> Run and test app , then freeze the dependencies [pip freeze > requirement.txt]</li>
    <li> Created Dockerfile</li>
    <li> [docker build -t wabalabadubdub:1.0.0 .]</li>
    <li> [docker run -it -p 8000:8000 wabalabadubdub:1.0.0 ]</li>
</ul>