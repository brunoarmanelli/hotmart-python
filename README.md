
# Unoffical Hotmart Hotconnect 2 Python Module

Hotmart Hotconnect requests made easy.

### Usage
  
````python
import hotconnect

hotmart = hotconnect.Hotmart(
    id='YOUR_ID',
    secret='YOUR_SECRET',
    key='YOUR_KEY'
)
````

and then

````python
response = hotmart.get_order()
print(response)
````
