# Indentation-JS-Compiler
or indent javascript

# Quick Introduction 

This is a kind of an **interpreated syntax** derived from JS rather than a new language 
Lasy to open brackets and reorder them 
you like python syntax (like me) with indentations
this tools is made for you ! (and me for sure :smile: ) 
look attentively to this description before using it
> i used compiler rather than script to make in highlight **the concept of a new syntax** 

# Getting started

easy guide to start using JSI the syntax

### Setting parameters

You can find in the **compiler.py**
```Python
#Here Put your file name
YourFileName = "test.jsi"
'''needs to be in .JSI format'''
YourOutputFileName = "result.js"
'''needs to be in .JS format'''
```


### Compilation

After setting your files
just be in the same path as your files and type in the terminal
```powershell
python compiler.py
```

# Syntax 

Good news ! Same syntax as JS dont be lost 
use colon ":" instead of opening brackets
and use indetations "\t" to 

### Important To know

* "::" for object in an object 
> look at the example  below

* When using arrow functions in perenthese "()" the closing parenthese ")" should be in a diffrent line than the last instruction of the scope
> example using map() function below 

* Be sure that your **tab** caracter in your text editor is set to **4 Four spaces** 
> this is required so the compiler can work

### Syntax Errors

You can notice your errors in the generated JS file and fix it 
So , you already get it , the syntax errors related with JS are the same in JSI

> if you find an issue related with the compiler and  not with your JS code 
**Please submit this issue**


# Samples
### JSI syntax

```dart
//this is a classic function
function A():
    console.log("function A")
//this is an arrow function
const arrowfunc = (e) => :
    if (e > 0) :
        console.log("greater than 0")
    else :
        console.log("negative")
//this is an object JSON
obj = :
    id : 0,
    anotherProp : "banana",
    objInObj ::
        id : 5,
        props : "pancake"
//a class also
class Rabbit :
    constructor(name,color,age,height,weight):
        this.name = name
        this.color = color
        this.array = [age,height,weight]
    //conveting to int using map in this method
    adabtType():
        this.array.map((e) => :
            int(e)
        )
        console.log("Done")
```
### JS result

```javascript
//this is a classic function
function A(){
    console.log("function A")
}
//this is an arrow function
const arrowfunc = (e) => {
    if (e > 0) {
        console.log("greater than 0")
	}
    else {
        console.log("negative")
	}
}
//this is an object JSON
obj = {
    id : 0,
    anotherProp : "banana",
    objInObj :{
        id : 5,
        props : "pancake"
	}
}
//a class also
class Rabbit {
    constructor(name,color,age,height,weight){
        this.name = name
        this.color = color
        this.array = [age,height,weight]
	}
    //conveting to int using map in this method
    adabtType(){
        this.array.map((e) => {
            int(e)
		}
        )
        console.log("Done")
	}
}

```

# Contribution 

Tts an *open source* project show your imagination
you can look to the **Issues tab** to help us improve the compiler (or script) 
