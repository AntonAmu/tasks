# tasks
### Repository setup:
1. Clone this repository:
```
git clone https://github.com/AntonAmu/tasks.git.
```
2. Move to repo:
```
cd <repo>
```
3. Create virtual environment
```
python -m venv venv 
```
4. Activate virtual environment
```
venv\Scripts\activate.bat
```
5. Install the requirements in the current environment
```
pip install -r requirements.txt
```
6. Create .env files out of .env.example files with .env.example file, for example like this:

### How to use counter:
1. Run the command:
```
python counter.py '<string>'
```
### How to use reverser:
1. To get only letters from the string on reverse order, each letter on a new line -> Run the command:
```
python reverser.py '<string>' 
```
2. To all char from the string on reverse order, each char on a new line -> Run the command:
```
python reverser.py '<string>' --all
```
### How to use cryptographer:
1. To get encoded message -> Run the command:
```
python cryptographer.py "<string>" encode 
```
2. To get decoded message -> Run the command:
```
python cryptographer.py "<encoded_string>" decode #or '<encoded_string>' (case when $ in encoded string)
```